import requests
from datetime import datetime, timedelta

class OzonAPI:
    def __init__(self, client_id, api_key):
        self.client_id = client_id
        self.api_key = api_key

    def get_report(self):
        last_month = datetime.now() - timedelta(days=30)
        date = last_month.strftime("%Y-%m")

        endpoint = 'https://api-seller.ozon.ru/v1/finance/realization'
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key
            }
        data = {
            "date": date
            }
        response = requests.post(endpoint, headers=headers, json=data)

        if response.status_code == 200:
            return response

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)