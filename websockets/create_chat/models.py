import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class CreateChat(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable= False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    chat_member_1 = models.CharField(max_length=100)
    chat_member_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    def is_valid(self):
        return timezone.now() - self.created_at < timezone.timedelta(hours=24)
