from django.http import HttpResponse
from django.shortcuts import render
from .models import Small,Large,Topping,Subs_small,Subs_large,Pasta,Salads,Dinner

# Create your views here.
def index(request):
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

def checkout(request,food,pizza_id):
    context={
        "small": Small.objects.all(),
        "large": Large.objects.all(),
        "topping": Topping.objects.all(),
        "subs_s": Subs_small.objects.all(),
        "subs_l": Subs_large.objects.all(),
        "pasta" : Pasta.objects.all(),
        "salads" : Salads.objects.all(),
        "dinner" : Dinner.objects.all(),
        "id": pizza_id

    }
    return render(request,"orders/checkout.html",context)
