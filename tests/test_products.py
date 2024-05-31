# tests/test_products.py
import unittest
from app import create_app

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_product(self):
        response = self.client.post('/products', json={'name': 'Test Product', 'price': 10.0})
        self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
