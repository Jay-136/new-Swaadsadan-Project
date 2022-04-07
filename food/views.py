
from django.http import HttpResponse
from food.models import Gujproduct,Southjproduct,Punjabijproduct,Rajsthaniproduct,Indianstreetproduct,Chinesseproduct
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request ,"food/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        mail = request.POST['mail']
        pnum = request.POST['pnum']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, mail, pass1)
        myuser.phone_number= pnum
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('handlelogin')
    return render(request,'food/register.html')

def restaurantReg(request):
    if request.method == "POST":
        rname = request.POST['rname']
        rmail = request.POST['rmail']
        pnum = request.POST['pnum']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myrestaurant = User.objects.create_user(rname, rmail, pass1)
        myrestaurant.phone_number= pnum
        myrestaurant.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('restaurantLogin')
    return render(request,'food/restaurant-reg.html')


def handlelogin(request):
    if request.method == "POST":
       loginusername= request.POST['loginusername']
       loginpass1 = request.POST['loginpass1']

       user = authenticate(username=loginusername, password=loginpass1)

       if user is not None:
        login(request,user)
        messages.success(request,'successfully logged in!')
        return redirect('index')
       else:
        messages.success(request,"invalid ,pelase try again")
        return redirect('handlelogin')

    return render(request,'food/login.html')

def restaurantLogin(request):
    if request.method == "POST":
       username1= request.POST['username1']
       pass3 = request.POST['pass3']

       user = authenticate(username=username1, password=pass3)

       if user is not None:
        login(request,user)
        messages.success(request,'successfully logged in!')
        return redirect('index')
       else:
        messages.success(request,"invalid ,pelase try again")
        return redirect('restaurantLogin')

    return render(request,'food/restaurant-login.html')

def loggout(request):
    logout(request)
    messages.success(request,"successfully logged out!")
    return redirect("index")

def authentic(request):
    return render(request,"food/authentic.html")

def gujProductView(request):
    prods = Gujproduct.objects.all()
    return render(request, "food/gujrati.html", {'prods' :  prods})

def southProduct(request):
    sprods = Southjproduct.objects.all()
    return render(request, "food/south.html", {'sprods' :  sprods})

def punjabiProduct(request):
    pprods = Punjabijproduct.objects.all()
    return render(request, "food/punjabi.html", {'pprods' :  pprods})

def rajsthaniProduct(request):
    pprods = Rajsthaniproduct.objects.all()
    return render(request, "food/rajsthani.html", {'pprods' :  pprods})

def indianStreetProduct(request):
    pprods = Indianstreetproduct.objects.all()
    return render(request, "food/indian-street-food.html", {'pprods' :  pprods})

def chinesseProduct(request):
    pprods = Chinesseproduct.objects.all()
    return render(request, "food/chinesse.html", {'pprods' :  pprods})

def cartView(request):
    return render(request,'food/cart.html')
