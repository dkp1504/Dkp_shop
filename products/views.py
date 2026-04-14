from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def home(request):
    featured = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'featured': featured, 'categories': categories})

def index(request):
    category_slug = request.GET.get('category')
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=active_category)
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'products/index.html', {
        'products': products,
        'categories': categories,
        'active_category': active_category,
        'query': query,
    })

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    return render(request, 'products/product_details.html', {'product': product, 'related': related})


def shop(request):
    return redirect('product')