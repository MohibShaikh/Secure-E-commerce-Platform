# Secure E-commerce Platform

A modern, secure e-commerce platform built with Django REST Framework and React.

## Features

- 🔐 Secure Authentication with JWT
- 🛍️ Product Management
- 🛒 Shopping Cart
- 💳 Secure Payment Processing with Stripe
- 👤 User Profiles
- 📦 Order Management
- 🔒 Admin Dashboard

## Tech Stack

### Backend
- Django 4.2
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Stripe API
- Gunicorn
- WhiteNoise

### Frontend (Coming Soon)
- React
- Redux Toolkit
- Material-UI
- Axios

## Security Features

- JWT Authentication with HTTPOnly cookies
- CSRF Protection
- XSS Prevention
- SQL Injection Protection
- Secure Password Hashing
- Rate Limiting
- Input Validation
- Secure File Uploads

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 16+ (for frontend)
- PostgreSQL
- Stripe Account

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/enforced_ecom.git
cd enforced_ecom/backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
DATABASE_URL=sqlite:///db.sqlite3
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

### API Endpoints

#### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login user
- `GET /api/users/profile/` - Get user profile
- `PATCH /api/users/profile/picture/` - Update profile picture

#### Products
- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get product details
- `POST /api/products/` - Create product (admin only)
- `PUT /api/products/{id}/` - Update product (admin only)
- `DELETE /api/products/{id}/` - Delete product (admin only)

#### Cart
- `GET /api/carts/mycart/` - Get user's cart
- `POST /api/cart-items/` - Add item to cart
- `PUT /api/cart-items/{id}/` - Update cart item
- `DELETE /api/cart-items/{id}/` - Remove item from cart

#### Orders
- `GET /api/orders/` - List user's orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Get order details

#### Payments
- `POST /api/payments/` - Process payment
- `GET /api/payments/{id}/` - Get payment details

## Deployment

The project is configured for deployment on Fly.io. See deployment instructions in the [deployment guide](docs/deployment.md).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django REST Framework
- Stripe
- React
- Material-UI 