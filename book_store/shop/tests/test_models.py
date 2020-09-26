from django.test import TestCase
from shop.models import Book, Category
import datetime

class BookModelTest(TestCase):

	def test_string_representation(self):
		category =  Category(name='History')
		book = Book(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)

		self.assertEqual(str(book), book.title)


class CategoryModelTest(TestCase):

	def test_string_representation(self):
		category =  Category(name='History')
		self.assertEqual(str(category), category.name)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Category._meta.verbose_name_plural), "categories")