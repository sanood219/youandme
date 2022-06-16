# from concurrent.futures import thread
from multiprocessing import context
from django.shortcuts import redirect, render
from user.models import User
from user.views import *
# Create your views here.
from chat.models import Thread, User


def messages_page(request):
    id = request.session['username']
    user = User.objects.get(email=id)
    print(user)
    threads = Thread.objects.by_user(user=user).prefetch_related(
        'chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads,
        'user': user
    }
    return render(request, 'messages.html', context)


def chat_id(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)
    print(user1.id)
    if Thread.objects.filter(first_person=user1.id,second_person=id).first():
        return redirect(messages_page)
    elif Thread.objects.filter(second_person=user1.id,first_person=id).first():
        return redirect(messages_page)
    else:
        user_1 = User.objects.get(email=email)
        user_2 = User.objects.get(id=id)
        thread = Thread.objects.create(
            first_person=user_1, second_person=user_2)
        return redirect(messages_page)
