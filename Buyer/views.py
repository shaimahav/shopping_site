from django.shortcuts import render,redirect
from django.contrib import messages
from Buyer.models import*
from seller.models import*
from site_admin.models import*
from django.http import JsonResponse
from seller.models import*
import datetime

# Create your views here.
def buyerRegistration(request):
    return render(request,'buyerRegistration.html')
def  registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    buyer=buyer_tb(name=name,gender=gender,dob=dob,country=country,phone=phone,address=address,username=username,password=password)
    buyer.save()
    messages.add_message(request,messages.INFO,"Registration successfull")
    return redirect('buyerRegistration')
def updateProfile(request):
    userid=request.session['id']
    buyer=buyer_tb.objects.filter(id=userid)
    return render(request,'updateBuyerProfile.html',{'data':buyer})
def updateBuyerAction(request):
    userid=request.session['id']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    buyer=buyer_tb.objects.filter(id=userid).update(name=name,gender=gender,dob=dob,country=country,phone=phone,address=address,username=username,password=password)
    messages.add_message(request,messages.INFO,"update successfull")
    return redirect('updateProfile')
def checkUsername(request):
    username=request.GET['data']
    buyer=buyer_tb.objects.filter(username=username)
    seller=seller_tb.objects.filter(username=username)
    if len(buyer)>0:
        msg="exist"
    elif len(seller)>0:
        msg="exist"    
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def viewAllProduct(request):
    product=product_tb.objects.all()
    return render(request,'viewAllProduct.html',{'data':product})
def addtocart(request,uid):
    product=product_tb.objects.filter(id=uid)
    return render(request,'addtoCart.html',{'data':product})
def addtoCartAction(request):
    productid=request.POST['productid']
    product_obj=product_tb.objects.get(id=productid)
    stock=product_obj.stock
    print(stock)
    buyerid=request.session['id']
    buyer_obj=buyer_tb.objects.get(id=buyerid)
    shippingaddress=request.POST['shippingaddress']
    contactno=request.POST['contactno']
    quantity=request.POST['quantity']
    print(quantity)
    totalprice=request.POST['totalprice']
    if(stock<quantity):
        messages.add_message(request,messages.INFO,"stock less than entered quantity")
        return redirect('addtocart',uid=productid)
    else:
        cart=cart_tb(productid=product_obj,buyerid=buyer_obj,shippingaddress=shippingaddress,contactno=contactno,quantity=quantity,totalprice=totalprice)
        cart.save()
        messages.add_message(request,messages.INFO,"Added to cart")
    return redirect('viewAllProduct')
def viewCart(request):
    buyerid=request.session['id']
    cart=cart_tb.objects.filter(buyerid=buyerid)
    return render(request,'viewCart.html',{'data':cart})
def delet(request,uid):
    cart=cart_tb.objects.filter(id=uid).delete()
    return redirect('viewCart')
def orderAction(request):
    order=request.POST.getlist('cart')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    for cid in order:
        cartitem=cart_tb.objects.filter(id=cid)
        print(cartitem)
        productid=cartitem[0].productid
        buyerid=request.session['id']
        buyer_obj=buyer_tb.objects.get(id=buyerid)
        sellerid=cartitem[0].productid.sellerid
        shippingaddress=cartitem[0].shippingaddress
        quantity=cartitem[0].quantity
        totalprice=cartitem[0].totalprice
        stock=cartitem[0].productid.stock
        pid=cartitem[0].productid.id
        if(int(cartitem[0].productid.stock)<quantity):
            messages.add_message(request,messages.INFO,"stock lessthan order")
            return redirect('viewCart')
        else:
            orderitem=order_tb(date=date,time=time,productid=productid,buyer_id=buyer_obj,sellerid=sellerid,shippingaddress=shippingaddress,quantity=quantity,totalprice=totalprice)
            newstock=int(stock)-quantity
            productupdate=product_tb.objects.filter(id=pid).update(stock=stock)
            orderitem.save()
            cartitem.delete()
            messages.add_message(request,messages.INFO,"ordered successfully")
            return redirect('viewCart')
def viewOrder(request):
    buyerid=request.session['id']
    order=order_tb.objects.filter(buyer_id=buyerid)
    return render(request,'viewOrder.html',{'data':order})
def cancel(request,uid):
    status="cancelled"
    order=order_tb.objects.filter(id=uid).update(status=status)
    return redirect('viewOrder')
def viewTrackDetails(request,uid):
    track=tracking_tb.objects.filter(orderid=uid).order_by('-id')
    return render(request,'viewTrackDetails.html',{'data':track})
def searchProduct(request):
    return render(request,'searchProduct.html')
def searchProductAction(request):
    word=request.POST['word']
    products=product_tb.objects.filter(name__istartswith=word)
    return render(request,'viewAllProduct.html',{'data':products})
def searchProductCategory(request):
    category=category_tb.objects.all()
    return render(request,'searchProductCategory.html',{'categ':category})
def searchProductbyCategoryAction(request):
    category=request.POST['category']
    #category_obj=category_tb.objects.get(category_name=category)
    #categoryid=category_obj.id
    print(category)
    price=request.POST['price']
    print(price)
    pro=product_tb.objects.filter(price__lte=price,categoryid=category)
    return render(request,'viewAllProduct.html',{'data':pro})
    



        
