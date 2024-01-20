import uuid
from django.db import models

# Create your models here.
class CreateChat(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable= False
    )
    chat_member_1 = models.CharField(max_length=100)
    chat_member_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.chat_member_1
