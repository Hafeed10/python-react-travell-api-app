
from django.http import JsonResponse
from rest_framework.decorators import api_view
from likes.models import Likes
from api.v1.likes.serializers import LikesSerializer


@api_view(["GET"])
def likes_view(request, pk):
    try:
        like_instance = Likes.objects.filter(pk=pk).exists()
    except Likes.DoesNotExist:
        return JsonResponse({'error': 'Like does not exist'}, status=404)

    if request.method == 'GET':
        serializer = LikesSerializer(like_instance)
        return JsonResponse(serializer.data, status=200)
        
    # elif request.method == 'POST':
    #     serializer = LikesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
        
    # elif request.method == 'PATCH': 
    #     like_instance.likes += 1
    #     like_instance.save()
    #     serializer = LikesSerializer(like_instance)
    #     return JsonResponse(serializer.data, status=200)
