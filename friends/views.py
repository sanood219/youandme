import profile
from django.shortcuts import redirect, render
from friends.models import Friend_list, Friend_request
from user.views import *
from user.models import User

# Create your views here.


def friend_request(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)
    if Friend_request.objects.filter(sent_by=user1, send_to=id).first():
        return redirect(view, id)
    else:
        sent_by = user1
        send_to = User.objects.get(id=id)
        print(send_to.id)
        friend_request = Friend_request.objects.create(
            sent_by=sent_by, send_to=send_to)
        return redirect(view, id)


def cancel_request(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)
    user2 = User.objects.get(id=id)
    if Friend_request.objects.filter(sent_by=user1, send_to=id).first():
        friend_request = Friend_request.objects.get(
            sent_by=user1, send_to=user2)
        friend_request.delete()
        return redirect(view, id)
    elif Friend_request.objects.filter(sent_by=user2, send_to=user1).first():
        friend_request = Friend_request.objects.get(
            sent_by=user2, send_to=user1)
        friend_request.delete()
        return redirect(view, id)

    return redirect(view, id)


def view_request(request):
    email = request.session['username']
    user = User.objects.get(email=email)
    friend_request = Friend_request.objects.filter(send_to=user)
    if Friend_list.objects.filter(user=user).first():
        friend_list = Friend_list.objects.filter(user=user)
        context = {
            'friend_request': friend_request,
            'user': user,
            'friend_list': friend_list

        }
        return render(request, 'friends.html', context)
    elif Friend_list.objects.filter(friend=user).first():
        print('hey')
        friend_list = Friend_list.objects.filter(friend=user)
        context = {
            'friend_request': friend_request,
            'user': user,
            'friend_list': friend_list

        }
        return render(request, 'friends.html', context)
    friend_list = Friend_list.objects.filter(friend=user)
    context = {
        'friend_request': friend_request,
        'user': user,
        'friend_list': friend_list
    }
    return render(request, 'friends.html', context)


def accept_request(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)

    if Friend_list.objects.filter(user=user1, friend=id).first():
        return redirect(view_request)
    else:
        user2 = User.objects.get(id=id)
        accept_request = Friend_list.objects.create(user=user1, friend=user2)
        friend_request = Friend_request.objects.get(
            sent_by=user2, send_to=user1)
        friend_request.delete()
        return redirect(view_request)


def friend_remove(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)
    user2 = User.objects.get(id=id)
    if Friend_list.objects.filter(user=user1, friend=user2).first():
        friend_remove = Friend_list.objects.get(user=user1, friend=user2)
        friend_remove.delete()
        return redirect(view_request)
    elif Friend_list.objects.filter(user=user2, friend=user1).first():
        print('hey')
        friend_remove = Friend_list.objects.get(user=user2, friend=user1)
        friend_remove.delete()
        return redirect(view_request)
