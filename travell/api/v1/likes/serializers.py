from rest_framework.serializers import ModelSerializer
from likes.models import Likes

class LikesSerializer(ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'content', 'likes']
