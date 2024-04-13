


from django.urls import path
from api.v1.likes import views

urlpatterns = [
   
    path('likes/<int:pk>', views.Likes),
]
