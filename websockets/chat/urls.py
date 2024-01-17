from django.urls import path
from .views import ChatView

urlpatterns = [
    path("<int:id>/", ChatView.as_view())
]