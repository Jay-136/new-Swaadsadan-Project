from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from food.models import Category,Product,Cart
from django.shortcuts import render,redirect,get_object_or_404
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
    category = Category.objects.all()
    return render(request,"food/authentic.html",{'category' : category})

def gujProductView(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/gujrati.html", {'prods' :  prods,'category_name':category_name})

def southProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/south.html", {'prods' :  prods,'category_name':category_name})

def punjabiProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/punjabi.html", {'prods' :  prods,'category_name':category_name})

def rajsthaniProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/rajsthani.html", {'prods' :  prods,'category_name':category_name})

def indianStreetProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/indian-street-food.html", {'prods' :  prods,'category_name':category_name})

def chinesseProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
    return render(request, "food/chinesse.html", {'prods' :  prods,'category_name':category_name})

def cartView(request):
    context={}
    items =  Cart.objects.filter(user__id=request.user.id,status=False)
    context['items'] = items
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                pid = request.POST['pid']
            except MultiValueDictKeyError:
                pid = False
            qty = request.POST['qty']
            is_exist = Cart.objects.filter(product__id=pid,user__id=request.user.id,status=False)
            if len(is_exist)>0:
                context["msz"] = "Item Already Exists in your Cart"
                context["cls"] = "alert alert-warning"
            else:
                product = get_object_or_404(Product,id=pid)
                usr = get_object_or_404(User,id=request.user.id)
                c = Cart(user=usr,product=product,quantity=qty)
                c.save()
                context['msz'] = "{} Added in Your Cart".format(product.name)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request,"food/cart.html",context)


def get_cart_data(request):
    items = Cart.objects.filter(user__id=request.user.id,status=False)
    total = 0
    quantity = 0
    for i in items:
        total += (i.product.price)*i.quantity
        quantity += i.quantity

    res = {
        "total":total,"quan":quantity,
    }
    return JsonResponse(res)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(Cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)
    
    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(Cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)