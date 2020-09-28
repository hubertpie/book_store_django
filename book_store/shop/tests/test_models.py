from django.test import TestCase
from shop.models import Book, Category
import datetime

class BookModelTest(TestCase):

	def test_string_representation_book(self):
		category =  Category(name='History')
		book = Book(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)

		self.assertEqual(str(book), book.title)

	def test_get_absolute_url_book(self):
		category =  Category(name='History')
		category.save()
		book = Book(category=category, 
					title='The Fire Next Time',
					slug='the-fire-next-time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)
		book.save()
		self.assertEqual(book.get_absolute_url(), f'/{book.id}/{book.slug}/')


class CategoryModelTest(TestCase):

	def test_string_representation(self):
		category =  Category(name='History')
		self.assertEqual(str(category), category.name)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Category._meta.verbose_name_plural), "categories")


	def test_get_absolute_url_category(self):
		category =  Category(name='History', slug='history')
		self.assertEqual(category.get_absolute_url(), f'/{category.slug}/')