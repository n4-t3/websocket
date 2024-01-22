from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import CreateChat

# Create your views here.
class CreateChatView(View):
    template_name = 'create_chat.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        chat_code = request.POST.get('chat_code')
        user_name = request.POST.get('user_name')

        if not chat_code:
            chatroom = CreateChat.objects.create(chat_member_1 = user_name)
        else:
            try:
                chatroom = CreateChat.objects.get(id = chat_code)
            except CreateChat.DoesNotExist:
                chatroom = CreateChat.objects.create(chat_member_1 = user_name)
            else:
                if not chatroom.is_valid():
                    return HttpResponse('Chatroom Expired')
                existing_user = chatroom.chat_member_1 == user_name or chatroom.chat_member_2 == user_name
                if existing_user:
                    return redirect('ChatView', id = chatroom.id, user = user_name)
                if chatroom.chat_member_1 and chatroom.chat_member_2:
                    return HttpResponse("Chatroom is full")
                else:
                    chatroom.chat_member_2 = user_name
                    chatroom.save()
        return redirect(f'chat/{chatroom.id}/{user_name}', id = chatroom.id, user = user_name)
                
