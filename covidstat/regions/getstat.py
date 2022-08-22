import requests
from requests.structures import CaseInsensitiveDict
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('AUTH_TOKEN')
TODAY_DATE = datetime.date.today()
TODAY_DATE_DOT = TODAY_DATE.strftime("%d.%m.%Y")
URL = "http://127.0.0.1:8000/region/"

class get_statistic():
    """Получение данных"""
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f'Bearer {TOKEN}'
    headers["Content-Type"] = "application/json"
    data = requests.get(URL, headers=headers).json()


    def sick(self, date, region):
        data = self.data
        for k in data:
            if (k['pub_date'] == date) and (k['region'] == region):
                print(f"{k['region']} {k['sick_today']}")

    def died(self, date, region):
        data = self.data
        for k in data:
            if (k['pub_date'] == date) and (k['region'] == region):
                print(f"{k['region']} {k['died_today']}")


if __name__ == '__main__':

    get_statistic.sick(get_statistic, str(TODAY_DATE), 'novosib')



