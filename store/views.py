from django.shortcuts import render
from .models import *
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'store/store.html',context)
def cart(request):
    context = {}
    return render(request,'store/cart.html',context)
def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
def home(request):
    context = {}
    return render(request, 'home/home.html', context)
def blog(request):
    blog = BlogPost.objects.all()
    context = {}
    return render(request, 'home/blog.html', context)
def news(request):
    context = {}
    return render(request, 'home/news.html', context)
def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)
def about(request):
    context = {}
    return render(request, 'home/about.html', context)