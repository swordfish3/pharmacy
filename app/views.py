from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import json
from urllib.request import urlopen
from .forms import ProductForm

from django.http import HttpResponseRedirect

from .models import Product


def index(request):
    return HttpResponse("hello there")


def all_products(request):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/?format=json').read().decode('utf-8')
    alldata = json.loads(web_data)
    context = {'alldata': alldata}
    return render(request, 'allproducts.html', context)


def product_info(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/' + str(pharmacyid) + "/?format=json").read().decode('utf-8')
    p_data = json.loads(web_data)
    context = {'pdata': p_data}
    return render(request, "product.html", context)


def post_form(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
            form = ProductForm(request.POST)
            barcode = form.cleaned_data['title']
            name = form.cleaned_data['body']
            quantity = form.cleaned_data['quantity']
            p = Product.objects.get(pk=id)
            Product.objects.create(barcode=barcode, name=name, postId=p, quantity=quantity)
    return HttpResponseRedirect("app/allproducts/" + str(Product.id))

    return render(request, 'buyproduct.html', {'form': form}, )
