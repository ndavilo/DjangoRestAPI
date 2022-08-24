from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def currencyView(request):
    data = {
        'id': 12,
        'name': 'BTC',
        'value' :21532,
        'date': '2022/08/24'
    }
    return JsonResponse(data)