from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Adds sample products to the database'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = {
            'Electronics': 'Latest gadgets and electronic devices',
            'Clothing': 'Fashion and apparel for all seasons',
            'Books': 'Best-selling books and literature',
            'Home & Kitchen': 'Everything for your home',
        }

        created_categories = {}
        for name, description in categories.items():
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            created_categories[name] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))

        # Sample products data
        products_data = [
            {
                'name': 'Smartphone X',
                'description': 'Latest smartphone with advanced features',
                'price': Decimal('699.99'),
                'category': 'Electronics',
                'stock': 50,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Laptop Pro',
                'description': 'High-performance laptop for professionals',
                'price': Decimal('1299.99'),
                'category': 'Electronics',
                'stock': 30,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Designer T-Shirt',
                'description': 'Comfortable cotton t-shirt with modern design',
                'price': Decimal('29.99'),
                'category': 'Clothing',
                'stock': 100,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Classic Novel',
                'description': 'Timeless literature masterpiece',
                'price': Decimal('19.99'),
                'category': 'Books',
                'stock': 75,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Smart Coffee Maker',
                'description': 'Programmable coffee maker with smart features',
                'price': Decimal('89.99'),
                'category': 'Home & Kitchen',
                'stock': 40,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Wireless Earbuds',
                'description': 'High-quality wireless earbuds with noise cancellation',
                'price': Decimal('149.99'),
                'category': 'Electronics',
                'stock': 60,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Designer Jeans',
                'description': 'Premium denim jeans with perfect fit',
                'price': Decimal('79.99'),
                'category': 'Clothing',
                'stock': 45,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Cookbook Collection',
                'description': 'Collection of best-selling recipes',
                'price': Decimal('34.99'),
                'category': 'Books',
                'stock': 25,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Smart Home Hub',
                'description': 'Control your home devices with voice commands',
                'price': Decimal('199.99'),
                'category': 'Home & Kitchen',
                'stock': 35,
                'image': 'https://picsum.photos/400/400'
            },
            {
                'name': 'Fitness Tracker',
                'description': 'Track your daily activities and health metrics',
                'price': Decimal('89.99'),
                'category': 'Electronics',
                'stock': 55,
                'image': 'https://picsum.photos/400/400'
            }
        ]

        # Create products
        for product_data in products_data:
            category_name = product_data.pop('category')
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    **product_data,
                    'category': created_categories[category_name]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully added sample products')) 