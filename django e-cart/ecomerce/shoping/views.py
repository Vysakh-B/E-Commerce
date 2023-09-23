from django.shortcuts import render
from django.contrib.auth.models import User
from  register.models import products
from .models import cart,order
from django.shortcuts import redirect



# Create your views here.
def men(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    mod='Men'
    type=products.objects.filter(gender=mod)
    return render(request,'shop.html',{'gnd':type,'sets':set})
def women(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    mod='women'
    type=products.objects.filter(gender=mod)
    return render(request,'shop.html',{'gnd':type,'sets':set})
def add_cart(request,id):
    if request.user.is_authenticated:     
        u = request.user
        product2=products.objects.get(id=id)
        name = product2.name
        img = product2.image
        model = product2.model_name
        counts = 1
        amount = product2.price
        carts=cart(user=u,product_name=name,count=counts,image=img,model_name=model,amount=amount)
        carts.save()
        return redirect('/')
    else:
        return redirect('/login')
def carts(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    total=0
    # prod = User.objects.get(username=name)
    uname = request.user
    
    cart_items = cart.objects.filter(user=uname)
    # print(cart_items.image)
    for i in cart_items:
        
        am=i.amount
        c=i.count
        tot=am*c
        total=total+tot    
    return render(request,'cart.html',{'list':cart_items,'total':total,'sets':set})
def change(request,id,data):
    counts=cart.objects.get(id=id)
    if(data == 'pls'):
        counts.count +=1
        counts.save()    
    else:
        counts.count -=1
        counts.save()
    return redirect('cart')  
def remove(request,id): 
    row = cart.objects.get(id=id)
    row.delete()
    return redirect('cart')
def checkout(request):
    if request.method == 'POST':
        user = request.user
        country = request.POST['country']
        first = request.POST['c_fname']
        last = request.POST['c_lname']
        address = request.POST['c_address']
        optional = request.POST['c_optional']
        address1 = address+','+optional
        state = request.POST['c_state']
        postal = request.POST['c_postal']
        email = request.POST['c_email']
        phone = request.POST['c_phone']
        payment = request.POST['bank']
        total=0
        cart_items = cart.objects.filter(user=user)
        for k in cart_items:
            product = k.product_name
            qntity = k.count
            img = k.image
            ttl = k.amount
            orders = order(user_name=user,country=country,firstname=first,lastname=last,address=address1,state=state,postal=postal,email=email,phone=phone,products=product,image=img,quantity=qntity,total=ttl,payment=payment)
            orders.save()
        return redirect('thankyou')    

    
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    total=0
    # prod = User.objects.get(username=name)
    uname = request.user
    
    cart_items = cart.objects.filter(user=uname)
    # print(cart_items.image)
    for i in cart_items:
        
        am=i.amount
        c=i.count
        tot=am*c
        total=total+tot    
    return render(request,'checkout.html',{'list':cart_items,'total':total,'sets':set})
    
def thankyou(request):
    u = request.user
    count = cart.objects.filter(user=u)
    set=0
    for c in count:
        set=set+1
    return render(request,'thankyou.html',{'sets':set})
def profile(request):
    if request.user.is_authenticated:
        us = request.user
        count = cart.objects.filter(user=us)
        set=0
        for c in count:
            set=set+1
        order_items = order.objects.filter(user_name=us)
        return render(request,'profile.html',{'ord':order_items,'sets':set})
    else:
        return redirect('/login')
def single(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            country = request.POST['country']
            first = request.POST['c_fname']
            last = request.POST['c_lname']
            address = request.POST['c_address']
            optional = request.POST['c_optional']
            address1 = address+','+optional
            state = request.POST['c_state']
            postal = request.POST['c_postal']
            email = request.POST['c_email']
            phone = request.POST['c_phone']
            payment = request.POST['bank']
            product_items = products.objects.get(id=id)
            product = product_items.name
            qntity = 1
            img = product_items.image
            ttl = product_items.price
            orders = order(user_name=user,country=country,firstname=first,lastname=last,address=address1,state=state,postal=postal,email=email,phone=phone,products=product,image=img,quantity=qntity,total=ttl,payment=payment)
            orders.save()
            return redirect('thankyou')
        u = request.user
        count = cart.objects.filter(user=u)
        set=0
        for c in count:
            set=set+1
        p_id = products.objects.get(id=id)
        return render(request,'shop-single.html',{'list':p_id,'sets':set})
    else:
        return redirect('/login')


        
    
