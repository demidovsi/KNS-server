import common
import time
import config
import kns_api
import kns_html
import clear_logs


if __name__ == '__main__':
    common.login()
    # загрузка по API
    # api_knesset = kns_api.ApiKnesset()
    # api_knesset.start()
    # начальная загрузка законов или их проверка из HTML на трассировку действий с законами
    # obj_html_parser_bill = kns_html.HtmlParserBill()
    # obj_html_parser_bill.start()
    # чистка лога
    obj_clear_logs = clear_logs.ClearLogs()
    obj_clear_logs.start()
    while True:
        time.sleep(60)
