from django.test import TestCase
from shop.models import Book, Category
from datetime import datetime

class BookModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='fantasy',
							slug='fantasy')
        
		Category.objects.create(name='sci-fi',
								slug='sci-fi')
								
	def test_string_representation_book(self):
		category =  Category(name='History')
		book = Book(category=category, 
					title='The Fire Next Time',
					author='James Baldwin',
					publishing_house='Ace Books',
					price=11.99,
					release_date=datetime.now(),
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
					release_date=datetime.now(),
					pages=412)
		book.save()
		self.assertEqual(book.get_absolute_url(), f'/shop/{book.id}/{book.slug}/')

	def test_adding_book_without_slug_field(self):
		book = Book.objects.create(category=Category.objects.get(name='fantasy'),
    						title="harry potter and the half blood prince",
                            author='Joanne Rowling',
                            publishing_house='Bloomsbury',
                            description="is a fantasy novel written by British author J.K. Rowling and the sixth and penultimate novel in the Harry Potter series. Set during Harry Potter's sixth year at Hogwarts, the novel explores the past of the boy wizard's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.",
                            price=20,
                            release_date=datetime.now(),
                            pages=336)	
		self.assertEqual('harry-potter-and-the-half-blood-prince', book.slug)

class CategoryModelTest(TestCase):

	def test_string_representation(self):
		category =  Category(name='History')
		self.assertEqual(str(category), category.name)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Category._meta.verbose_name_plural), "categories")

	def test_get_absolute_url_category(self):
		category =  Category(name='History', slug='history')
		self.assertEqual(category.get_absolute_url(), f'/shop/{category.slug}/')
	
	def test_adding_category_without_slug_field(self):
		category = Category.objects.create(name='history')
		self.assertEqual('history', category.slug)