from django.test import TestCase
from shop.models import Book, Category
import datetime

class HomePageTest(TestCase):

	def test_display_home_page(self):

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_home_page_display_books_list(self):

		category =  Category(name='History')
		# Have to save, due to ValueError
		category.save()
		Book.objects.create(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)
		Book.objects.create(category=category, 
					title='Guns, Germs, and Steel',
					author='Jared Diamond',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1997, 3, 2),
					pages=412)

		response = self.client.get('/')

		self.assertContains(response, 'The Fire Next Time')
		self.assertContains(response, 'Guns, Germs, and Steel')