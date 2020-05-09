from django.db import models

# Create your models here.
class Small(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)    
    topping = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return f" A Small {self.name} pizza  with {self.topping} topping =${self.price}"

class Large(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)    
    topping = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f" A Large {self.name} pizza  with {self.topping} topping"

class Topping(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Subs_small(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"    

class Subs_large(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Salads(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Dinner(models.Model):
    id= models.IntegerField(primary_key=700)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"



