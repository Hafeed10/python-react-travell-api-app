from django.urls import path
from api.v1.comment import views

urlpatterns = [
    path('comments/<int:pk>', views.comments),
    
]
