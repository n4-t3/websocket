from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CreateChatForm
# Create your views here.
class CreateChat(TemplateView):
    template_name = "create_chat.html"
    form_class = CreateChatForm
    def post(self, request):
        print(request.data)
