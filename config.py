import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    OZON_CLIENT_ID = os.getenv('OZON_CLIENT_ID')
    OZON_API_KEY = os.getenv('OZON_API_KEY')
    WB_API_KEY = os.getenv('WB_API_KEY')
    MS_EMPLOYEE_ID = os.getenv('MS_EMPLOYEE_ID')
    MS_ORGANIZATION_ID = os.getenv('MS_ORGANIZATION_ID')
    MS_WB_CONTRACT_ID = os.getenv('MS_WB_CONTRACT_ID')
    MS_WB_COUNTERPARTY_ID = os.getenv('MS_WB_COUNTERPARTY_ID')
    MS_OZON_CONTRACT_ID = os.getenv('MS_OZON_CONTRACT_ID')
    MS_OZON_COUNTERPARTY_ID = os.getenv('MS_OZON_COUNTERPARTY_ID')