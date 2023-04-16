import requests
from config import Config


class MoySkladAPI:
    def __init__(self, api_key, employee_id, organization_id, contract_id, counterparty_id):
        self.api_key = api_key
        self.employee_id = employee_id
        self.organization_id = organization_id
        self.contract_id = contract_id
        self.counterparty_id = counterparty_id

    def create_report(self, products, start_date, end_date):
        start_date = Config.REPORT_START_DATE or '2023-02-01'
        end_date = Config.REPORT_END_DATE or '2023-04-15'

        positions = []
        for product_id in products:
            product_id = ''
            quantity = 0
            price = 0
            reward = 0
            position = {
                "assortment": {
                    "meta": {
                        "href": f"https://online.moysklad.ru/api/remap/1.2/entity/product/{product_id}",
                        "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/product/metadata",
                        "type": "product",
                        "mediaType": "application/json"
                    }
                },
                "quantity": quantity,
                "price": price,
                "vat": 0,
                "reward": reward
            }
            positions.append(position)

    def request(self, start_date, end_date, positions):
        url = "https://online.moysklad.ru/api/remap/1.2/entity/commissionreportin"

        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "owner": {
                "meta": {
                    "href": f"https://online.moysklad.ru/api/remap/1.2/entity/employee/{self.employee_id}",
                    "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/employee/metadata",
                    "type": "employee",
                    "mediaType": "application/json"
                }
            },
            "shared": False,
            "name": "10000",
            "moment": f"{end_date} 10:00:00",
            "applicable": False,
            "sum": 0,
            "contract": {
                "meta": {
                    "href": f"https://online.moysklad.ru/api/remap/1.2/entity/contract/{self.contract_id}",
                    "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/contract/metadata",
                    "type": "contract",
                    "mediaType": "application/json"
                }
            },
            "agent": {
                "meta": {
                    "href": f"https://online.moysklad.ru/api/remap/1.2/entity/counterparty/{self.counterparty_id}",
                    "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/counterparty/metadata",
                    "type": "counterparty",
                    "mediaType": "application/json"
                }
            },
            "organization": {
                "meta": {
                    "href": f"https://online.moysklad.ru/api/remap/1.2/entity/organization/{self.organization_id}",
                    "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/organization/metadata",
                    "type": "organization",
                    "mediaType": "application/json"
                }
            },
            "positions": positions,
            "vatEnabled": True,
            "vatIncluded": True,
            "commissionPeriodStart": f"{start_date} 10:00:00",
            "commissionPeriodEnd": f"{end_date} 10:00:00",
            "rewardType": "PercentOfSales"
        }
