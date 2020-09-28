from django.test import TestCase
from shop.models import Book, Category
import datetime

class HomePageTest(TestCase):
	
	def test_display_home_page(self):

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_home_page_display_just_available_books_list(self):

		category = Category.objects.create(name='History')
		book1 = Book.objects.create(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)
		book2 = Book.objects.create(category=category, 
					title='Guns, Germs, and Steel',
					author='Jared Diamond',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1997, 3, 2),
					pages=588,
					available=False)

		response = self.client.get('/')

		self.assertContains(response, book1.title)
		self.assertNotContains(response, book2.title)
	
	
	def test_home_page_display_books_list_from_specific_category(self):
		
		category1 = Category.objects.create(name='Physics', slug='physisc')
		category2 = Category.objects.create(name='Fantasy', slug='fantasy')

		book1 = Book.objects.create(category=category1, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1963, 10, 12),
					pages=412)

		book2 = Book.objects.create(category=category2, 
					title="Gullivers travels",
					author='Jonathan Swift',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(2020, 5, 10),
					pages=201)

		book3 = Book.objects.create(category=category2, 
					title="Bilbo le Hobbit",
					author='J.R.R. Tolkien',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.date(1995, 9, 30),
					pages=995,
					available=False)

		response = self.client.get('/fantasy/')

		self.assertNotContains(response, book1.title)
		self.assertNotContains(response, book3.title)
		self.assertContains(response, book2.title)

class BookDetailTest(TestCase):

	def test_display_book_detail_page(self):
		category = Category.objects.create(name='Fantasy', slug='fantasy')
		book = Book.objects.create(category=category, 
									title="Bilbo le Hobbit",
									slug='bilbo-le-hobbit',
									author='J.R.R. Tolkien',
									publishing_house='Ace Books',
									price=22.31,
									release_date=datetime.date(1995, 9, 30),
									pages=995)

		response = self.client.get(f'/{book.id}/{book.slug}/')
		self.assertEqual(response.status_code, 200)

	
	def test_display_book_details(self):
		category = Category.objects.create(name='Fantasy', slug='fantasy')
		book = Book.objects.create(category=category, 
									title="Bilbo le Hobbit",
									slug='bilbo-le-hobbit',
									author='J.R.R. Tolkien',
									publishing_house='Ace Books',
									price=22.31,
									release_date=datetime.date(1995, 9, 30),
									pages=995)

		response = self.client.get(f'/{book.id}/{book.slug}/')

		print(response.content.decode())
		self.assertContains(response, book.title)
		self.assertContains(response, book.author)
		self.assertContains(response, book.release_date)
		self.assertContains(response, book.publishing_house)
		self.assertContains(response, book.price)