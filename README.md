# DjangoRestAPI
Django Rest API samples
Cleate a Repo

Clone the repo to your harddrive:
  a) Open a VS code,
  b) Go to clone git Repository,
  c) Copy the Repo adress and paste on VS code,
  d) Select the location on your harddrive and open on VS code.

Create a Python 3 Virtual environment:
  a)  python3 -m venv restenv
  b)  source restenv/bin/activate

pip install the following librarys into to Virtual env
    Django
    djangorestframework

mkdir djangorest
cd djangorest
django-admin startproject crypto
cd crypto
python manage.py startapp crptoapi 

open settings.py and add:
    'rest_framework', and
    'cryptoapi',
     inside INSTALLED_APPS

Open the view on cryptoapi and add the folllowing examples:

from django.shortcuts import render
import datetime
from django.http import JsonResponse # this will help us serialize our data

# Create your views here.
def currencyView(request):
    data = {
        'id': 12,
        'name': 'BTC'
        'value': 21532
        'date': '2022/08/24'
    }
    return JsonResponse(data)

Open views.py in crypto and add:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crypto/', include('cryptoapi.urls'))
]

create urls.py inside cryptoapi, open it and add the following codes:

from django.urls import path
from .views import currencyView

urlpatterns = [
    path('', currencyView)
]

python3 manage.py runserver