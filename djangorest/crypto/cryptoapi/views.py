from django.shortcuts import render
from django.http import JsonResponse
from .models import Cryptocoin

# Create your views here.
def currencyView(request):
    data = Cryptocoin.objects.all()
    response = {'coins':list(data.values('name', 'value', 'date'))}
    return JsonResponse(response)