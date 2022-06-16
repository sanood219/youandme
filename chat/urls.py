from django.urls import path
from requests import request
from . import views
urlpatterns = [
    path('', views.messages_page,name='message_page'),
    path('chat_id/<int:id>',views.chat_id,name='chat_id')
]
