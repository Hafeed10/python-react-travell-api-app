from django.urls import path
from . import views

urlpatterns = [
    path('reply_comment/<int:pk>', views.reply_comment, name='reply_comment'),
]
