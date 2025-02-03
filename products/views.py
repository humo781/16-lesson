from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from brands.models import Brand
from catalogs.models import Catalog
from colors.models import Color

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        brand_id = request.POST.get('brand')
        category_id = request.POST.get('category')
        color_id = request.POST.get('color')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        brand = get_object_or_404(Brand, pk=brand_id)
        color = get_object_or_404(Color, pk=color_id)
        category = get_object_or_404(Catalog, pk=category_id)
        if name and price and brand and category and color and desc and image:
            Product.objects.create(
                name=name,
                price=price,
                brand=brand,
                category=category,
                color=color,
                description=desc,
                image=image
            )
            return redirect('home')
    brands = Brand.objects.all()
    catalogs = Catalog.objects.all()
    colors = Color.objects.all()
    ctx = {'catalogs': catalogs, 'brands': brands, 'colors': colors}
    return render(request, 'product/product-create.html', ctx)

def product_detail(request, year, month, day, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                created_at__year=year,
                                created_at__month=month,
                                created_at__day=day)

    comments = Comment.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        content = request.POST.get('content')

        if name and rating and content:
            comment = Comment.objects.create(
                product=product,
                user_name=name,
                rating=rating,
                comment=content
            )
            # product.comment.add(comment)
            return redirect(product.get_detail_url())
    ctx = {'product': product, 'comments': comments}
    return render(request, 'product/product-detail.html', ctx)

def product_by_category(request):
    products = Product.objects.all()

    # Filtrlarni olish
    selected_brands = request.GET.getlist('brand')
    selected_colors = request.GET.getlist('color')
    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')

    if selected_brands:
        products = products.filter(brand__name__in=selected_brands)

    if selected_colors:
        products = products.filter(color__name__in=selected_colors)

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    brands = Brand.objects.all()
    colors = Color.objects.all()
    ctx = {'products': products,
           'brands': brands,
           'colors': colors,
           'selected_brands': selected_brands,
           'selected_colors': selected_colors,
           'min_price': min_price,
           'max_price': max_price}
    return render(request, 'product/product-by-category.html', ctx)

