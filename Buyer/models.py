from django.db import models

# Create your models here.
class buyer_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phone=models.CharField(max_length=20,default="nophone number")
    country=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class cart_tb(models.Model):
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=50)
    contactno=models.IntegerField()
    totalprice=models.IntegerField()
    quantity=models.IntegerField(default=1)
class order_tb(models.Model):
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    buyer_id=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    sellerid=models.ForeignKey('seller.seller_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=40)
    quantity=models.CharField(max_length=20)
    totalprice=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
