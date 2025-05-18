from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductListView, ProductDetailView, CartViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = router.urls + [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
] 