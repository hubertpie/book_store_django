import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')
django.setup()

from faker import Faker
from shop.models import Category, Book
from django.utils import timezone
import random
from datetime import datetime, timedelta
from django.utils.text import slugify

faker = Faker()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

publishing_houses = ['Faber & Faber', 'Influx Press', 'Penned In The Margins', 'Helion', 'Bloomsbury Publishing', 'Penguin Random House']
d1 = datetime.strptime('1/1/1980 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')


def create_books(N):
    for i in range(1, N):
        book = Book.objects.create(category=random.choice(Category.objects.all()),
                            title=faker.sentence(nb_words=4),
                            author=faker.name(),
                            publishing_house=random.choices(publishing_houses),
                            description=faker.text(),
                            price=round(random.uniform(10,49), 2),
                            release_date=random_date(d1, d2),
                            pages=random.randint(100,999))


create_books(200)