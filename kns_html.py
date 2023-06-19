import threading
import webbrowser

import common as cd
import config
import time
import json
import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import re
import webbrowser
# from selenium import webdriver
import urllib
from requests_html import HTMLSession
import requests_html


http_adapter = HTTPAdapter(max_retries=3)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "rbzid=oo6XcliuU2QC8We87874BO9GA9Pg41SRibMzr0fR4Pso9n1VAQKm0oyrnLJPVriQf9JI2FTIAoCtAV4KnJPeVGRS4rFQgN0ATx7FeG5ZsPhPER2d4NunXqSNLzg7eF+v3AlmD7G/hNyUlA5matUZg84CJQfK7RPsmDJVvhF+lDGlaBU8veOPv/ir/BtL3k6x503nnMNKWVQHCTrqwrUCWVQPIH7wmGKCucKl8DO4PwVIpJ4CmxNG0jx3/yDiSQUW; rbzsessionid=887378f03050c7c41a47db6ab65b13ff; _gid=GA1.3.1186344673.1686827652; WSS_FullScreenMode=false; deviceChannel=Default; _gat=1; _ga=GA1.1.312130872.1686827652; _ga_F5VXQ9Z7N5=GS1.1.1686827652.1.1.1686827968.0.0.0",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}


class HtmlParserBill(threading.Thread):
    row_count = 0
    row_from = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def load_row_count(self):
        answer, ok, status = cd.send_rest(
            'v1/content/count/{schema}/{table_name}'.format(
                schema=config.schema_name, table_name='nsi_bill'), 'GET')
        if ok:
            self.row_count = int(answer)
            return True
        else:
            cd.write_log_db('ERROR', 'HTMLParserBill', 'Ошибка чтения количества BILL: ' + str(answer))

    def save_to_base(self, response, bill_id, url, t_begin):
        result = True
        if response.ok:  # 200
            trans = BeautifulSoup(response.text, 'lxml').find_all(class_='LawDocTextTd')
            st = ''
            for tran in trans:
                param = tran.text.split('-')
                st1 = "select {schema}.pw_trans_data({billid}, '{action_date}', '{action_name}', " \
                      "'{action_source}');\n".format(
                        schema=config.schema_name, billid=bill_id,
                        action_date=param[0], action_name=param[1].replace("'", "''"),
                        action_source=param[2].replace("'", "''"))
                st = st + st1
            cd.write_log_db('Load bill', 'HTMLParserBill', url,
                            law_id=bill_id, td=time.time() - t_begin, page=self.row_from // 100,
                            file_name='Trans count=' + str(len(trans)))
            if st != '':  # записываем в БД
                answer, ok, status = cd.send_rest('v1/NSI/script/execute', 'PUT', params=str(st),
                                                  token_user=cd.token)
                if not ok:
                    cd.write_log_db('ERROR Load bill', 'HTMLParserBill',
                                    'Ошибка записи в БД: ' + answer,
                                    law_id=bill_id)
                    result = False
        else:
            cd.write_log_db('ERROR Load bill', 'HTMLParserBill',
                            'Ошибка чтения bill с сайта КНЕССЕТа: ' + url,
                            law_id=bill_id, td=time.time() - t_begin)
            result = False
        return result

    def run(self):
        cd.write_log_db('LOAD', 'HtmlParserBill', 'Поток скачивания информации по законам КНЕССЕТ загружен')
# прочитать список всех законов
        while True:
            self.row_from = 0  # сначала всех законов
            while self.load_row_count() and self.row_from < self.row_count:
                t0 = time.time()
                answer, ok, status = cd.send_rest(
                    'v1/view/{schema}/{view}?row_from={row_from}&row_count=100&order=order by billid desc'.format(
                        schema=config.schema_name, view='get_url_bills', row_from=self.row_from), 'GET')
                if not ok:
                    cd.write_log_db('ERROR', 'HTMLParserBill', 'Ошибка чтения get_url_bills ' + str(answer),
                                    td=time.time() - t0)
                    time.sleep(3600)
                else:
                    answer = json.loads(answer)
                    session = None
                    good = True
                    for unit in answer:
                        t = time.time()
                        bill_id = unit['1']
                        url = unit['0']
                        if session is None:
                            session = requests.Session()
                            session.mount(url, http_adapter)
                        r = session.get(url, headers=headers, timeout=(100, 100))
                        r.encoding = r.apparent_encoding
                        good = self.save_to_base(r, bill_id, url, t)
                        if not good:
                            break
                    if good:
                        self.row_from += 100
                    else:  # ошибка чтения с сайта или ошибка записи в БД
                        cd.write_log_db('Sleep', 'HTMLParserBill', 'Ожидание 1 минута и повторим страницу', td=time.time() - t0)
                        time.sleep(60)  # ждем минуту, а потом пытаемся повторить
            cd.write_log_db('Sleep', 'HTMLParserBill', 'Ожидание 1 сутки')
            time.sleep(86400)  # не удалось прочитать количество законов или их кол-во закончилось
