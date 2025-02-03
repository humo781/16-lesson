from django.shortcuts import render, redirect
from products.models import Product
from .models import Brand

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def create_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        if name and desc:
            Brand.objects.create(
                name=name,
                desc=desc
            )
            return redirect('home')
    return render(request, 'brand/brand-create.html')

