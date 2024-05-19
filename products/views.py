from itertools import product

from django.shortcuts import render, redirect

from .models import Category, Products
from .forms import ProductForm,UpdateForm


def CategoryView(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def ProductView(request, pk):
    product = Products.objects.filter(category=pk)
    return render(request, 'products.html', {'product': product})


def DetailsView(request, pk):
    detail = Products.objects.get(pk=pk)
    return render(request, 'details.html', {'detail': detail})


# POST qoshish funksiyasi
def PostView(request):
    post = ProductForm(request.POST, request.FILES)
    if post.is_valid():
        post.save()
        return redirect('category')
    return render(request, 'post.html', {'post': post})


# Update qilish
def UpdateView(request, pk):
    data = Products.objects.get(pk=pk)
    if request.method == 'POST':
        update = UpdateForm(request.POST, request.FILES, instance=data)
        if update.is_valid():
            update.save()
            return redirect('category')
    else:
        update = UpdateForm(request.POST,request.FILES,instance=data)
    return render(request, 'update.html', {'update': update})
