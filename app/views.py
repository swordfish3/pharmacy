import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from urllib.request import urlopen
from .models import Product

from cart.cart import Cart


def index(request):
    return HttpResponse("hello there")


def all_products(request):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/?format=json').read().decode('utf-8')
    alldata = json.loads(web_data)
    context = {'alldata': alldata}
    return render(request, 'allproducts.html', context)


def product_info(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/' + str(pharmacyid) + '/?format=json').read().decode('utf-8')
    p_data = json.loads(web_data)
    context = {'pdata': p_data}
    return render(request, "product.html", context)


def add_to_cart(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/' + str(pharmacyid) + '/?format=json').read().decode('utf-8')
    p_data = json.loads(web_data)
    quantity = request.POST.get('quantity')
    product = Product.objects.create_product \
        (p_data['name'], p_data['barcode'], p_data['price_retail'], quantity)
    cart = Cart(request)
    cart.add(product, p_data['price_retail'], quantity)
    return render(request, 'cart.html', {'cart': cart}, )



def remove_from_cart(request):
    product_id =request.POST.get('id')
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    return render(request, 'cart.html', {'cart': cart}, )

def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))