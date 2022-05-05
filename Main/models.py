from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    Scrap = models.CharField(max_length=50)
    Weight = models.IntegerField(default=0)
    Pickup_date = models.DateField('Pickup date', null=True)
    Total_Price = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=300)
    Address2 = models.CharField(max_length=300)
    locality = models.CharField(max_length=100)




