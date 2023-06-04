from requests.exceptions import HTTPError
import requests
import json
import config
import base64

endpoint = "odata"
token = None
app_lang = None


def send_get_request(url):
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(config.base_url + url, headers=headers, timeout=100)
        if response.ok: # Check the response status code
            # Try to parse the response JSON
            try:
                data = response.json()  # Process the data as needed
                return data, True, response.status_code
            except json.JSONDecodeError as e:
                st = f"Error response: {e}"
                # print(st)
                return st, False, ''
        else:
            return response.text, False, response.status_code
            # print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        st = f"Request error: {e}"
        # print(st)
        return st, False, ''


def send_rest(mes, directive="GET", params=None, lang='', token_user=None):
    js = {}
    if token_user is not None:
        js['token'] = token_user
    if lang == '':
        lang = 'ru'
    if directive == 'GET' and 'lang=' not in mes:
        if '?' in mes:
            mes = mes + '&lang=' + lang
        else:
            mes = mes + '?lang=' + lang
    else:
        js['lang'] = lang   # код языка пользователя
    if params:
        if type(params) is not str:
            params = json.dumps(params, ensure_ascii=False)
        js['params'] = params  # дополнительно заданные параметры
    try:
        headers = {"Accept": "application/json"}
        response = requests.request(directive, config.url + mes.replace(' ', '+'), headers=headers, json=js)
    except HTTPError as err:
        txt = f'HTTP error occurred: {err}'
        print('ERROR: send_rest', txt)
        return txt, False, None
    except Exception as err:
        txt = f'Other error occurred: {err}'
        print('ERROR: send_rest', txt)
        return txt, False, None
    else:
        return response.text, response.ok, '<' + str(response.status_code) + '> - ' + response.reason


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def login():
    global token, app_lang
    result = False
    txt_z = {"login": config.user_name, "password": decode('abcd', config.kirill), "rememberMe": True}
    try:
        headers = {"Accept": "application/json"}
        response = requests.request(
            'POST', config.url + 'v1/login', headers=headers,
            json={"params": txt_z}
            )
    except HTTPError as err:
        txt = f'HTTP error occurred: {err}'
    except Exception as err:
        txt = f'Other error occurred: : {err}'
    else:
        try:
            txt = response.text
            result = response.ok
            if result:
                js = json.loads(txt)
                if "accessToken" in js:
                    token = js["accessToken"]
                if 'lang' in js:
                    app_lang = js['lang']
            else:
                token = None
                return txt, result, token
        except Exception as err:
            txt = f'Error occurred: : {err}'
    # print(txt)
    return txt, result, token


def str1000(number, sep=' '):
    """
    Вывод целого значения числа с разделением по тысячам (три знака) через указанную строку (по умолчанию - пробел).
    :param number: значение целого числа,
    :param sep: - разделитель между тройками цифр,
    :return: возвращается строка, типа 123 456 789.
    """
    if number is None:
        return ''
    if type(number) == int or type(number) == str:
        n = str(number)[::-1]
        return sep.join(n[i:i + 3] for i in range(0, len(n), 3))[::-1]
    return str(number)
