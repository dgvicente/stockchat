from unittest import TestCase
from unittest.mock import patch

from ..models import ChatMessage
from ..chatbot_api_client import ApiResponseModel
from ..service import ReplyService


class TestReplyService(TestCase):

    @patch('chat.chatbot_api_client.ChatbotApiClient.get_stock_value_for_company')
    def test_should_invoke_api_when_given_message_matches_defined_regex(self, mock_get_value):
        mock_get_value.return_value = ApiResponseModel("aapl", 234)
        message = ChatMessage("user", "/stock=aapl.us")
        reply = ReplyService.get_reply_for(message)

        self.assertIsNotNone(reply)
        self.assertEqual("botty", reply.user)
        self.assertEqual("AAPL quote is $234 per share.", reply.message)

    def test_should_not_invoke_api_when_given_message_does_not_match_defined_regex(self):
        message = ChatMessage("user", "random message with no meaning")
        reply = ReplyService.get_reply_for(message)
        self.assertIsNone(reply)
