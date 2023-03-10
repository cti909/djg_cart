from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm #dki
from cart.models import Cart
from products.models import Product

User = get_user_model()

# Create your views here.
def loginPage(request): # tranh trung ham co san login
    if 'search' in request.session:
        del request.session['search']
    if 'field' in request.session:
        del request.session['field']
    if 'category' in request.session:
        del request.session['category']
    context = {}
    return render(request, 'login_form.html',context)

def checklogin(request):
    accounts = User.objects.all()
    # print(accounts)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(accounts[1])
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")
            return redirect('loginPage')

    user = authenticate(request, username = username, password = password)
    print(user)
    if user is None:
        messages.error(request, 'Username or password does not exit')
        return redirect('loginPage')
    else:
        login(request, user)
        if 'temple_cart' in request.session:
            list_product = request.session['temple_cart']
            for product in list_product:
                product_object = Product.objects.get(id=product['product_id']) 
                # product.pop('id')
                # if Cart.objects.all().exists():
                #     id = Cart.objects.latest('id').id
                # else:
                #     id = 0
                # cart = Cart(product['name'], product['image'], product['number'], product['price'])
                # cart = Cart.objects.create(name = product['name'], image = product['image'], number = product['number'], price = product['price'])
                cart_all = Cart.objects.all()
                check = True
                for ptu in cart_all:
                    print(ptu.product_id.id)
                    if ptu.product_id.id == int(product['product_id']):
                        check = False
                        break
                if check:
                    cart = Cart.objects.create(number = product['number'],
                                            product_id = product_object)
                    cart.save()
        
    request.session['position'] = user.position
    return redirect('homepage')

def logoutPage(request):
    if 'search' in request.session:
        del request.session['search']
    if 'field' in request.session:
        del request.session['field']
    if 'category' in request.session:
        del request.session['category']
    logout(request)
    return redirect('homepage')

def registerPage(request):
    if 'search' in request.session:
        del request.session['search']
    if 'field' in request.session:
        del request.session['field']
    if 'category' in request.session:
        del request.session['category']
    # page = 'register'
    # form = UserCreationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     user = form.save(commit=False)
        #     user.username = user.username.lower()
        #     user.save()
        print(request.POST)
        user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password'), name = request.POST.get('name'), 
                        email = request.POST.get('email'), phone = request.POST.get('phone'), address = request.POST.get('address'), position = request.POST.get('position'))
        user.save()
        context = {}
        return redirect('homepage')
    else:        
        return render(request, 'register_form.html')
    
