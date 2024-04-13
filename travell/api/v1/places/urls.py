from django.urls import path ,include
from api.v1.places import views

urlpatterns = [
    path('', views.places),
    path('view/<int:pk>', views.place),
    path('proteced/<int:pk>', views.proteced),
    path('likes/', include("api.v1.likes.urls")),  # Adjust the import path accordingly
]
