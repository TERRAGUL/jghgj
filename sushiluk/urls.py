"""
URL configuration for sushiluk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from user.views import user_profile
from cart.views import cart_view, add_to_cart, remove_from_cart, increase_quantity, decrease_quantity, clear_cart
from shop.views import product_list, product_detail, product_edit, about, contact
from shop.views import product_list, product_detail, product_edit, products_by_tag, category_list, products_by_category, add_category, tag_list, add_tag
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/<int:id>/edit/', product_edit, name='product_edit'),
    path('tag/<int:tag_id>/', products_by_tag, name='products_by_tag'),
    path('categories/', category_list, name='category_list'),
    path('categories/add/', add_category, name='add_category'),
    path('tags/', tag_list, name='tag_list'),
    path('tags/add/', add_tag, name='add_tag'),
    path('category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('user/profile/', user_profile, name='user_profile'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('api/', include('api.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)