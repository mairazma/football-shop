from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_news_creation(self):
        product = Product.objects.create(
          nama="Jersey Real Madrid",
          price="600000",
          description="Jersey Real Madrid asli banget real ori 100%",
          category="Jersey",
          purchase_count=100
        )
        self.assertTrue(product.is_best_seller)
        self.assertEqual(product.category, "Jersey")
        
    def test_product_default_values(self):
        product = Product.objects.create(
          nama="Test Product",
          description="Test content"
        )
        self.assertEqual(product.category, "Sport")
        self.assertEqual(product.purchase_count, 0)
        self.assertFalse(product.is_featured)
        self.assertFalse(product.is_best_seller)
        
    def test_increment_purchase(self):
        product = Product.objects.create(
          nama="Test Product",
          description="Test content"
        )
        initial_count = product.purchase_count
        product.increment_sell()
        self.assertEqual(product.purchase_count, initial_count + 1)
        
    def test_is_best_seller_threshold(self):
        # Test product with exactly 10 sell (should not be best seller)
        product_10 = Product.objects.create(
          nama="Product with 10 sell",
          description="Test content",
          purchase_count=10
        )
        self.assertFalse(product_10.is_best_seller)
        
        # Test news with 21 views (should be hot)
        product_11 = Product.objects.create(
          nama="Product with 11 sell", 
          description="Test content",
          purchase_count=11
        )
        self.assertTrue(product_11.is_best_seller)