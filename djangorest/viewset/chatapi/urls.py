from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageView, UserView

router = DefaultRouter()
router.register('message', MessageView)
router2 = DefaultRouter()
router2.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
]