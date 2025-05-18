from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from orders.models import Order, OrderItem
from .models import Cart, CartItem

class CartViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def checkout(self, request):
        user = request.user
        cart = self.get_queryset().filter(user=user).first()
        if not cart or not cart.items.exists():
            return Response({'error': 'Cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Create an order from the cart
            order = Order.objects.create(
                user=user,
                total_price=cart.total_price,
                status='pending'
            )
            
            # Create order items from cart items
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
            
            # Empty the cart
            cart.items.all().delete()
            
            return Response({
                'message': 'Checkout successful',
                'order_id': order.id
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'error': f'Checkout failed: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST) 