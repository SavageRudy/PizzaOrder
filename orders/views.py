from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Small,Large,Topping,Subs_small,Subs_large,Pasta,Salads,Dinner
from . import models
from .forms import OrderForm


# Create your views here.
@csrf_protect
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
        pizza_id = order.data['pizza_id']
        db_name = order.data['db_name']

        request.session['cart'].append({
            'pizza_id' : pizza_id,
            'db_name' : db_name
        })
        
        request.session.modified = True

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
        

def checkout(request):
    cart_items = request.session['cart']

    print(cart_items)
    context = {}
    context['cart_info'] = {}
    for x in cart_items:

        print(x)

        fn = getattr(models,x['db_name'])

        result =  fn.objects.all().filter(id = x['pizza_id']).values('price')

        print(result)

        context['cart_info'][x['pizza_id']] = result


    context['cart'] = cart_items

    print(context)
   
    return render(request,"orders/checkout.html",context)
