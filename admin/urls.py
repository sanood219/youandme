from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('admin-home/',views.admin_home,name='admin_home'),
    path('user_manage/',views.user_manage,name='user_manage'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('user_block/<int:id>',views.user_block,name='user_block'),
    path('user_manage/view_user<int:id>',views.view_user,name='user_manage/view_user'),
    path('user_connection/',views.user_connection,name='user_connection'),
]
