from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Product, Order
from .forms import ProductForm, OrderForm

logger = logging.getLogger(__name__)


def index(request):
    html_text = """<h1>Добро пожаловать!</h1>
                    <p>Вы посетили мой первый Django - сайт</p>"""
    logger.info('Переход на главную страницу')

    return HttpResponse(html_text)


def about(request):
    html_text ="""<p>Меня зовут Максим.</p>
                <p>Я студент GB.</p>"""
    logger.info('Переход на страницу с информацией обо мне.')                
    return HttpResponse(html_text)

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})


def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect('client_list')  # Перенаправление на страницу со списком клиентов
    return render(request, 'myapp/add_client.html')

# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         product = Product.objects.create(name=name, description=description, price=price)
#         return redirect('product_list')  # Перенаправление на страницу со списком продуктов
#     return render(request, 'myapp/add_product.html')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Перенаправляем на страницу со списком продуктов после сохранения
    else:
        form = ProductForm()
    return render(request, 'myapp/add_product.html', {'form': form})




# def add_order(request):
#     if request.method == 'POST':
#         client_id = request.POST.get('client_id')
#         product_id = request.POST.get('product_id')
#         quantity = request.POST.get('quantity')
#         order = Order.objects.create(client_id=client_id, product_id=product_id, quantity=quantity)
#         return redirect('order_list')  # Перенаправление на страницу со списком заказов
#     return render(request, 'myapp/add_order.html')

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Создаем объект Order и сохраняем его в базе данных
            order = form.save(commit=False)
            order.save()

            # Добавляем связанные товары в заказ
            selected_products = form.cleaned_data['products']
            for product in selected_products:
                order.products.add(product)
                order.total_amount += product.price

            # Сохраняем изменения в объекте Order
            order.save()

            return render(request, 'myapp/success.html')
    else:
        form = OrderForm()
    
    return render(request, 'myapp/add_order.html', {'form': form})



def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)  # Перенаправляем пользователя на страницу деталей товара после успешного редактирования
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})