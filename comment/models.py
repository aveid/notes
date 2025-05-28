from django.contrib.auth import get_user_model
from django.db import models
from note.models import CommonInfo, Note

User = get_user_model()


class Comment(CommonInfo):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


