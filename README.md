# LUXE — Django E-Commerce Project

A full-featured, beautifully styled e-commerce application built with Django.

## Features
- Product catalog with categories & search
- Product detail pages with related products
- Shopping cart (add, update quantity, remove)
- Multi-step checkout flow
- Payment page (demo/mock)
- Order history with status tracking
- User registration & login
- Responsive dark luxury UI
- Django Admin for full management

## Project Structure
```
ecomm_project/
├── ecomm/              # Project config (settings, urls, wsgi)
├── accounts/           # User auth (register, login, logout)
├── products/           # Product catalog & categories
├── cart/               # Shopping cart logic
├── orders/             # Checkout, payment, order history
├── templates/          # All HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── products/
│   ├── cart/
│   └── orders/
├── static/media/       # Uploaded product images
├── requirements.txt
├── setup.sh            # One-command setup
└── manage.py
```

## Quick Start

### 1. Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Run the setup script (installs deps + migrates + seeds demo data)
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Start the development server
```bash
python manage.py runserver
```

### 4. Open in browser
- **Shop:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin  →  `admin / admin123`

---

## Manual Setup (if setup.sh doesn't work)
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Adding Products via Admin
1. Go to `/admin` and log in
2. Under **Products → Categories**, add categories
3. Under **Products → Products**, add products with images, price, stock
4. Products appear on the homepage and shop page immediately

## URL Overview
| URL | View |
|-----|------|
| `/` | Homepage with featured products |
| `/products/` | All products + category filter + search |
| `/products/<slug>/` | Product detail page |
| `/cart/` | Shopping cart |
| `/cart/add/<id>/` | Add item to cart |
| `/orders/checkout/` | Checkout form |
| `/orders/payment/<id>/` | Payment page |
| `/orders/success/<id>/` | Order success |
| `/orders/history/` | Order history |
| `/accounts/register/` | Register |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/admin/` | Django admin panel |

## Customization
- **Colors / Theme:** Edit CSS variables in `templates/base.html` under `:root { ... }`
- **Currency:** Replace `₹` with your currency symbol in templates
- **Shipping logic:** Edit `orders/views.py`
- **Payment gateway:** Replace mock payment in `orders/views.py` with Razorpay / Stripe SDK
