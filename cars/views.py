from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_list=Product.objects.all()

    return render(request,'index.html',{'product_list':product_list})

def about(request):
    context={
    "welcome":"from about"
    }
    return render(request,'about.html',context)

def product(request):
    product_list=Product.objects.all()
    #paginator=Paginator(product_list,12)
    #page=request.GET.get('pg')
    #product_list=paginator.get_page(page)
    return render(request,'product.html',{'product_list':product_list})

def contact(request):
    context={
    "welcome":"from contacts"
    }
    return render(request,'contact.html',context)

def login(request):
    context={
    "welcome":"from login"
    }
    return render(request,'login.html',context)

def register(request):
    context={
    "welcome":"from register"
    }
    return render(request,'register.html',context)
