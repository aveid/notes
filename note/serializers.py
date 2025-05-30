from rest_framework import serializers

from comment.serializers import CommentSerializer
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.comments.exists():
            comment_data = CommentSerializer(instance.comments.all(), many=True).data
            representation['comments'] = comment_data
        else:
            representation['comments'] = []
        return representation
