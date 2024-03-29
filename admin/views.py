import django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from friends.models import Friend_list
from user.models import User
from django.views.decorators.cache import never_cache
from payment.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@never_cache
@csrf_exempt
def admin_login(request):
    if 'admin' in request.session:
        return redirect('admin_home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_superuser:
                request.session['admin'] = email
                return redirect(admin_home)
            else:
                messages.error(
                    request, 'You dont have permission to this page')
                return redirect(admin_login)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect(admin_login)
    return render(request, 'admin_login.html')


@never_cache
def admin_home(request):
    if 'admin' in request.session:
        payment = Payments.objects.all()
        payment_count = Payments.objects.filter(amount=89900).count()
        print(payment_count)
        total_amount = int(899*payment_count)
        print(total_amount)
        user = User.objects.all().count()
        context = {'user': user, 'payment': payment, 'total_amount': total_amount}
        print(user)
        return render(request, 'admin_home.html', context)
    else:
        return redirect(admin_login)
    


def user_manage(request):
    if 'admin' in request.session:
        user = User.objects.all()
        context = {'user': user}
        return render(request, 'user_manage.html', context)
    else:
        return redirect(admin_login)
    


def admin_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(admin_login)


def user_block(request, id):
    if 'admin' in request.session:
        user = User.objects.get(id=id)
        if user.is_active:
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()
        return redirect(user_manage)


def view_user(request, id):
    if 'admin' in request.session:
        user = User.objects.filter(id=id)
        context = {'user': user}
        return render(request, 'view_user.html', context)


def user_connection(request):
    if 'admin' in request.session:
        friend_list = Friend_list.objects.all()
        context = {
            'friend_list': friend_list
        }
        return render(request, 'user_connections.html', context)
