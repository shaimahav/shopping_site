from django.shortcuts import render,redirect
from seller.models import *
from django.contrib import messages
from site_admin.models import *
from Buyer.models import *
# Create your views here.
def sellerRegistration(request):
    return render(request,'sellerRegistration.html')
def sellerregisterAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    if(len(request.FILES)>0):
        image=request.FILES['image']
    else:
        image="no pic"
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    seller=seller_tb(name=name,gender=gender,dob=dob,country=country,address=address,image=image,phone=phone,username=username,password=password)
    print(seller)
    seller.save()
    messages.add_message(request,messages.INFO,"Registration successfull")
    return redirect('sellerRegistration')
def addProduct(request):
    category=category_tb.objects.all()
    return render(request,'addProduct.html',{'data':category})
def addProductAction(request):
    name=request.POST['name']
    if(len(request.FILES)>0):
        picture=request.FILES['picture']
    else:
        picture="no pic"
    price=request.POST['price']
    details=request.POST['details']
    stock=request.POST['stock']
    categoryid=request.POST['category']
    category_obj=category_tb.objects.get(id=categoryid)
    sellerid=request.session['id']
    seller_obj=seller_tb.objects.get(id=sellerid)
    product=product_tb(name=name,picture=picture,price=price,details=details,stock=stock,categoryid=category_obj,sellerid=seller_obj)
    product.save()
    messages.add_message(request,messages.INFO,"Product added")
    return redirect('addProduct')
def viewProduct(request):
    sellerid=request.session['id']
    products=product_tb.objects.filter(sellerid=sellerid)
    return render(request,'viewProduct.html',{'data':products})
def delete(request,uid):
    product=product_tb.objects.filter(id=uid).delete()
    return redirect('viewProduct')
def edit(request,uid):
    products=product_tb.objects.filter(id=uid)
    category=category_tb.objects.all()
    return render(request,'editproduct.html',{'data':products,'categ':category})
def editAction(request):
    name=request.POST['name']
    productid=request.POST['productid']
    product=product_tb.objects.filter(id=productid)
    if len(request.FILES)>0:
        picture=request.FILES['picture']
    else:
        picture=product[0].picture
    details=request.POST['details']
    price=request.POST['price']
    stock=request.POST['stock']
    categoryid=request.POST['category']
    category_obj=category_tb.objects.get(id=categoryid)
    sellerid=request.session['id']
    seller_obj=seller_tb.objects.get(id=sellerid)
    productsave=product_tb.objects.filter(id=productid).update(name=name,price=price,details=details,stock=stock,categoryid=category_obj,sellerid=seller_obj)
    product_obj=product_tb.objects.get(id=productid)
    product_obj.picture=picture
    product_obj.save()
    messages.add_message(request,messages.INFO,"Product edited successfully")
    return redirect('viewProduct')
def updateSeller(request):
    sellerid=request.session['id']
    seller=seller_tb.objects.filter(id=sellerid)
    return render(request,'updateSeller.html',{'data':seller})
def updateSellerAction(request):
    sellerid=request.session['id']
    seller=seller_tb.objects.filter(id=sellerid)
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    phone=request.POST['phone']
    if(len(request.FILES)>0):
        image=request.FILES['image']
    else:
        image=seller[0].image
    username=request.POST['username']
    password=request.POST['password']
    seller_save=seller_tb.objects.filter(id=sellerid).update(name=name,gender=gender,dob=dob,country=country,address=address,phone=phone)
    seller_obj=seller_tb.objects.get(id=sellerid)
    seller_obj.image=image
    seller_obj.save()
    messages.add_message(request,messages.INFO,"Updatd successfully")
    return redirect('updateSeller')
def customerOrderView(request):
    sellerid=request.session['id']
    order=order_tb.objects.filter(sellerid=sellerid)
    return render(request,'customerOrderView.html',{'data':order})
def accept(request,uid):
    status=order_tb.objects.filter(id=uid).update(status='accepted')
    return redirect('customerOrderView')
def reject1(request,uid):
    status=order_tb.objects.filter(id=uid).update(status='cancelled')
    return redirect('customerOrderView')
def conformCancel(request,uid):
    order=order_tb.objects.filter(id=uid).update(status="cancellation success")
    return redirect('customerOrderView')
def trackOrder(request,uid):
    order=order_tb.objects.filter(id=uid)
    return render(request,'trackOrder.html',{'data':order})
def trackOrderAction(request):
    orderid=request.POST['orderid']
    orderid_obj=order_tb.objects.get(id=orderid)
    details=request.POST['details']
    date=orderid_obj.date
    time=orderid_obj.time
    details1=details.upper()
    trackorder=tracking_tb(orderid=orderid_obj,details=details,date=date,time=time)
    if 'DELIVERED' in details1:
        order=order_tb.objects.filter(id=orderid).update(status="delivered")
    trackorder.save()
    messages.add_message(request,messages.INFO,"added tracking details")
    return redirect('customerOrderView')
