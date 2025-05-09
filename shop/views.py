from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Tag
from .forms import ProductForm, CategoryForm, TagForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def product_list(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'index.html', {'products': products, 'menu': 'main'})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product, 'menu': 'main'})

@login_required
@permission_required('shop.add_product', raise_exception=True)
def product_edit(request, id=None):
    if id:
        product = get_object_or_404(Product, id=id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'form': form, 'menu': 'main'})

def products_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = tag.product_set.filter(is_deleted=False)
    return render(request, 'index.html', {'products': products, 'filter_title': f'Товары с тегом: {tag.name}', 'menu': 'main'})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories, 'menu': 'category'})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_deleted=False)
    return render(request, 'index.html', {'products': products, 'filter_title': f'Категория: {category.name}', 'menu': 'main'})

@login_required
@permission_required('shop.add_category', raise_exception=True)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form, 'menu': 'category'})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags, 'menu': 'tags'})

@login_required
@permission_required('shop.add_tag', raise_exception=True)
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tag_form.html', {'form': form, 'menu': 'tags'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')