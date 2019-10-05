import re
from .chatbot_api_client import ChatbotApiClient
from .definitions import BOT_NAME, MESSAGE_REGEX
from .models import ChatMessage


class ReplyService:

    @staticmethod
    def get_reply_for(message):
        matches = re.match(MESSAGE_REGEX, message.message)
        if matches:
            company = matches.group('search')
            value_for_company = ChatbotApiClient.get_stock_value_for_company(company)
            return ChatMessage(BOT_NAME, ReplyService.__build_message_for(value_for_company))
        else:
            return None

    @staticmethod
    def __build_message_for(api_reply):
        return "%s quote is $%s per share." % (api_reply.name.upper(), str(api_reply.value)) \
            if api_reply.value else "We have no quote for %s" % api_reply.name.upper()
