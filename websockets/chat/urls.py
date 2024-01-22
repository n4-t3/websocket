from django.urls import path
from .views import ChatView

urlpatterns = [
    path("<uuid:id>/<slug:user>", ChatView.as_view(),name="ChatView")
]
