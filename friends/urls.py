from django.urls import path
from . import views
urlpatterns = [
    # path('', views.messages_page,name='message_page'),
    path('friend_request/<int:id>',views.friend_request,name='friend_request'),
    path('cancel_request/<int:id>',views.cancel_request,name='cancel_request'),
    path('view_request/',views.view_request,name='view_request'),
    path('accept_request/<int:id>',views.accept_request,name='accept_request'),
    path('friend_remove/<int:id>',views.friend_remove,name='friend_remove'),
]
