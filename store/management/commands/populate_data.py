from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database...')

        # Create admin user if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user (username: admin, password: admin123)'))

        # Create demo user
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user('demo', 'demo@example.com', 'demo123')
            self.stdout.write(self.style.SUCCESS('Created demo user (username: demo, password: demo123)'))

        # Create categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics', 'description': 'Electronic devices and gadgets'},
            {'name': 'Clothing', 'slug': 'clothing', 'description': 'Fashion and apparel'},
            {'name': 'Books', 'slug': 'books', 'description': 'Books and publications'},
            {'name': 'Home & Garden', 'slug': 'home-garden', 'description': 'Home and garden products'},
        ]

        for cat_data in categories_data:
            Category.objects.get_or_create(slug=cat_data['slug'], defaults=cat_data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(categories_data)} categories'))

        # Create products
        electronics = Category.objects.get(slug='electronics')
        clothing = Category.objects.get(slug='clothing')
        books = Category.objects.get(slug='books')
        home = Category.objects.get(slug='home-garden')

        products_data = [
            {'name': 'Wireless Headphones', 'slug': 'wireless-headphones', 'category': electronics,
             'description': 'Premium wireless headphones with noise cancellation and 30-hour battery life.', 'price': 99.99, 'stock': 50},
            {'name': 'Smartphone', 'slug': 'smartphone', 'category': electronics,
             'description': 'Latest smartphone with 6.5" display, 128GB storage, and advanced camera system.', 'price': 599.99, 'stock': 30},
            {'name': 'Laptop', 'slug': 'laptop', 'category': electronics,
             'description': 'Powerful laptop with Intel i7 processor, 16GB RAM, and 512GB SSD.', 'price': 899.99, 'stock': 20},
            {'name': 'Smartwatch', 'slug': 'smartwatch', 'category': electronics,
             'description': 'Fitness tracking smartwatch with heart rate monitor and GPS.', 'price': 249.99, 'stock': 40},

            {'name': 'Classic T-Shirt', 'slug': 'classic-t-shirt', 'category': clothing,
             'description': '100% cotton t-shirt in various colors. Comfortable and durable.', 'price': 19.99, 'stock': 100},
            {'name': 'Denim Jeans', 'slug': 'denim-jeans', 'category': clothing,
             'description': 'Classic fit denim jeans with stretch comfort.', 'price': 49.99, 'stock': 75},
            {'name': 'Winter Jacket', 'slug': 'winter-jacket', 'category': clothing,
             'description': 'Warm winter jacket with water-resistant outer shell.', 'price': 129.99, 'stock': 35},
            {'name': 'Running Shoes', 'slug': 'running-shoes', 'category': clothing,
             'description': 'Lightweight running shoes with cushioned sole and breathable mesh.', 'price': 79.99, 'stock': 60},

            {'name': 'Python Programming', 'slug': 'python-programming', 'category': books,
             'description': 'Comprehensive guide to Python programming for beginners and experts.', 'price': 39.99, 'stock': 45},
            {'name': 'Mystery Novel', 'slug': 'mystery-novel', 'category': books,
             'description': 'Bestselling mystery thriller with unexpected twists.', 'price': 14.99, 'stock': 80},
            {'name': 'Cook Book', 'slug': 'cook-book', 'category': books,
             'description': 'Delicious recipes from around the world with step-by-step instructions.', 'price': 24.99, 'stock': 55},

            {'name': 'Coffee Maker', 'slug': 'coffee-maker', 'category': home,
             'description': 'Programmable coffee maker with 12-cup capacity and auto shut-off.', 'price': 49.99, 'stock': 40},
            {'name': 'Bed Sheets Set', 'slug': 'bed-sheets-set', 'category': home,
             'description': 'Soft microfiber bed sheets set including pillowcases.', 'price': 29.99, 'stock': 65},
            {'name': 'Garden Tools Set', 'slug': 'garden-tools-set', 'category': home,
             'description': 'Complete gardening tool set with durable handles.', 'price': 59.99, 'stock': 30},
            {'name': 'Table Lamp', 'slug': 'table-lamp', 'category': home,
             'description': 'Modern table lamp with adjustable brightness and USB charging port.', 'price': 34.99, 'stock': 50},
        ]

        for prod_data in products_data:
            Product.objects.get_or_create(slug=prod_data['slug'], defaults=prod_data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(products_data)} products'))
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
