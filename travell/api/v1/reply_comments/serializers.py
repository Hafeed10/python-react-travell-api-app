
from rest_framework import serializers
from comments.models import Comment


class Reply_CommentSerializer(serializers.ModelSerializer):  # Renamed to follow naming conventions
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'Reply_comment']