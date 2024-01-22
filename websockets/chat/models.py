from django.db import models
# Create your models here.

class Chat(models.Model):
    chatroom = models.ForeignKey("create_chat.CreateChat",on_delete = models.CASCADE)
    user = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text
