from django.urls import path
from .views import CreateChatView

urlpatterns = [
    path("", CreateChatView.as_view(), name="CreateChaView")
]
