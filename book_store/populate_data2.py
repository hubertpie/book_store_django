import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')
django.setup()

import random
from shop.models import Category, Book
import requests 
from bs4 import BeautifulSoup
import re
import datetime
from urllib.parse import urlparse
from django.core.files.base import ContentFile
example = 'https://www.bookdepository.com/'
result = requests.get(example)

if result.status_code == 200:
    soup = BeautifulSoup(result.content, "html.parser")

# Find all books from website
books = soup.find_all('div', {'class': 'book-item'})
book_urls = []
# For each book loop and get url to detail website
for book in books:
    book_urls.append('https://www.bookdepository.com/' + book.find('div', {'class' : 'item-img'}).find('a', href=True)['href'])


for book in book_urls:
    result_2 = requests.get(book)
    if result_2.status_code == 200:
        soup2 = BeautifulSoup(result_2.content, 'html.parser')
        image_url = soup2.find('img', {'class': 'book-img'}).get('src')
        name = urlparse(image_url).path.split('/')[-1]
    if result_2.status_code == 200:
        soup2 = BeautifulSoup(result_2.content, 'html.parser')
        book_title = soup2.find('h1', {'itemprop': 'name'}).text.strip()
        book_author = soup2.find('div', {'class': 'author-info hidden-md'}).find('span', {'itemprop' : 'name'}).text.strip()
        book_publisher = soup2.find('div', {'class': 'biblio-wrap'}).find('span', {'itemprop': 'publisher'}).find('span', {'itemprop': 'name'}).text.strip()
        book_desc = " ".join(soup2.find('div', {'class': 'item-excerpt trunc', 'itemprop' : 'description'}).text.split())
        book_release_date = datetime.datetime.strptime(soup2.find('span', {'itemprop': "datePublished"}).text, '%d %b %Y')
        book_pages = re.findall(r"\d+",soup2.find('span', {'itemprop': 'numberOfPages'}).text )[0]

        try:
            book = Book(category=random.choice(Category.objects.all()),
                                title=book_title,
                                author=book_author,
                                publishing_house=book_publisher,
                                description=book_desc,
                                price= round(random.uniform(10, 40), 2),
                                release_date=book_release_date,
                                pages=book_pages)

            request_3 = requests.get(image_url)
            if request_3.status_code == 200:
                book.image.save(name, ContentFile(request_3.content), save=True)
            else:
                continue
        except AttributeError:
            continue