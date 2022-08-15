import requests
from requests.structures import CaseInsensitiveDict
import json
import datetime
from datetime import timedelta
import os
from dotenv import load_dotenv


REGION_CODES = {
    'novosib': "RU-NVS",
    'barnaul': 'RU-ALT',
    'omsk': 'RU-OMS',
    'tomsk': 'RU-TOM',
    'kemerovo': 'RU-KEM',
    'krasnoyarsk': 'RU-KYA',
    'irkutsk': 'RU-IRK',
    'chita': 'RU-ZAB',
    'tyva': 'RU-TY',
    'buratia': 'RU-BU',
    'altai': 'RU-GA',
    'khakasia': 'RU-KK'
}

load_dotenv()
TOKEN = os.getenv('AUTH_TOKEN')
TODAY_DATE = datetime.date.today()
TODAY_DATE_DOT = TODAY_DATE.strftime("%d.%m.%Y")
URL = "http://127.0.0.1:8000/region/"
URL_PARSE = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/covid_data.json?do=region_stats&code='


def dateconv(date):
    """Конвертация даты в формат БД"""
    return datetime.datetime.strptime(date,"%d.%m.%Y").date()

def strtodate(str):
    """Конвертация строки в дату YYYY-MM-DD"""
    return datetime.datetime.strptime(str,"%Y-%m-%d").date()




def check_update():
    """Проверка наличия обновлений за сегодня"""
    count_updated = 0 #количество обновленных регионов
    for reg_name in REGION_CODES:
        code = REGION_CODES.get(reg_name)
        url_parse_reg = f'{URL_PARSE}{code}'
        stats = requests.get(url_parse_reg).json()
        if dateconv(stats[0]['date']) == TODAY_DATE:
            count_updated += 1
    if count_updated == 12:
        return True
    else:
        return False


def parse_date(date_to_parse):
    """Парсинг добавление в БД данных за определенную дату"""
    YESTERDAY = (dateconv(date_to_parse) - timedelta(days=1)).strftime("%d.%m.%Y")
    for reg_name in REGION_CODES:
        code = REGION_CODES.get(reg_name)
        url_parse_reg = f'{URL_PARSE}{code}'
        stats = requests.get(url_parse_reg).json()
        value_yesterday = next(x for x in stats if x['date'] == YESTERDAY)
        value = next(x for x in stats if x['date'] == date_to_parse)
        sick = value['sick']
        sick_today = value['sick'] - value_yesterday['sick']
        died = value['died']
        died_today = value['died'] - value_yesterday['died']
        pub_date = str(dateconv(date_to_parse))
        result = {
        "pub_date": pub_date,
        "region": reg_name,
        "sick": sick,
        "died": died,
        "sick_today": sick_today,
        "died_today": died_today
        }
        add_today(result)
        print(result)


def get_last_date():
    """Проверка последней даты обновления БД"""
    all_dates = []
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f'Bearer {TOKEN}'
    headers["Content-Type"] = "application/json"
    data = requests.get(URL, headers=headers).json()
    for k in data:
        # print(type(k['pub_date']))
        all_dates.append(k['pub_date'])
    last_date = max(all_dates)
    return strtodate(last_date)


def add_today(stat_for_date):
    """Добавление данных в БД"""
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f'Bearer {TOKEN}'
    headers["Content-Type"] = "application/json"
    resp = requests.post(URL, headers=headers, data=json.dumps(stat_for_date))
    print(resp.status_code)


if __name__ == '__main__':
    print(check_update())
    parse_date("15.08.2022")





