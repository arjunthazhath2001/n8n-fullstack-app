from django.urls import path, include
from .views import SendRequest

urlpatterns = [
    path('', SendRequest.as_view(),name="send-request"),
]
