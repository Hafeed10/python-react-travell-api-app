from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views



urlpatterns = [
   
    path('admin/', admin.site.urls),
     path('api/v1/auth/', include("api.v1.auth.urls")),
     path('api/v1/places/', include("api.v1.places.urls")),
     path('api/v1/comment/', include("api.v1.comment.urls")),
     path('api/v1/likes/', include('api.v1.likes.urls')),
     path('api/v1/reply_comments/', include('api.v1.reply_comment.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

