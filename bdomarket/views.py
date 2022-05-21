from django.shortcuts import render
import requests
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

def date_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def item_test_view(request):
    url = "https://na-trade.console.playblackdesert.com/Trademarket/GetWorldMarketSearchList"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "searchResult": "5419,5418"
    }
    result = requests.request('POST', url, json=payload, headers=headers)
    if result.status_code == 200:
        return HttpResponse("<html><body>%s</body></html>" % result.text)
        # return HttpResponse('Successful')
    return HttpResponse('Something Went Wrong')