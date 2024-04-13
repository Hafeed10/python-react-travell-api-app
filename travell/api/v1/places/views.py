from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.v1.places.serializers import PlaceSerializer, PlaceDetailSerializer 
from places.models import Place
from django.http import JsonResponse
 


from rest_framework.permissions import IsAuthenticated 
from django.db.models import Q



@api_view(['GET'])
def places(request):
    instances = Place.objects.filter(is_deleted=False) 

    q = request.GET.get("q")
    if q:
        ids = q.split(", ")
        # instances = instances.filter(Q(name__icontains=q) | Q(place_icntains=q))
        #  instances = instances.filter(category__name__icontains=q)
        instances = instances.filter(category__in=ids)


    context = {
        "request": request
    }
    serializer = PlaceDetailSerializer(instances, many=True, context=context)  
    response_data = { 
        "status": 6000, 
        "message": "success",
        "data": serializer.data  
    }
    
    return Response(response_data)


@api_view(['GET'])

def place(request, pk):
    try:
        instance = Place.objects.get(pk=pk)
        serializer = PlaceSerializer(instance)
        response_data = {
            "status": 6000,
            "message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    except Place.DoesNotExist:
        response_data = {
            "status": 6001,
            "message": "place not found"
        }
        return Response(response_data, status=404)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def proteced(request, pk):
    try:
        instance = Place.objects.get(pk=pk)
        serializer = PlaceSerializer(instance)
        response_data = {
            "status": 6000,
            "message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    except Place.DoesNotExist:
        response_data = {
            "status": 6001,
            "message": "place not found"
        }
        return Response(response_data, status=404)
    






