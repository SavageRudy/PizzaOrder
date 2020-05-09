from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.Form,):
    pizza_id = forms.CharField(label='pizza_id', max_length=100)
    db_name = forms.CharField(label='db_name', max_length=100)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        permissions = (("not_admin"))
        model = User
        fields = ["username", "email", "password"] 

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user       