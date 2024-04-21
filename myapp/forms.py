from django import forms
from .models import Product,Order

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'quantity']  # Поля, которые вы хотите редактировать

        
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount', 'order_date']  # Измените на нужные поля модели Order

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Добавляем виджет для выбора нескольких продуктов
        self.fields['products'].widget = forms.CheckboxSelectMultiple()
        # Отображаем доступные продукты в виде чекбоксов
        self.fields['products'].queryset = Product.objects.all()