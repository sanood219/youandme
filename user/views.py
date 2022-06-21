from friends.models import *
from payment.models import Subscription
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.sites.shortcuts import get_current_site
import random
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@never_cache
@csrf_exempt
def signup(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).first():
            messages.success(request, 'user already exist please login!')
            return redirect(signup)
        request.session['email'] = email
        request.session['password'] = password1
        messages.success(request, 'Your account has been successfully created')
        return redirect(register)
    return render(request, 'signup.html')

@never_cache
@csrf_exempt
def register(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        phone = request.POST['phone']
        mother_name = request.POST['mother_name']
        father_name = request.POST['father_name']
        address = request.POST['address']
        gender = request.POST['gender']
        religion = request.POST['religion']
        city = request.POST['city']
        date_of_birth = request.POST['date_of_birth:day']
        date_of_birth += '-'
        date_of_birth += request.POST['date_of_birth:mon']
        date_of_birth += '-'
        date_of_birth += request.POST['date_of_birth:year']
        job = request.POST['job']
        qualification = request.POST['qualification']
        marital_status = request.POST['Marital_status']
        height = request.POST['height']
        weight = request.POST['weight']
        body_type = request.POST['Body_type']
        physical_status = request.POST['Physical_status']
        food = request.POST['Food']
        smoking = request.POST['Smoking']
        drinking = request.POST['drinking']
        profile = request.FILES.get('profile')
        email = request.session['email']
        password = request.session['password']

        print(email, password)
        print('image :', profile)
        user_info = User_info.objects.create(full_name=full_name, phone=phone, mother_name=mother_name, father_name=father_name, address=address, gender=gender, religion=religion,
                                             city=city, date_of_birth=date_of_birth, job=job, qualification=qualification, marital_status=marital_status, height=height,
                                             weight=weight, body_type=body_type, profile=profile, physical_status=physical_status, food=food, smoking=smoking, drinking=drinking)
        user = User.objects.create_user(
            email=email, password=password, gender=gender)
        user.user_info = user_info
        domain_name = get_current_site(request).domain
        token = str(random.random()).split('.')[1]
        user.token = token
        link = f'http://{domain_name}/verify/{token}'

        send_mail(
            'Verify your email',
            f'Please Click {link} to verify your account',
            settings.EMAIL_HOST_USER,
            [email],
        )
        user.save()
        sub = Subscription.objects.create(user=user)
        return redirect(home)
    return render(request, 'register.html')


def verify(request, token):
    try:
        user = User.objects.get(token=token)
        user.is_verified = True
        user.save()
        messages.success(request, 'Your account has been verified')
        return redirect(login)
    except Exception as e:
        messages.error(request, 'somthing went wrong')
        return redirect(login)

@never_cache
@csrf_exempt
def login(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active == True:
                if user.is_verified:
                    request.session['username'] = email
                    user = User.objects.get(email=email)
                    request.session['gender'] = user.user_info.gender
                    return redirect(home)
                else:
                    messages.error(
                        request, 'Your account is not verified check your email')
                    return redirect(login)
            else:
                messages.error(request, 'Your account has been suspended')
                return redirect(login)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect(login)
    return render(request, 'login.html')


def home(request):
    if 'username' in request.session:
        id = request.session['username']
        print(id)
        id_gender = request.session['gender']
        print(id_gender)
        log_user = User.objects.filter(email=id)
        if id_gender == 'Male':
            user = User.objects.filter(gender='Female')
            context = {'log_user': log_user, 'user': user}
            return render(request, 'home.html', context)
        elif id_gender == 'Female':
            user = User.objects.filter(gender='Male')
            context = {'log_user': log_user, 'user': user}
            return render(request, 'home.html', context)

    return redirect(login)


def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(login)


def view(request, id):
    user = User.objects.filter(id=id)
    print(user)
    email = request.session['username']
    user1 = User.objects.get(email=email)
    sub = Subscription.objects.get(user=user1)
    if sub.is_subscribed:

        if Friend_list.objects.filter(user=user1, friend=id).first():
            friend_list = Friend_list.objects.get(user=user1, friend=id)
            print(friend_list.is_friends)
            context = {
                'user': user,
                'friend_list': friend_list
            }
            if Profile_views.objects.filter(user=user1.id, visited_user=id).first():
                return render(request, 'view.html', context)
            else:
                views = Profile_views.objects.create(
                    user=user1.id, visited_user=id)
                return render(request, 'view.html', context)
        elif Friend_list.objects.filter(user=id, friend=user1).first():
            friend_list = Friend_list.objects.get(user=id, friend=user1)
            context = {
                'user': user,
                'friend_list': friend_list
            }
            if Profile_views.objects.filter(user=user1.id,visited_user=id).first():
                return render(request, 'views.html', context)
            else:
                views = Profile_views.objects.create(user=user, visited_user=id)
                return render(request, 'view.html', context)
        elif Friend_request.objects.filter(sent_by=user1, send_to=id).first():
            friend_request = Friend_request.objects.get(send_to=id, sent_by=user1)
            print(friend_request)
            context = {
                'user': user,
                'friend_request': friend_request
            }
            return render(request, 'view.html', context)
        else:
            context = {
                'user': user,
            }
            return render(request, 'view.html', context)
    else:
        return render(request,'not_sub.html',{'user':user1})


def gallery(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'gallery.html', context)


def log_user(request, id):
    email = request.session['username']
    user1 = User.objects.get(email=email)
    user = User.objects.filter(id=id)
    if Profile_views.objects.filter(visited_user=user1.id):
        views = Profile_views.objects.filter(visited_user=user1.id).count()
        context = {
            'user': user,
            'views':views
        }
        print(views)
        return render(request, 'log_user.html', context)
    context = {
            'user': user
        }
    return render(request, 'log_user.html', context)

@csrf_exempt
def user_edit(request, id):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        phone = request.POST['phone']
        mother_name = request.POST['mother_name']
        father_name = request.POST['father_name']
        address = request.POST['address']
        gender = request.POST['gender']
        religion = request.POST['religion']
        city = request.POST['city']
        date_of_birth = request.POST['date_of_birth:day']
        date_of_birth += '-'
        date_of_birth += request.POST['date_of_birth:mon']
        date_of_birth += '-'
        date_of_birth += request.POST['date_of_birth:year']
        job = request.POST['job']
        qualification = request.POST['qualification']
        marital_status = request.POST['Marital_status']
        height = request.POST['height']
        weight = request.POST['weight']
        body_type = request.POST['Body_type']
        physical_status = request.POST['Physical_status']
        food = request.POST['Food']
        smoking = request.POST['Smoking']
        drinking = request.POST['drinking']
        profile = request.FILES.get('profile')

        user1 = User_info(full_name=full_name, phone=phone, mother_name=mother_name, father_name=father_name, address=address, gender=gender, religion=religion,
                          city=city, date_of_birth=date_of_birth, job=job, qualification=qualification, marital_status=marital_status, height=height, weight=weight, body_type=body_type,
                          physical_status=physical_status, food=food, smoking=smoking, drinking=drinking, profile=profile)
        user1.save()
        return redirect(log_user, id)
    user = User.objects.filter(id=id)
    context = {
        'user': user
    }
    return render(request, 'user_edit.html', context)
