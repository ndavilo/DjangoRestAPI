from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatView, PersonView

router = DefaultRouter()
router.register('chat', ChatView)
router.register('person', PersonView)

urlpatterns = [
    path('', include(router.urls)),
]