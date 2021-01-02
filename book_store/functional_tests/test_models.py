from django.test import TestCase
from orders.models import Order, OrderItem
from shop.models import Book, Category
from datetime import datetime

class OrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='fantasy', slug='fantasy')
        Book.objects.create(category=Category.objects.get(name='fantasy'),
                            title='The Way of Kings',
                            author='Brandon Sanderson',
                            publishing_house='Tor Books',
                            description='is an epic fantasy novel written by American author Brandon Sanderson and the first book in The Stormlight Archive series.',
                            price=22.90,
                            release_date=datetime.now(),
                            pages=1001)
        Order.objects.create(first_name='Bob', 
                            last_name='Kowalski', 
                            email="bobkowalski@gmail.com",
                            address='Cucumber Street 10',
                            postal_code='12-200',
                            city='New York')
    
    def test_string_representation(self):
        order = Order.objects.get(id=1)
        expected_object_string_represntation = "Order 1"
        self.assertEqual(expected_object_string_represntation, str(order))

    def test_empty_order_total_cost(self):
        order = Order.objects.get(id=1)
        self.assertEqual(0, order.get_total_cost())

    def test_adding_item_to_order(self):
        OrderItem.objects.create(order=Order.objects.get(id=1),
                                book=Book.objects.get(id=1),
                                quantity=5)
        order = Order.objects.get(id=1)
        self.assertEqual(1, order.items.all().count())
    