from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('verify/<str:token>',views.verify,name='verify'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('user_view/<int:id>',views.view,name='view'),
    path('user_view/gallery<int:id>',views.gallery,name='gallery'),
    path('user_edit/<int:id>',views.user_edit,name='user_edit'),
    path('log_user/<int:id>',views.log_user,name='log_user'),
    # path('send_request/<int:id>',views.send_request,name='send_request'),
    # path('accept_req/<int:id>',views.accept_request,name='accept_req')
]