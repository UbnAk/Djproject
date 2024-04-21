from django.contrib import admin
from .models import Client, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price', 'date_added']
    ordering = ['name']
    list_per_page = 3
    search_fields = ['name']
    
    fieldsets = [
        (
        'Продукт',
        {
        'classes': ['wide'],
        'fields': ['name'],
        },
        ),
        (
        'Подробности',
        {
        'classes': ['collapse'],
        'description': 'Описание',
        'fields': ['description'],
        },
        ),
        (
        'Цена',
        {
        'fields': ['price'],
        }
        ),
        (
        'Количество и дата',
        {
        'description': 'Дата',
        'fields': ['date_added'],
        }
        ),
        ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    ordering = ['name']
    list_per_page = 3
    
    
    fieldsets = [
        (
        'Имя',
        {
        'classes': ['wide'],
        'fields': ['name'],
        },
        ),
        (
        'Почта',
        {

        'fields': ['email'],
        },
        ),
        (
        'Контактный номер',
        {
        'fields': ['phone_number'],
        }
        ),
        
        ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'get_products_info', 'total_amount', 'order_date')
    ordering = ['-order_date']
    list_per_page = 3
    
    def get_products_info(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    get_products_info.short_description = 'Products'

admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)

# Register your models here.
