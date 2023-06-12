import threading
import common as cd
import config
import time
import json
import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup


http_adapter = HTTPAdapter(max_retries=3)


class HtmlParserBill(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        cd.write_log_db('LOAD', 'HtmlParserBill', 'Поток скачивания информации по законам КНЕССЕТ загружен')
# прочитать список всех законов
        while True:
            t0 = time.time()
            answer, ok, status = cd.send_rest('v1/view/{schema}/{view}'.format(
                schema=config.schema_name, view='get_url_bills'), 'GET')
            if not ok:
                cd.write_log_db('ERROR', 'HTMLParserBill', 'Ошибка чтения get_url_bills ' + str(answer),
                                td=time.time() - t0)
                time.sleep(3600)
            answer = json.loads(answer)
            for unit in answer:
                t = time.time()
                bill_id = unit['1']
                url = unit['0']
                session = requests.Session()
                session.mount(url, http_adapter)
                r = session.get(url, timeout=(100, 100))
                cd.write_log_db('Load bill', 'HTMLParserBill', 'Считан bill с сайта ГД\n' + url,
                                law_id=bill_id, td=time.time() - t)
                if r.ok:  # 200
                    lws = BeautifulSoup(r.text, 'lxml').find_all('div', class_='LawDocTextTd')
                    pass
                    # if len(lws) == 0:
                    #     return 0
