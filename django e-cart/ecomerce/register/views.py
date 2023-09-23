from django.shortcuts import render
from .models import products
from  shoping.models import cart,order
from django.contrib.auth.models import User,auth
# from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    item = products.objects.all()
    return render(request,"index.html",{'items':item,'sets':set})
def about(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    item = products.objects.all()
    return render(request,"about.html",{'items':item,'sets':set})
def shop(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    item = products.objects.all()
    return render(request,"shop.html",{'gnd':item,'sets':set})
def signup(request):
    if request.method=='POST':
        # messages.info(request,"data passesd")
        user = request.POST['user']
        password = request.POST['pass']
        if user == "" or password == "":
            messages.info(request,"Enter valid username or password")
            return redirect('register')
        else:
            if User.objects.filter(username = user):
                messages.info(request,"user Already Exist")
                return redirect('register')
            else:
                users=User.objects.create_user(username=user,password=password)
                users.save()
                print(users)
                return redirect('signin')
  
    return render(request,'signup.html')
def login(request):
    if request.method == "POST":
        uname=request.POST['usernme']
        passw=request.POST['password']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')


    return render(request,"signin.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
    # item = products.objects.all()
    # return render(request,"index.html",{'items':item})
def product(request,id):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    product=products.objects.get(id=id)
    print(product)
    return render(request,'product.html',{'product1':product,'sets':set})
def contact(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    return render(request,"contact.html",{'sets':set})