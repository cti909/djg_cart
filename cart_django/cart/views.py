from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from products.models import Product
import json
from decimal import *
from django.contrib import messages
import datetime
from django.http import HttpResponse

def cart_home(request):
    # del request.session['id_cart']
    # del request.session['temple_cart']
    if 'search' in request.session:
        del request.session['search']
    if 'field' in request.session:
        del request.session['field']
    if 'category' in request.session:
        del request.session['category']
    if request.user.is_authenticated:
        products = Cart.objects.all()
        
    elif 'temple_cart' in request.session:
        products = request.session.get('temple_cart')
        print(request.session.get('temple_cart'))
        temp = []
        for ptu in products:
            pro = Product.objects.get(id=ptu['product_id'])
            ptu = {'id': ptu['id'],
                'number':ptu['number'],
                'product_id':pro}
            temp.append(ptu)
            # print(pro)
        products = temp
    else:
        products = None
    # product_detail = Product.objects.get(id=products.product_id)
    context = {'products': products}
    return render(request, 'cart_home.html', context)

# Create your views here.
@csrf_exempt
def cart_add(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    if 'id_cart' not in request.session:
        request.session['id_cart'] = 1
    # print(data['product_id'])
    product_object = Product.objects.get(id=data['product_id']) 

    if product_object.number == 0:
        # messages.add_message(request, messages.INFO, 'Empty od this product')
        context = {'message': 'Empty of this product'}
        return render(request,'cart_home.html', context)
    new_cart = {'id':request.session.get('id_cart'),
                'number': data['number'], 
                'product_id': data['product_id']
                }
    if 'temple_cart' not in request.session:
        request.session['temple_cart'] = [new_cart]
    else:
        list_cart = request.session.get('temple_cart')
        list_cart.append(new_cart)
        request.session['temple_cart'] = list_cart
    request.session['id_cart'] += 1 

    # print(request.session.get('temple_cart'))

    if request.user.is_authenticated:
        cart_all = Cart.objects.all()
        check = False
        for product_idx in cart_all:
            # print(data['product_id'])
            if product_idx.product_id.id == Decimal(data['product_id']):
                # cart = Cart.objects.get(id=product_idx.id)
                # cart.number = cart.number + Decimal(data['product_id'])
                # cart.save()
                # if messages:
                    # break
                # else:
                    # messages.add_message(request, messages.WARNING, 'Product existed from your cart') 
                    # check = True
            # return redirect('product_home')
                check = True
                break
        if check == False:
            cart = Cart.objects.create(
                        # name = data['name'], 
                        # image = data['url_image'],
                        number = data['number'], 
                        # price = data['price'],
                        product_id = product_object
                        )
            cart.save()
    # del request.session['id_cart']
    # del request.session['temp_le_cart']
    # context = {}
    # return render(request, 'home.html', context)
    # return redirect('product_home')
    return HttpResponse('Add oke')

# def cart_addp(request):
#     product_object = Product.objects.get(id=request.POST.get('id'))
#     if product_object.number == 0:
#         # messages.add_message(request, messages.INFO, 'Empty of this product')
#         return redirect('cart_home')
#     if request.user.is_authenticated:
#         cart_all = Cart.objects.all()
#         check = False
#         for product_idx in cart_all:
#             if product_idx.product_id.id == request.POST.get('id'):
#                 check = True
#                 break
#         if check == False:
#             cart = Cart.objects.create(
#                         # name = data['name'], 
#                         # image = data['url_image'],
#                         number = data['number'], 
#                         # price = data['price'],
#                         product_id = product_object
#                         )
#             cart.save()
#     else:
#         # xu li
#         return redirect('product_home')


# def cart_edit(request, id):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             product = Cart.objects.get(id=id)
#             num = request.POST.get('number')
#             product.number = num
#             product.save()
#             return redirect('cart_home')
#         else:
#             return
#     else:
#         if request.user.is_authenticated:
#             product = Cart.objects.get(id=id)
#             context = {'product': product, 'action': 'Edit'}
#             return render(request, 'cart_form.html', context)
#         else: 
#             # xu ly chua dang nhap
#             return

def cart_edit(request, id, number):
    
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        cart = Cart.objects.get(product_id=product.id)
        if request.user.is_authenticated:
            cart.number = request.POST.get('num')
            cart.save()
            return redirect('cart_home')
    else:
        cart = Cart.objects.get(id=id)
        product = Product.objects.get(id=cart.product_id.id)
        if request.user.is_authenticated:           
            context = {'product': product, 'number':number}
            return render(request, 'edit_cart.html', context)
       

def cart_delete(request, id):
        if request.user.is_authenticated:
            Cart.objects.filter(id=id).delete()
            return redirect('cart_home')
        else:
            print(id)
            index = 0
            if 'temple_cart' in request.session:
                list_cart = request.session.get('temple_cart')
                print(list_cart)
                for ptu in list_cart:
                    if ptu['id'] == int(id):
                        list_cart.pop(index)
                    index += 1
                request.session['temple_cart'] = list_cart
                return redirect('cart_home')

def order_view(request):    
    request.session['number_product'] = []
    if request.user.is_authenticated:
        list = request.POST.getlist('select_product')
        # print(list)
        if list:
            list_product = []
            total_all = 0
            auto_id = 1
            product_cart = []
            for id_product in list:
                product = Cart.objects.get(id=id_product)
                id = auto_id
                auto_id += 1
                name = product.product_id.name
                image = product.product_id.image
                price = product.product_id.price
                # number = int(request.POST.get('number'+id_product))
                number = product.number
                total = price*number
                total_all += total

                check = Product.objects.get(id=product.product_id.id)
                if number > check.number:
                    # messages.add_message(request, messages.INFO, 'Hello world.')
                    # return redirect('cartid_home')
                    # messages.add_message(request, messages.INFO, 'Empty od this product')
                    # context = {'message': 'Incorrect quantity'}
                    # request.session
                    return redirect('cart_home')
                dic = {'id': id,
                        'name': name,
                        'image': image,
                        'number': number,
                        'price': price,
                        'total': total}
                list_product.append(dic)
                temp = {
                        'id': id_product,
                        'number': number
                    }
                if 'product_cart' not in request.session:
                    request.session['product_cart'] = [temp]
                else:
                    product_cart = request.session.get('product_cart')
                    product_cart.append(temp)
                    request.session['product_cart'] = product_cart
                
            context = {'list_product': list_product, 'total_price': total_all}
            return render(request, 'payment_form.html',context)
        else:
            return redirect('cart_home')
    else:
        return redirect('loginPage')

def payment(request):
    if request.POST.get('receiver') == "" or request.POST.get('phone') == "" or request.POST.get('address') == "":
        # nhap ko du
        # messages.add_message(request, messages.WARNING, 'Incorrect input')
        return redirect('order_view')
    else:
        
        data = request.session.get('product_cart')
        # print(data)
        # order_detail = Order.objects.create
        receiver = request.POST.get('receiver')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # id number
        data = request.session.get('product_cart')
        order = Order.objects.create(
                receiver = receiver,
                phone = phone,
                address = address,
                date = datetime.datetime.now(),
                user_id = request.user.id
            )
        order.save()
        id_order = Order.objects.latest('id')
        # print(id_order.id)
        for product in data:
            # print(product['id'])
            temp = Cart.objects.get(id=product['id'])
            pro = Product.objects.get(id=temp.product_id.id)
            name = pro.name
            price = pro.price
            # describe = pro.describe
            # producer = pro.producer
            image = pro.image
            order_detail = OrderDetail.objects.create(
                    name = name,
                    image =image,
                    number = product['number'],
                    price = price,
                    order_id = Order.objects.get(id=id_order.id)
                )    
            order_detail.save()
            tg = Cart.objects.filter(id=product['id'])
            tg.delete()
            delpro = Product.objects.get(id=temp.product_id.id)
            delpro.number = delpro.number - product['number']
            delpro.save()
        del request.session['product_cart']
        return redirect('history_home')

def history_home(request):
    if request.user.is_authenticated:
        list_order = []
        order = Order.objects.filter(user_id=request.user.id)
        total_price = 0
        auto_id = 1
        # if auto_id % 2 == 1: color_table = 0 
        # else: color_table = 1
        for order_obj in order:
            tg = []      
            # print(order_obj.id)
            order_detail = OrderDetail.objects.filter(order_id=order_obj.id)
            # print(order_detail)
            for product in order_detail:
                # print(product)
                tmp = {
                    'name': product.name,
                    'number': product.number,
                    'price': product.price,
                    'total': product.number*product.price            
                }
                tg.append(tmp)
                total_price += product.number*product.price 
            # print(total_price)
            temp = {
                'auto_id': auto_id,
                'receiver': order_obj.receiver,
                'date': order_obj.date,
                'list_order': tg,
                'count': order_detail.count(),
                'total_price': total_price
            }
            auto_id += 1
            list_order.append(temp)    
        # print(list_order)
        context = {'products': list_order}
        return render(request, 'history_home.html', context)
    else:
        return redirect('loginPage')
    