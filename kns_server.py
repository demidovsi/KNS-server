import common
import time
import config
import kns_api
import kns_html


if __name__ == '__main__':
    common.login()
    # загрузка по API
    api_knesset = kns_api.ApiKnesset()
    api_knesset.start()
    # загрузка законов или их проверка из HTML на трассировку действий с законами
    obj_html_parser_bill = kns_html.HtmlParserBill()
    obj_html_parser_bill.start()
    while True:
        time.sleep(60)
