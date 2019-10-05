import json

from django.http import HttpResponse

from .api_client import StockApiClient


def get_value_for(request, company):
    response = StockApiClient.get_for_company(company)
    return HttpResponse(json.dumps(response.__dict__), content_type="application/json")

