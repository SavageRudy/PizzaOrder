from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Small,Large,Topping,Subs_small,Subs_large,Pasta,Salads,Dinner
from . import models
from .forms import OrderForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


orders=[]
customer=[]
# Create your views here.
@csrf_protect
@login_required(login_url='/login')
def index(request):

    if request.method == 'GET':

        context={
            "small": Small.objects.all(),
            "large": Large.objects.all(),
            "topping": Topping.objects.all(),
            "subs_s": Subs_small.objects.all(),
            "subs_l": Subs_large.objects.all(),
            "pasta" : Pasta.objects.all(),
            "salads" : Salads.objects.all(),
            "dinner" : Dinner.objects.all()

        }
        return render(request,"orders/menu.html",context)

    elif request.method == 'POST':
        
        order = OrderForm(request.POST)
        data = request.POST.copy()
        if order.is_valid:            
            pizza_id = data.get('pizza_id')
            db_name = data.get('db_name')
            try:
                request.session['cart'].append({
                    'pizza_id' : pizza_id,
                    'db_name' : db_name
                })
            except:
                request.session['cart']=[{
                                        'pizza_id' : pizza_id,
                                        'db_name' : db_name }]

            request.session.modified = True    
        else:
            return HttpResponse("Form error")
    
        context={
            "small": Small.objects.all(),
            "large": Large.objects.all(),
            "topping": Topping.objects.all(),
            "subs_s": Subs_small.objects.all(),
            "subs_l": Subs_large.objects.all(),
            "pasta" : Pasta.objects.all(),
            "salads" : Salads.objects.all(),
            "dinner" : Dinner.objects.all()

        }
        return render(request,"orders/menu.html",context)
        

def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.is_authenticated
        customer.append(username)
        
@login_required(login_url='/login')
def checkout(request):
    try:
        cart_items = request.session['cart']
    except:
        cart_items = {}
    
    total=0
    
    context = {}
    context['cart_info'] = []
    for index, item in enumerate(cart_items):


        fn = getattr(models,item['db_name'])

        result =  fn.objects.all().filter(id = item['pizza_id']).values()[0]

        orders.append(result)
        cart_items[index]['price'] = result['price']
        cart_items[index]['name'] = result['name']
        try:
            cart_items[index]['topping'] = result['topping'] 
        except:
            cart_items[index]['topping'] = "no toppings"
        total += result['price']   
    
    print(total)
    cart_total = total

    
    
    context={
        'cart' : cart_items,
        'total' : cart_total
    }
   
    return render(request,"orders/checkout.html",context)

@login_required(login_url='/login')
@permission_required('admins_only', raise_exception=True)
def order(request):
    context= {
        'order': orders,
        'customer' : customer
    }
    return render(request,"orders/order.html",context)

@login_required(login_url='/login')
def success(request):
    recipient_list = []
    subject = 'Confirmation'
    message = ' Your order has been placed'
    email_from = settings.EMAIL_HOST_USER


    
    recipient_list.append(request.user.email)
    
    send_mail( subject = subject, message = message, from_email= email_from,recipient_list= recipient_list, fail_silently=False)
    context = {
       'msg' : 'Email has been sent'
    }
    return render(request,"orders/success.html",context)    
    

def register(response):
    if response.method == "GET":
        form = RegisterForm()
        return render(response,"orders/register.html",context={"form":form})

    elif response.method == "POST":
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = RegisterForm()
            return render(response, "orders/register.html", {"form":form})    

def login_request(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request = request,
                    template_name = "orders/login.html",
                    context={"form":form})

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('/login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login') 

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")                           