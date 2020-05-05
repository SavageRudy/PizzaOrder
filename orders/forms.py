from django import forms

class OrderForm(forms.Form):
    pizza_id = forms.CharField(label='pizza_id', max_length=100)
    db_name = forms.CharField(label='db_name', max_length=100)