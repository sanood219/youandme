from operator import truediv
from tkinter.tix import Tree
from django.db import models
from user.models import *

# Create your models here.
class Friend_list(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friend')
    is_friends = models.BooleanField(default=True,blank=True,null=False)

class Friend_request(models.Model):
    sent_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_by')
    send_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='send_to')
    is_active = models.BooleanField(default=True,blank=True,null=False)