import requests

class WildberriesAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_report(self, start_date, end_date):
        endpoint = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod'
        params = {"key": self.api_key, "dateFrom": start_date, "dateTo": end_date}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)