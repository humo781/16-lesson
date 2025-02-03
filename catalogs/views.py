from django.shortcuts import render, redirect
from .models import Catalog

def create_catalog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        if name and desc:
            Catalog.objects.create(
                name=name,
                desc=desc
            )
            return redirect('home')
    return render(request, 'category/category-create.html')
