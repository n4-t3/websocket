from django.shortcuts import render, redirect
from django.views import View
from create_chat.models import CreateChat
from .models import Chat
# Create your views here.

class ChatView(View):
    template_name = 'chat.html'

    def get(self, request, *args, **kwargs):
        context = {}
        chatroom_id = self.kwargs['id']
        user = self.kwargs['user']
        chatroom = CreateChat.objects.get(id = chatroom_id)
        if chatroom.chat_member_1 == user or chatroom.chat_member_2==user:
            chat_logs = Chat.objects.filter(chatroom=chatroom).order_by('time')
            context['chat_logs'] = [{'user': 'sent' if chat.user==user else 'received', 'text': chat.text} for chat in chat_logs]
            return render(request, self.template_name, context=context)
        return render(request, 'error', {'error_message': 'You are not a member of this chatroom.'})
    
    def post (self,request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        user = kwargs.get('user')
        chatroom = CreateChat.objects.get(id=chatroom_id)
        if chatroom.chat_member_1 == user or chatroom.chat_member_2 == user:
            message = Chat(chatroom=chatroom, user=user, text=request.POST.get('message'))
            message.save()
            return redirect(request.get_full_path())
        return render(request, 'error', {'error_message': 'You are not a member of this chatroom.'})
