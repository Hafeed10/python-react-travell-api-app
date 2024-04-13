# api/v1/reply_comments/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.models import Comment
from .serializers import CommentSerializer








@api_view(['GET', 'POST'])
def comments(request, pk):
    if request.method == 'GET':
        
        comments = Comment.objects.filter(place=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
       
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)








