from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/', views.client_list, name='client_list'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_product/', views.create_product, name='add_prodact'),
    path('creat_order/', views.create_order, name='creat_order'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product',),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),]