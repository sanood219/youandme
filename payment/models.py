from django.db import models
from user.models import User

# Create your models here.


class Payments(models.Model):
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(default='899',max_length=200)
    order_id = models.CharField(max_length=500,blank=True)
    razorpay_payment_id = models.CharField(max_length=500, blank=True)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
 

def __str__(self):
    return self.amount


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    is_subscribed = models.BooleanField(default=False)