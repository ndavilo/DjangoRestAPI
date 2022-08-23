from django.urls import path
from .views import currencyView

urlpatterns = [
    path('', currencyView)
]