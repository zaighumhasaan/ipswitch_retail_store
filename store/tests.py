from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
from .models import Category, Product, Cart, CartItem, Order, OrderItem


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics',
            description='Electronic devices'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Electronics')
        self.assertEqual(str(self.category), 'Electronics')


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test description',
            price=Decimal('99.99'),
            stock=10,
            available=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, Decimal('99.99'))
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_in_stock(self):
        self.assertTrue(self.product.in_stock)
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)

    def test_product_get_absolute_url(self):
        url = self.product.get_absolute_url()
        self.assertEqual(url, '/product/test-product/')


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test', slug='test')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test',
            price=Decimal('50.00'),
            stock=10
        )
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        self.assertEqual(str(self.cart), 'Cart for testuser')

    def test_cart_add_item(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.assertEqual(cart_item.get_total_price(), Decimal('100.00'))
        self.assertEqual(self.cart.get_total_items(), 2)


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test', slug='test')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test',
            price=Decimal('99.99'),
            stock=10,
            available=True
        )

    def test_home_view_status_code(self):
        response = self.client.get(reverse('store:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('store:home'))
        self.assertTemplateUsed(response, 'store/home.html')

    def test_home_view_context(self):
        response = self.client.get(reverse('store:home'))
        self.assertIn('products', response.context)
        self.assertIn('categories', response.context)


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test', slug='test')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test description',
            price=Decimal('99.99'),
            stock=10,
            available=True
        )

    def test_product_detail_view_status_code(self):
        response = self.client.get(reverse('store:product_detail', args=['test-product']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_template(self):
        response = self.client.get(reverse('store:product_detail', args=['test-product']))
        self.assertTemplateUsed(response, 'store/product_detail.html')

    def test_product_detail_view_context(self):
        response = self.client.get(reverse('store:product_detail', args=['test-product']))
        self.assertEqual(response.context['product'].name, 'Test Product')


class CartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test', slug='test')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test',
            price=Decimal('99.99'),
            stock=10,
            available=True
        )

    def test_cart_view_status_code(self):
        response = self.client.get(reverse('store:cart'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('store:add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_user_login(self):
        response = self.client.post(reverse('store:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

    def test_user_registration(self):
        response = self.client.post(reverse('store:register'), {
            'username': 'newuser',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)


class CheckoutWorkflowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
        self.category = Category.objects.create(name='Test', slug='test')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test',
            price=Decimal('50.00'),
            stock=10,
            available=True
        )

    def test_checkout_requires_login(self):
        response = self.client.get(reverse('store:checkout'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_checkout_with_login(self):
        self.client.login(username='testuser', password='testpass')
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=2)

        response = self.client.get(reverse('store:checkout'))
        self.assertEqual(response.status_code, 200)

    def test_order_creation(self):
        self.client.login(username='testuser', password='testpass')
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=2)

        order_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'city': 'Ipswich',
            'postal_code': 'IP1 1AA',
            'country': 'United Kingdom',
            'payment_method': 'credit_card'
        }

        response = self.client.post(reverse('store:checkout'), order_data)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(response.status_code, 302)  # Redirect to confirmation
