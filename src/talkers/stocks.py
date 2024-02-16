import requests
from decouple import config

class Stocks:
    def __init__(self, ticker:str) -> None:
        self.ticker = ticker.upper()
    

    def get_prices(self):
        URL = f"http://{config('HOST')}:{config('PORT')}/yahoo/history_prices/{self.ticker}"
        response = requests.get(url=URL)

        if response.status_code == 200:
            return response.json()
        return None
    
    def get_dividends(self):
        URL = f"http://{config('HOST')}:{config('PORT')}/fundamentus/dividends/{self.ticker}"
        response = requests.get(url=URL)

        if response.status_code == 200:
            return response.json()
        return None

