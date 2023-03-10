from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import ProductForm
from django.contrib import messages
from json import dumps
import os

def product_home(request):
    # them product vao cart
    # print(request.user)
    # if 'catagory' in request.session:
    #     products.filter(catagory_id__contains = request.session.get('catagory'))
    products =Product.objects.all()
    token = ""
    if 'search' in request.session:      
        search = request.session.get('search').lower()
        token = request.session.get('search')
        products = Product.objects.filter(name__icontains = search)
        
    if 'field' in request.session:
        field = request.session.get('field')
        print(field)
        products = products.order_by(request.session.get('field'))

    if 'category' in request.session:
        category = request.session.get('category')
        if category != 'all':
            cate = Category.objects.get(name = category)
            products = products.filter(category_id = cate)
    
    context = {
        'products': products,
        'token': token
        }
    return render(request,'home.html',context)

def product_category(request, category):
    request.session['category'] = category
    print(category)
    return redirect('product_home')

def product_search(request):
    token = request.POST.get('search')
    request.session['search'] = token
    # products = Product.objects.filter(name__contains = token)
    # context = {'products':products}
    # return render(request, 'home.html', context)
    return redirect('product_home')

def product_sort(request):
    field = request.POST.get('field')
    sort = request.POST.get('sort')
    if field == None or sort == None:
        # xu ly
        return redirect('product_home')
    if sort == 'desc':
        field = '-' + field

    request.session['field'] = field
    # products = Product.objects.order_by(field)
    
    # context = {'products': products}
    # return render(request, 'home.html', context)
    return redirect('product_home')

def product_detail(request, id):
    product = Product.objects.get(id = id)
    related_products = Product.objects.filter(category_id = product.category_id)
    related_products =related_products.exclude(id=id)
    
    # data = []
    # for pro in related_products:
    #     if pro.id == id:
    #         continue
    #     temp = {
    #         'name': pro.name,
    #         'number': pro.number,
    #         'price': pro.price,
    #         'describe': pro.describe,
    #         'producer': pro.producer,
    #         'image': pro.image,
    #     }
    #     data.append(temp)
    # dataJSON = dumps(data)
    # print(dataJSON)
    context = {'product': product, 'related_products': related_products}
    # return JsonResponse(data)
    return render(request, 'product_detail.html', context)



# def product_add(request):
#     # print(request.FILES)
#     # print(request.POST.get('image'))
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if request.POST.get('name') == '' or request.POST.get('number') == '' or request.POST.get('price') == '' or request.POST.get('image') == '':
#                 messages.warning(request, 'You need enter name, number, price, image')
#                 return redirect('product_add')
#             else:
#                 product = Product.objects.create(
#                                                 name = request.POST.get('name'),
#                                                 number = request.POST.get('number'),
#                                                 price = request.POST.get('price'),
#                                                 describe = request.POST.get('describe'),
#                                                 producer = request.POST.get('producer'),
#                                                 image = request.FILES['image'],
#                                                 user_id = request.user
#                 )
#                 product.save()
#                 return redirect('product_home')
#         else: 
#             # dic = {'action': 'Create'}
#             context = {'product':None,
#                         'action': 'Add',
#                         'product_action': 'product_add'
#                         }
#             return render(request, 'product_form.html',context)
#     else:
#         return redirect('loginPage')

# def product_edit(request, id): 
#     product = Product.objects.get(id=id)
#     if request.user == product.user_id:
#         if request.method == 'POST':
#             if request.POST.get('name') == '' or request.POST.get('number') == '' or request.POST.get('price') == '':
#                 messages.warning(request, 'You need enter name, number, price, image')
#                 return redirect('product_add')
#             else:
#                 product.name = request.POST.get('name')
#                 product.number = request.POST.get('number')
#                 product.price = request.POST.get('price')
#                 product.describe = request.POST.get('describe')
#                 product.producer = request.POST.get('producer')
#                 if 'image' in request.FILES:
#                     product.image = request.FILES['image']
#                 product.save()
#                 return redirect('product_home')
#         else:
#             context = {'product': product,
#                         'action': 'Edit',
#                         'product_action': 'product_edit'
#                         }
#             return render(request, 'product_form.html', context)
#     else:
#         return redirect('product_home')

# def product_delete(request, id):
#     product = Product.objects.filter(id=id)
#     product.delete()
#     return redirect('product_home')

