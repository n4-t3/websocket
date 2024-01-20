from django import forms
from .models import CreateChat

class CreateChatForm(forms.ModelForm):
    class Meta:
        model = CreateChat
        fields = ('chat_member_1',)
