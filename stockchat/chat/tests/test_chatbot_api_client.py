import random
from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from ..stock_api_client import StockApiClient, ApiResponseModel


class TestStockApiClient(TestCase):
    @skip("This integration test, requires app to be up. Run when needed")
    def test_integration_with_api_for_known_value(self):
        company_name = "aapl.us"
        api_response = StockApiClient.get_stock_value_for_company(company_name)

        self.assertIsInstance(api_response, ApiResponseModel)
        self.assertEqual(company_name, api_response.name)
        self.assertGreater(api_response.value, 0)

    @patch('chat.stock_api_client.requests.get')
    def test_should_parse_and_return_stock_value_when_it_is_returned(self, mock_get):
        random_value = random.randint(1, 500)
        mock_get.return_value.content = '{"name": "aapl.us", "value": %s}' % str(random_value)

        company_name = "aapl.us"
        api_response = StockApiClient.get_stock_value_for_company(company_name)
        self.assertEqual(company_name, api_response.name)
        self.assertEqual(random_value, api_response.value)
