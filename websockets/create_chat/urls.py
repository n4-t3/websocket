from django.urls import path
from .views import CreateChat

urlpatterns = [
    path("", CreateChat.as_view())
]
