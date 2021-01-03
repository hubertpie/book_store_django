from django.test import TestCase
from orders.models import Order, OrderItem
from shop.models import Book, Category
from datetime import datetime

class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='fantasy',
                                slug='fantasy')
        
        Category.objects.create(name='sci-fi',
                                slug='sci-fi')

        Book.objects.create(category=Category.objects.get(name='fantasy'),
                            title='The Way of Kings',
                            slug='the-way-of-kings',
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
    
    def test_order_string_representation(self):
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
    
    def test_order_total_cost(self):
        OrderItem.objects.create(order=Order.objects.get(id=1),
                                book=Book.objects.get(id=1),
                                quantity=5)
        order = Order.objects.get(id=1)
        self.assertEqual(114.50, order.get_total_cost())

    def test_category_string_representation(self):
        fantasy_category = Category.objects.get(id=1)
        self.assertEqual('fantasy', str(fantasy_category))

    def test_adding_category_without_slug_field(self):
        Category.objects.create(name='history')
        history_category = Category.objects.get(id=3)
        self.assertEqual('history', str(history_category))
        self.assertEqual('history', history_category.slug)
    
    def test_category_absolute_url(self):
        fantasy_category = Category.objects.get(id=1)
        self.assertEqual('/shop/fantasy/', fantasy_category.get_absolute_url())
    
    def test_book_string_representation(self):
        fantasy_book = Book.objects.get(id=1)
        self.assertEqual('The Way of Kings', str(fantasy_book))
    
    def test_book_absolute_url(self):
        fantasy_book = Book.objects.get(id=1)
        self.assertEqual('/shop/1/the-way-of-kings/', fantasy_book.get_absolute_url())

    def test_adding_book_without_slug_field(self):
        Book.objects.create(category=Category.objects.get(name='fantasy'),
                            title="harry potter and the half blood prince",
                            author='Joanne Rowling',
                            publishing_house='Bloomsbury',
                            description="is a fantasy novel written by British author J.K. Rowling and the sixth and penultimate novel in the Harry Potter series. Set during Harry Potter's sixth year at Hogwarts, the novel explores the past of the boy wizard's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.",
                            price=20,
                            release_date=datetime.now(),
                            pages=336)
        harry_potter_book = Book.objects.get(title="harry potter and the half blood prince")
        self.assertEqual('harry-potter-and-the-half-blood-prince', harry_potter_book.slug)