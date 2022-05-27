from django.shortcuts import render
import requests
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from .models import Item
from .serializers import ItemSerializer
from tablib import Dataset

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

def simple_upload(request):
    if request.method == 'POST':
        item_resource = ItemResource()
        dataset = Dataset()
        new_items = request.FILES['myfile']

        imported_data = dataset.load(new_items.read())
        result = item_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            item_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import.html')