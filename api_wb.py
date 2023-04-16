import requests
from config import Config


class WildberriesAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_report(self, start_date, end_date):
        endpoint = 'https://statistics-api.wildberries.ru/api/v1/supplier/reportDetailByPeriod'

        HEADERS = {'Authorization': '{}'.format(Config.WB_API_KEY)}
        with requests.Session() as s:

            params = {"key": self.api_key,
                      "dateFrom": start_date, "dateTo": end_date,
                      "auth": Config.WB_API_KEY}
            s.headers.update(HEADERS)

            response = s.get(endpoint, params=params)
            if response.status_code == 200:
                return response.json()

            else:
                print("Error: Request returned status code",
                      response.status_code, "with message", response.reason)
