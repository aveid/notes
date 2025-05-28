from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Note(CommonInfo):
    title = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
