from django.db import models
from django.utils import timezone
# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента

class Client(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    address = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    

# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Order #{self.id} by {self.client.name} ({self.order_date})"
    
    
    
    