from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.models import ReplyComment, Comment
from .serializers import Reply_CommentSerializer

@api_view(['GET', 'POST'])
def reply_comment(request, pk):
    if request.method == 'GET':
        reply_comments = ReplyComment.objects.all()
        serializer = Reply_CommentSerializer(reply_comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Reply_CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
