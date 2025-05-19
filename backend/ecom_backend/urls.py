"""
URL configuration for ecom_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('payments.urls')),
    path('waf/monitor/', views.waf_monitor, name='waf_monitor'),
    path('', TemplateView.as_view(template_name='products.html'), name='products'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('products/<int:pk>/', TemplateView.as_view(template_name='product_detail.html'), name='product-detail'),
    path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('orders/', TemplateView.as_view(template_name='orders.html'), name='orders'),
    path('payment/', TemplateView.as_view(template_name='payment.html'), name='payment'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
]
