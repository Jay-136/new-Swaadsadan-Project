
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from food.models import Category,Order,OrderItem,Product,Cart,Profile
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import random
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    return render(request ,"food/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['mail']
        phone = request.POST['pnum']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pass1,email=email)
                user.set_phone= phone
                user.save()
                print('user created')
        else:
            print("Password not matching..")
            return redirect('register')
        return redirect('handlelogin')
    else:
        return render(request,"food/register.html")

def profile(request):

    profile = Profile.objects.filter(user=request.user).first()
    context = {'profile':profile}
    return render(request,"food/profile.html",context)

def restaurantReg(request):
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # context = {'form':form}
    return render(request,'food/restaurant-reg.html',context)


def handlelogin(request):
    if request.method == "POST":
        loginusername= request.POST['loginusername']
        loginpass1 = request.POST['loginpass1']

        user = auth.authenticate(username=loginusername, password=loginpass1)

       
        if user is not None:
            auth.login(request,user)
            messages.success(request,'successfully logged in!')
            return redirect('index')
        else:
            messages.success(request,"invalid pelase try again")
            return redirect('handlelogin')


    else:
        return render(request,'food/login.html')

# def ChangePassword(request,token):
#     context = {}
#     user_obj = User_Profile.objects.get(forget_password_token = token)
#     print(user_obj)
#     return render(request,"food/reset_password_confirm.html")

# import uuid
# def ForgetPassword(request):

#     return render(request,"food/reset_password.html")

        

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
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/gujrati.html", {'prods' :  prods,'category_name':category_name ,'category_img':category_img})

def southProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/south.html", {'prods' :  prods,'category_name':category_name,'category_img':category_img})

def punjabiProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/punjabi.html", {'prods' :  prods,'category_name':category_name,'category_img':category_img})

def rajsthaniProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/rajsthani.html", {'prods' :  prods,'category_name':category_name,'category_img':category_img})

def indianStreetProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/indian-street-food.html", {'prods' :  prods,'category_name':category_name,'category_img':category_img})

def chinesseProduct(request,slug):
    if(Category.objects.filter(slug=slug)):
        prods = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        category_img = Category.objects.filter(slug=slug).first()
    return render(request, "food/chinesse.html", {'prods' :  prods,'category_name':category_name,'category_img':category_img})

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
        total += int(i.product.price)*i.quantity
        quantity += int(i.quantity)

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

@login_required(login_url='login')
def checkOut(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.quantity > item.quantity:
            Cart.objects.delete(id=item.id)
    
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0 
    price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.quantity 
        price =  item.product.price * item.quantity 
    
    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems':cartitems,'total_price':total_price,'price':price,'userprofile':userprofile}
    return render(request,"food/checkout.html",context)

@login_required(login_url='login')
def placeOrder(request):
        if request.method == "POST":

            currentuser = User.objects.filter(id=request.user.id).first()

            if not currentuser.first_name:
                currentuser.first_name = request.POST.get('fname')
                currentuser.last_name = request.POST.get('lname')
                currentuser.save()

            if not Profile.objects.filter(user=request.user):
                userprofile = Profile()
                userprofile.user = request.user
                userprofile.phone = request.POST.get('phone')
                userprofile.address = request.POST.get('address')
                userprofile.state = request.POST.get('state')
                userprofile.city = request.POST.get('city')
                userprofile.zip = request.POST.get('zip')
                userprofile.payment_mode = request.POST.get('payment_mode')
                userprofile.save()

            neworder = Order()
            neworder.user = request.user
            neworder.fname = request.POST.get('fname')
            neworder.lname = request.POST.get('lname')
            neworder.email = request.POST.get('email')
            neworder.phone = request.POST.get('phone')
            neworder.address = request.POST.get('address')
            neworder.state = request.POST.get('state')
            neworder.city = request.POST.get('city')
            neworder.zip = request.POST.get('zip')
            neworder.payment_mode = request.POST.get('payment_mode')
            neworder.payment_id = request.POST.get('payment_id')
        
            cartitems = Cart.objects.filter(user=request.user)
            cart_total_price = 0
            for item in cartitems:
                cart_total_price = cart_total_price + item.product.price * item.quantity 


            neworder.total_price = cart_total_price

            trackno = 'Patel'+str(random.randint(1111111,9999999)) 
            while Order.objects.filter(tracking_no = trackno) is None:
                trackno = 'Patel'+str(random.randint(1111111,9999999)) 
        
            neworder.tracking_no = trackno
            neworder.save()


            neworderitems = Cart.objects.filter(user=request.user)
            for item in neworderitems:
                OrderItem.objects.create(
                    order=neworder,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )

                # to decrease the product quantity from avaliable stock
                # orderproduct = Product.objects.filter(id=item.product_id).first()
                # orderproduct.quantity = orderproduct.quantity - item.quantity
                # orderproduct.save()
 
            Cart.objects.filter(user=request.user).delete()
            messages.success(request,"Your order has been Placed successfully")
            payMode = request.POST.get('payment_mode')
            if(payMode == "Paid by Razorpay"):
                return JsonResponse({'status':"Your order has been Placed successfully"})
        return redirect("order")

@login_required(login_url='login')
def razorpaycheck(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.quantity

    return JsonResponse({
        'total_price':total_price
    })

def order(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request,'food/orderhistory.html',context)

def orderview(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitem = OrderItem.objects.filter(order=order)
    context = {'order':order,'orderitem':orderitem}
    return render(request,"food/orderview.html",context)

