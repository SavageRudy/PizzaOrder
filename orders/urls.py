from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout", views.checkout),
    path("order",views.order),
    path("success",views.success),
    path("register",views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
