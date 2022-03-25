from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
