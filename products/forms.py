from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class UpdateForm(ModelForm):
    class Meta:
        model = Products
        fields = [ 'image','number']