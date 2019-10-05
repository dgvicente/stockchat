import requests
import json

API_URL = 'http://localhost:8000/chatbot/%s/'


class ApiResponseModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ChatbotApiClient:

    @staticmethod
    def get_stock_value_for_company(company):
        url = API_URL % company
        response = requests.get(url)
        return ChatbotApiClient.__process_response(response)

    @staticmethod
    def __process_response(response):
        stock_info_as_dict = json.loads(response.content)
        return ApiResponseModel(stock_info_as_dict['name'], stock_info_as_dict['value'])
