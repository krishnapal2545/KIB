from django.db import models

class Mobiles(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Electronics(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Fashion(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Home(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Beauty(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Furniture(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class Medicine(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class ShoppingCart(models.Model):
    account_no = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    descrip = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=2083)

class OrderList(models.Model):
    account_no = models.CharField(max_length=20)
    total_amount = models.FloatField()
    order_id = models.CharField(max_length=200)