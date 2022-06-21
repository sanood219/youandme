from django.urls import path
from . import views

urlpatterns = [
    path('subscription/<int:id>',views.subscription,name='subscription'),
    path('payment-status/',views.paymentStatus,name='payment-status'),
    path('checkout/',views.payment,name='checkout'),
    path('do_sub/',views.do_sub,name='do_sub')
]