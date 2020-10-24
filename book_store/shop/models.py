from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):

	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200,
							db_index=True,
							unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:book_list_by_category',
						args=[self.slug])
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

class Book(models.Model):

	category = models.ForeignKey(Category,
								related_name='books',
								on_delete=models.CASCADE)
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	author = models.CharField(max_length=100)
	publishing_house = models.CharField(max_length=100)
	image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	added_to_store = models.DateTimeField(auto_now_add=True)
	release_date = models.DateTimeField()
	pages = models.IntegerField()

	class Meta:
		ordering = ('title', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('shop:book_detail',
						args=[self.id, self.slug])

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Book, self).save(*args, **kwargs)