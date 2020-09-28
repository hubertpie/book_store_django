from django.test import TestCase
from shop.models import Book, Category
import datetime

class HomePageTest(TestCase):
	
	def test_display_home_page(self):

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_home_page_display_just_available_books_list(self):

		category = Category.objects.create(name='History')
		category.save()

		book1 = Book.objects.create(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)
		book1.save()

		book2 = Book.objects.create(category=category, 
					title='Guns, Germs, and Steel',
					author='Jared Diamond',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1997, 3, 2),
					pages=588,
					available=False)
		book2.save()

		response = self.client.get('/')

		self.assertContains(response, book1.title)
		self.assertNotContains(response, book2.title)
	
	
	def test_home_page_display_books_list_from_specific_category(self):
		
		category1 = Category.objects.create(name='Physics', slug='physisc')
		category1.save()
		category2 = Category.objects.create(name='Fantasy', slug='fantasy')
		category2.save()

		book1 = Book.objects.create(category=category1, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)
		book1.save()

		book2 = Book.objects.create(category=category2, 
					title="Gullivers travels",
					author='Jonathan Swift',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(2020, 5, 10),
					pages=201)
		book2.save()

		book3 = Book.objects.create(category=category2, 
					title="Bilbo le Hobbit",
					author='J.R.R. Tolkien',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1995, 9, 30),
					pages=995,
					available=False)
		book3.save()

		response = self.client.get('/fantasy/')

		self.assertNotContains(response, book1.title)
		self.assertNotContains(response, book3.title)
		self.assertContains(response, book2.title)