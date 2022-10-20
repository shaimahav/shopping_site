from django.db import models

# Create your models here.
class seller_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    image=models.FileField(default="pending")
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=20,default="no phone")
    status=models.CharField(max_length=10,default="pending")
class product_tb(models.Model):
    name=models.CharField(max_length=20)
    picture=models.FileField()
    price=models.IntegerField()
    details=models.CharField(max_length=40)
    stock=models.CharField(max_length=20)
    categoryid=models.ForeignKey('site_admin.category_tb',on_delete=models.CASCADE)
    sellerid=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
class tracking_tb(models.Model):
    orderid=models.ForeignKey('Buyer.order_tb',on_delete=models.CASCADE)
    details=models.CharField(max_length=30,default="Order being prepared")
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
