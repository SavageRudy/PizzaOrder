from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout/<food>/<int:pizza_id>", views.checkout)
    
]
