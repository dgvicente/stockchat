import requests
import csv

ELEMENT_ROW = 1
ELEMENT_INDEX = 3
API_URL = 'https://stooq.com/q/l/?s=%s&f=sd2t2ohlcv&h&e=csv'


class StockApiClient:

    @staticmethod
    def get_for_company(company):
        url = API_URL % company
        response = requests.get(url)
        return StockApiClient.__process_response(company, response)

    @staticmethod
    def __process_response(company, response):
        decoded_content = response.content.decode('utf-8')

        csv_reader_as_list = list(csv.reader(decoded_content.splitlines(), delimiter=','))

        stock_value = csv_reader_as_list[ELEMENT_ROW][ELEMENT_INDEX]
        return ApiResponseModel(company, float(stock_value)) if stock_value != "N/D" else ApiResponseModel(company, None)


class ApiResponseModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value



