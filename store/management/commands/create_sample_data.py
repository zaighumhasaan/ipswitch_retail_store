from django.core.management.base import BaseCommand
from store.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Creates sample categories and products for the store'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Garden', 'slug': 'home-garden'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
            else:
                self.stdout.write(f'Category already exists: {category.name}')

        # Create products
        products_data = [
            # Electronics
            {'name': 'Wireless Headphones', 'slug': 'wireless-headphones', 'category': 'electronics',
             'description': 'High-quality wireless headphones with noise cancellation', 'price': '79.99', 'stock': 25},
            {'name': 'Smart Watch', 'slug': 'smart-watch', 'category': 'electronics',
             'description': 'Feature-rich smartwatch with fitness tracking', 'price': '199.99', 'stock': 15},
            {'name': 'Bluetooth Speaker', 'slug': 'bluetooth-speaker', 'category': 'electronics',
             'description': 'Portable bluetooth speaker with excellent sound quality', 'price': '49.99', 'stock': 30},
            {'name': 'USB-C Cable', 'slug': 'usb-c-cable', 'category': 'electronics',
             'description': 'Durable USB-C charging cable 2m length', 'price': '12.99', 'stock': 100},

            # Clothing
            {'name': 'Cotton T-Shirt', 'slug': 'cotton-tshirt', 'category': 'clothing',
             'description': 'Comfortable 100% cotton t-shirt available in multiple colors', 'price': '19.99', 'stock': 50},
            {'name': 'Denim Jeans', 'slug': 'denim-jeans', 'category': 'clothing',
             'description': 'Classic fit denim jeans with modern styling', 'price': '59.99', 'stock': 35},
            {'name': 'Winter Jacket', 'slug': 'winter-jacket', 'category': 'clothing',
             'description': 'Warm winter jacket with waterproof exterior', 'price': '129.99', 'stock': 20},
            {'name': 'Running Shoes', 'slug': 'running-shoes', 'category': 'clothing',
             'description': 'Lightweight running shoes with cushioned sole', 'price': '89.99', 'stock': 40},

            # Books
            {'name': 'Python Programming Guide', 'slug': 'python-guide', 'category': 'books',
             'description': 'Comprehensive guide to Python programming for beginners', 'price': '34.99', 'stock': 45},
            {'name': 'Web Development Handbook', 'slug': 'web-dev-handbook', 'category': 'books',
             'description': 'Complete handbook covering HTML, CSS, and JavaScript', 'price': '39.99', 'stock': 30},
            {'name': 'Mystery Novel Collection', 'slug': 'mystery-novels', 'category': 'books',
             'description': 'Collection of bestselling mystery novels', 'price': '24.99', 'stock': 60},

            # Home & Garden
            {'name': 'Coffee Maker', 'slug': 'coffee-maker', 'category': 'home-garden',
             'description': 'Programmable coffee maker with 12-cup capacity', 'price': '79.99', 'stock': 25},
            {'name': 'Indoor Plant Set', 'slug': 'indoor-plants', 'category': 'home-garden',
             'description': 'Set of 3 low-maintenance indoor plants', 'price': '44.99', 'stock': 20},
            {'name': 'Bedding Set', 'slug': 'bedding-set', 'category': 'home-garden',
             'description': 'Luxury cotton bedding set queen size', 'price': '99.99', 'stock': 15},
            {'name': 'Kitchen Knife Set', 'slug': 'knife-set', 'category': 'home-garden',
             'description': 'Professional kitchen knife set with wooden block', 'price': '149.99', 'stock': 18},
        ]

        for prod_data in products_data:
            category = categories[prod_data['category']]
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults={
                    'name': prod_data['name'],
                    'category': category,
                    'description': prod_data['description'],
                    'price': Decimal(prod_data['price']),
                    'stock': prod_data['stock']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(f'Product already exists: {product.name}')

        self.stdout.write(self.style.SUCCESS('\nSample data creation completed!'))
        self.stdout.write(f'Total categories: {Category.objects.count()}')
        self.stdout.write(f'Total products: {Product.objects.count()}')
