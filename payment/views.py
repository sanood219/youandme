import email
from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import razorpay
from payment.forms import PaymentForm
from payment.models import *
from user.models import User
from user.views import *
# Create your views here.



def payment(request):
    user_id = request.session['username']
    user = User.objects.get(email=user_id)
    if request.method == 'POST':
        sender = user
        name = user.user_info.full_name
        amount = int(899)*100

        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_JNm726wMkXt53A', 'z2uEcGcD2EzViveS9yCxL9AQ'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            print('hey')
            payment = Payments(
                name=name,
                amount=amount,
                order_id=order_id,
                sender = sender,

            )
            payment.save()
            response_payment['name'] = name

            form = Payments.objects.filter(order_id=order_id)
            context = {
                'form':form,
                'payment': response_payment
            }
            return render(request, 'checkout.html',context)
    return render(request, 'checkout.html')


@csrf_exempt
def paymentStatus(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_JNm726wMkXt53A', 'z2uEcGcD2EzViveS9yCxL9AQ'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        payment = Payments.objects.get(order_id=response['razorpay_order_id'])
        payment.razorpay_payment_id = response['razorpay_payment_id']
        payment.paid = True
        payment.save()
        return redirect(do_sub)
    except:
        return redirect(do_sub)   


def subscription(request,id):
    user_id = request.session['username']
    user = User.objects.get(email=user_id)
    if Payments.objects.filter(sender=id):
        return render(request,'already_sub.html')
    else:
        return render(request,'subscription.html')


def do_sub(request):
    user_id = request.session['username']
    user = User.objects.get(email=user_id)
    print(user)
    do_sub = Subscription.objects.get(user=user)
    if do_sub.is_subscribed:
        return redirect(home)
    else:
        do_sub.is_subscribed = True
        do_sub.save()
        return redirect(home)