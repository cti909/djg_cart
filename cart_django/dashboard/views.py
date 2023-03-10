from django.shortcuts import render, redirect
from django.http import JsonResponse
from products.models import *
from django.contrib import messages

def product_view(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_view.html',context)

def product_add(request):
    # print(request.FILES)
    # print(request.POST.get('image'))
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('name') == '' or request.POST.get('number') == '' or request.POST.get('price') == '' or request.POST.get('image') == '':
                messages.warning(request, 'You need enter name, number, price, image')
                return redirect('product_add')
            else:
                product = Product.objects.create(
                                                name = request.POST.get('name'),
                                                number = request.POST.get('number'),
                                                price = request.POST.get('price'),
                                                describe = request.POST.get('describe'),
                                                producer = request.POST.get('producer'),
                                                image = request.FILES['image'],
                                                user_id = request.user
                )
                product.save()
                return redirect('product_home')
        else: 
            # dic = {'action': 'Create'}
            context = {'product':None,
                        'action': 'Add',
                        'product_action': 'product_add'
                        }
            return render(request, 'product_form.html',context)
    else:
        return redirect('loginPage')

def product_edit(request, id): 
    product = Product.objects.get(id=id)
    if request.user == product.user_id:
        if request.method == 'POST':
            if request.POST.get('name') == '' or request.POST.get('number') == '' or request.POST.get('price') == '':
                messages.warning(request, 'You need enter name, number, price, image')
                return redirect('dashboard')
            else:
                product.name = request.POST.get('name')
                product.number = request.POST.get('number')
                product.price = request.POST.get('price')
                product.describe = request.POST.get('describe')
                product.producer = request.POST.get('producer')
                if 'image' in request.FILES:
                    product.image = request.FILES['image']
                product.save()
                return redirect('dashboard')
        else:
            context = {'product': product,
                        'action': 'Edit',
                        'product_action': 'product_edit'
                        }
            return render(request, 'product_form.html', context)
    else:
        return redirect('dashboard')

def product_delete(request, id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect('dashboard')

def dashboard(request):
    products = list(Product.objects.filter(user_id = request.user))
    # print(data)
    # return JsonResponse(data, safe=False)
    context = {'products': products}
    return render(request,'dashboard.html', context)

def statistical(request):
    # data = Product.objects.all().values('name', 'number')
    # return JsonResponse(list(data), safe=False)
    context = {}
    return render(request, 'statistical.html', context)