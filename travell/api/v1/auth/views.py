# Import necessary modules and classes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# Define the view function
@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')
    name = request.query_params.get('name')

    print("Email:", email)
    print("Password:", password)
    print("Name:", name)

    if not User.objects.filter(username=email).exists():
        User.objects.create_user(
            username=email,
            password=password,
            first_name=name,
        )
        response_data = {
            "status": 6000,
            "data": "User created successfully",
        }
    else:
        response_data = {
            "status": 6001,
            "data": "This account is already in use"
        }

    return Response(response_data)
