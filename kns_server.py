import common
import time
import config


skip = 0


def do_load():
    global skip
    common.login()
    t_begin = time.time()
    skip = 0
    for unit in config.entities:
        top = 100
        if 'skip' in unit:
            skip = unit['skip']
        data = list()
        t0 = time.time()
        to_db = 0
        while to_db == 0 or len(data) > 0:
            data, ok, status = common.send_get_request(unit['endpoint'] + '?$top={top}&$skip={skip}'.format(
                top=top, skip=skip))
            if ok:
                data = data['value']  # одна строка таблицы
                fields = unit['fields']
                mas_values = ''
                for row in data:   # одна строка таблицы
                    st = ''
                    for field in fields:  # поля строки таблицы
                        st = st + ',' if st != '' else st
                        if field['field'] not in row or row[field['field']] is None:
                            st = st + 'null'
                        else:
                            if 'str' in field.keys():
                                st = st + "'" + row[field['field']].replace("'", "''") + "'"
                            else:
                                st = st + str(row[field['field']])
                    st = 'select {schema}.{function_name}({values});\n'.format(
                        schema=config.schema_name, function_name=unit['function_name'], values=st)
                    mas_values = mas_values + st
                t1 = time.time()
                if mas_values != '':
                    answer, ok, status = common.send_rest('v1/NSI/script/execute', 'PUT', params=str(mas_values),
                                                          token_user=common.token)
                    to_db = to_db + time.time() - t1
                    if not ok:
                        print('\n', end='')
                        print('ERROR', str(answer))
                        return False
                if len(data) < 100:
                    break
                print('...', unit['endpoint'], '\tcount=' + common.str1000(skip + len(data)) + ';',
                      "\tt=%.3f sec;" % (time.time() - t0), "Прошло=%.3f sec;" % (time.time() - t_begin),
                      "\tt_db=%.3f sec" % to_db, '\r', end='', flush=True)
                skip += 100
            else:
                print('\n', end='')
                print('ERROR', data, status)
                return False
        print('===', unit['endpoint'], '\tcount=' + common.str1000(skip + len(data)) + ';',
              "\tt=%.3f sec;" % (time.time() - t0), "Прошло=%.3f sec;" % (time.time() - t_begin),
              "\tt_db=%.3f sec" % to_db, flush=True)
        skip = 0
    return True


if __name__ == '__main__':
    result = False
    while not result:
        result = do_load()
        if not result:
            count = 0
            while count < 60:
                count += 1
                print('Ожидание: ' + str(count) + ' сек из 60', '\r', end='', flush=True)
                time.sleep(1)
