from django.shortcuts import render
from .models import *
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'store/store.html',context)
def cart(request):
    
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.filter(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.filter(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/checkout.html', context)
def home(request):
    context = {}
    return render(request, 'home/home.html', context)
def blog(request):
    blogs = BlogPost.objects.all()
    context = {"blogs": blogs}
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