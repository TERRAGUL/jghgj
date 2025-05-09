from django.shortcuts import render, redirect
from django.http import HttpResponse
from decimal import Decimal
from shop.models import Product
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    for product_id, quantity in cart.items():
        product = Product.objects.filter(id=product_id, is_deleted=False).first()
        if product:
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'menu': 'cart'
    })

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            cart.pop(str(product_id))
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')
