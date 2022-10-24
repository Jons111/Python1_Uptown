from django.db import models

# Create your models here.


class Service(models.Model):
    nomi = models.CharField(max_length=20)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    rasm = models.ImageField(upload_to='media')
    son1 = models.IntegerField()
    son2 = models.IntegerField()
    manzil = models.CharField(max_length=100)
    kv = models.FloatField()
    vaqt = models.DateTimeField(auto_now=True)

class Murojaat(models.Model):
    ism = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)