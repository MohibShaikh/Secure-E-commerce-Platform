from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings
from django.db import transaction
from orders.models import Order, OrderItem
from products.models import Product

# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='create_intent/(?P<order_id>[^/.]+)')
    def create_intent(self, request, order_id=None):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
        amount = int(order.total_price * 100)  # Convert dollars to cents
        try:
            intent = stripe.PaymentIntent.create(
                amount=50,
                currency='usd',
                metadata={'order_id': order_id},
            )
            return Response({
                'client_secret': intent.client_secret,
                'publishable_key': settings.STRIPE_PUBLISHABLE_KEY
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='confirm/(?P<order_id>[^/.]+)')
    def confirm_payment(self, request, order_id=None):
        try:
            with transaction.atomic():
                order = Order.objects.select_for_update().get(id=order_id, user=request.user)
                # Lock all products in this order
                product_ids = [item.product_id for item in order.items.all()]
                products = Product.objects.select_for_update().filter(id__in=product_ids)
                product_map = {p.id: p for p in products}
                # Check stock
                for item in order.items.all():
                    product = product_map[item.product_id]
                    if product.stock < item.quantity:
                        return Response({'error': f'Not enough stock for {product.name}.'}, status=status.HTTP_400_BAD_REQUEST)
                # Decrease stock
                for item in order.items.all():
                    product = product_map[item.product_id]
                    product.stock -= item.quantity
                    product.save()
                # Mark order as processing/paid
                order.status = 'processing'
                order.save()
            return Response({'message': 'Payment confirmed, stock updated.'})
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Stripe integration and webhook handling would go here
