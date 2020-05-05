from django.contrib import admin

# Register your models here.
from .models import Small,Large,Topping,Subs_small,Subs_large,Pasta,Dinner,Salads

admin.site.register(Small)
admin.site.register(Large)
admin.site.register(Topping)
admin.site.register(Subs_small)
admin.site.register(Subs_large)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner)