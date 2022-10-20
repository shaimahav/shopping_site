from django.shortcuts import render,redirect
from site_admin.models import *
from seller.models import *
from Buyer.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=admin_tb.objects.filter(username=username,password=password)
    seller=seller_tb.objects.filter(username=username,password=password)
    buyer=buyer_tb.objects.filter(username=username,password=password)
    if(user.count()>0):
        request.session['id']=user[0].id
        return render(request,'adminhome.html',{'data':user})
    elif(seller.count()>0):
        request.session['id']=seller[0].id
        return render(request,'sellerhome.html',{'data':seller})
    elif(buyer.count()>0):
        request.session['id']=buyer[0].id
        return render(request,'buyerhome.html',{'data':buyer})
    else:
        messages.add_message(request,messages.INFO,"Incorrect username or password")
def viewAllSellers(request):
    status=['pending','approved']
    seller=seller_tb.objects.filter(status__in=status)
    return render(request,'viewAllSellers.html',{'data':seller})
def addCategory(request):
    return render(request,'addCategory.html')
def addCategoryAction(request):
    category_name=request.POST['category_name']
    category=category_tb(category_name=category_name)
    category.save()
    messages.add_message(request,messages.INFO,"category added")
    return redirect('addCategory')
def approve(request,uid):
    seller=seller_tb.objects.filter(id=uid).update(status="approved")
    return redirect('viewAllSellers')
def reject(request,uid):
    seller=seller_tb.objects.filter(id=uid).update(status="reject")
    return redirect('viewAllSellers')
def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Logout successfull")
    return redirect('login')
def forgotPassword(request):
    return render(request,'forgotPassword.html')
def forgotPasswordUsernameCheck(request):
    username=request.POST['username']
    print(username)
    seller=seller_tb.objects.filter(username=username)
    buyer=buyer_tb.objects.filter(username=username)
    admin=admin_tb.objects.filter(username=username)
    if(seller.count()>0):
        return render(request,'forgotPasswordUsernameCheck.html',{'data':seller})
    elif(buyer.count()>0):
         return render(request,'forgotPasswordUsernameCheck.html',{'data':buyer})
    elif(admin.count()>0):
        return render(request,'forgotPasswordUsernameCheck.html',{'data':admin})
    else:
        messages.add_message(request,messages.INFO,"User does not exist")
        return redirect('forgotPassword')
def forgotPasswordDOBPhoneCountrycheck(request):
    username=request.POST['username']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    seller=seller_tb.objects.filter(dob=dob,country=country,phone=phone)
    buyer=buyer_tb.objects.filter(dob=dob,country=country,phone=phone)
    if(seller.count()>0):
        return render(request,'newpassword.html',{'data':username})
    elif(buyer.count()>0):
        return render(request,'newpassword.html',{'data':username})
    else:
        messages.add_message(request,messages.INFO,"Entered details are incorrect")
        return redirect('forgotPassword')
def newpasswordAction(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    username=request.POST['username']
    seller=seller_tb.objects.filter(username=username)
    print(seller)
    buyer=buyer_tb.objects.filter(username=username)
    print(buyer)
    if(password == newpassword):
        if(seller.count()>0):
            sellerupdate=seller_tb.objects.filter(username=username).update(password=password)
            messages.add_message(request,messages.INFO,"Password changed successfully")
            return redirect('login')
        elif(buyer.count()>0):
            buyerupdate=buyer_tb.objects.filter(username=username).update(password=password)
            messages.add_message(request,messages.INFO,"Password changed successfully")
            return redirect('login')
        else:
            messages.add_message(request,messages.INFO,"Password word does not match")
            return render(request,'newpassword.html',{'data':username})
        

            
            
