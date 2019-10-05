import random
from unittest import TestCase
from unittest.mock import patch, MagicMock

from ..api_client import StockApiClient, ApiResponseModel


class TestStockApiClient(TestCase):

    def test_integration_with_api_for_known_value(self):
        company_name = "aapl.us"
        api_response = StockApiClient.get_for_company(company_name)
        self.assertIsInstance(api_response, ApiResponseModel)
        self.assertEqual(company_name, api_response.name)
        self.assertGreater(api_response.value, 0)

    @patch('chatbot.api_client.requests.get')
    def test_should_parse_and_return_stock_value_when_it_is_returned(self, mock_get):
        random_value = random.randint(1, 500)
        response_content = MagicMock()
        response_content.decode.return_value = \
            "Symbol,Date,Time,Open,High,Low,Close,Volume" \
            "\r\nAAPL.US,2019-10-04,22:00:02,%s,227.49,223.89,227.01,34755553" % str(random_value)

        mock_get.return_value.content = response_content

        company_name = "DoesNotMatter"
        api_response = StockApiClient.get_for_company(company_name)
        self.assertEqual(company_name, api_response.name)
        self.assertEqual(random_value, api_response.value)

    @patch('chatbot.api_client.requests.get')
    def test_should_return_none_when_no_value_is_returned_from_the_api(self, mock_get):
        response_content = MagicMock()
        response_content.decode.return_value = \
            "Symbol,Date,Time,Open,High,Low,Close,Volume" \
            "\r\nPEPE,N/D,N/D,N/D,N/D,N/D,N/D,N/D"

        mock_get.return_value.content = response_content

        company_name = "Pepe"
        api_response = StockApiClient.get_for_company(company_name)

        self.assertEqual(company_name, api_response.name)
        self.assertIsNone(api_response.value)
