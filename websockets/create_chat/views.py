from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CreateChat(TemplateView):
    template_name = "create_chat.html"
