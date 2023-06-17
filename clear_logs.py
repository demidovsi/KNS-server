import threading
import time
import common as cd
import datetime
import config


def get_count():
    answer, ok, status = cd.send_rest(
        'v1/content/count/{schema}/{table_name}'.format(
            schema=config.schema_name, table_name='logs'), 'GET')
    if ok:
        return int(answer)


class ClearLogs(threading.Thread):
    time_begin = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        cd.write_log_db('LOAD', 'clear_logs', 'Поток "Чистка лог файла" стартовал')
        while True:
            t0 = time.time()
            cd.login()
            try:
                start_count = get_count()
                first_date = datetime.date.today() - datetime.timedelta(days=7)
                sql_text = "delete from {schema}.logs where at_date_time < '{year}-{month}-{day}';".format(
                    schema=config.schema_name, year=first_date.year, month=first_date.month,
                    day=first_date.day
                )
                answer, ok, status = cd.send_rest('v1/NSI/script/execute', 'PUT', params=str(sql_text),
                                                  token_user=cd.token)
                if not ok:
                    cd.write_log_db('ERROR', 'clear_logs', 'Ошибка записи в БД: ' + answer)
                finish_count = get_count()
                st = ' Было строк ' + str(start_count) + '. Стало строк ' + str(finish_count)
                cd.write_log_db('Sleep', 'clear_logs', 'Тайм-аут на сутки.' + st, td=time.time() - t0)
                time.sleep(86400)
            except Exception as er:
                cd.write_log_db('ERROR', 'clear_logs', f"{er}; Повторим через час", td=time.time() - t0)
                time.sleep(3600)
