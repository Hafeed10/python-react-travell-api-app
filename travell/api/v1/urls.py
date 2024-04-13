from django.urls import path, include

urlpatterns = [
    path('comments/', include('api.v1.comment.urls')),
    path('reply_comments/', include('api.v1.reply_comment.urls')),
]
