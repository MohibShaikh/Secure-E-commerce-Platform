import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_backend.settings')
django.setup()

from products.models import Category, Product

def create_sample_data():
    # Create categories
    electronics = Category.objects.get_or_create(name="Electronics", defaults={"description": "Electronic gadgets and devices"})[0]
    clothing = Category.objects.get_or_create(name="Clothing", defaults={"description": "Apparel and accessories"})[0]
    books = Category.objects.get_or_create(name="Books", defaults={"description": "Books and literature"})[0]

    # Sample products with real Unsplash images
    sample_products = [
        {
            "name": "Smartphone X",
            "description": "Latest smartphone with advanced features",
            "price": 699.99,
            "category": electronics,
            "stock": 50,
            "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Laptop Pro",
            "description": "High-performance laptop for professionals",
            "price": 1299.99,
            "category": electronics,
            "stock": 30,
            "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Wireless Earbuds",
            "description": "Premium wireless earbuds with noise cancellation",
            "price": 199.99,
            "category": electronics,
            "stock": 100,
            "image": "https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Cotton T-Shirt",
            "description": "Comfortable cotton t-shirt for everyday wear",
            "price": 24.99,
            "category": clothing,
            "stock": 200,
            "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Classic Novel",
            "description": "A must-read classic novel for book lovers",
            "price": 14.99,
            "category": books,
            "stock": 80,
            "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Denim Jeans",
            "description": "Stylish denim jeans with a modern fit",
            "price": 49.99,
            "category": clothing,
            "stock": 120,
            "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Bluetooth Speaker",
            "description": "Portable Bluetooth speaker with deep bass",
            "price": 59.99,
            "category": electronics,
            "stock": 75,
            "image": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Leather Jacket",
            "description": "Genuine leather jacket for a stylish look",
            "price": 199.99,
            "category": clothing,
            "stock": 40,
            "image": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=400&q=80"
        },
    ]

    for product_data in sample_products:
        product, created = Product.objects.get_or_create(
            name=product_data["name"],
            defaults=product_data
        )
        if not created:
            # Update image if product already exists
            product.image = product_data["image"]
            product.save()

if __name__ == "__main__":
    print("Creating sample products with images...")
    create_sample_data()
    print("Sample products created/updated successfully!") 