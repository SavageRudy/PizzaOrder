from django.db import models

# Create your models here.
class Small(models.Model):
    kind = models.CharField(max_length=40)    
    topping = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return f" A Small {self.kind} pizza  with {self.topping} topping"

class Large(models.Model):
    kind = models.CharField(max_length=40)    
    topping = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f" A Large {self.kind} pizza  with {self.topping} topping"

class Topping(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Subs_small(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"    

class Subs_large(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Salads(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Dinner(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

