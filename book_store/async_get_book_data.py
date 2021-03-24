import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')
django.setup()
import random
import requests 
from bs4 import BeautifulSoup
import re
import datetime
from urllib.parse import urlparse
from aiohttp import ClientSession
import asyncio
from shop.models import Category, Book

BOOK_DEPO = 'https://www.bookdepository.com/'


async def fetch(url, session):
    async with session.get(url) as response:
        html_body = await response.read()
        return html_body


async def get_book_content(books_ulr):
    tasks = []
    async with ClientSession() as session:
        for book_url in books_ulr:
            tasks.append(
                asyncio.create_task(
                    fetch(book_url, session)
                )
            )
        return await asyncio.gather(*tasks)


def find_all_books(soup):
    books = soup.find_all('div', {'class': 'book-item'})
    return ['https://www.bookdepository.com/' + book_url.find('div', {'class' : 'item-img'}).find('a', href=True)['href'] for book_url in books ]


def retrieve_data(book_data):
    book = {}
    book_soup = BeautifulSoup(book_data, "html.parser")
    book['image'] = book_soup.find('img', {'class': 'book-img'}).get('src')
    book['title'] = book_soup.find('h1', {'itemprop': 'name'}).text.strip()
    book['author'] = book_soup.find('div', {'class': 'author-info hidden-md'}).find('span', {'itemprop' : 'name'}).text.strip()
    book['publisher'] = book_soup.find('div', {'class': 'biblio-wrap'}).find('span', {'itemprop': 'publisher'}).find('span', {'itemprop': 'name'}).text.strip()
    book['description'] = " ".join(book_soup.find('div', {'class': 'item-excerpt trunc', 'itemprop' : 'description'}).text.split())
    try: 
        book['numberOfPages'] = re.findall(r"\d+",book_soup.find('span', {'itemprop': 'numberOfPages'}).text )[0]
    except AttributeError:
       book['numberOfPages'] = 1000
    try:
        book['datePublished'] = datetime.datetime.strptime(book_soup.find('span', {'itemprop': "datePublished"}).text, '%d %b %Y')
    except AttributeError:
        book['datePublished'] = datetime.datetime(year=1900, month=1, day=1)

    return book


def insert_into_db(dict_data):
    book = Book(category=random.choice(Category.objects.all()),
                title=dict_data['title'],
                author=dict_data['author'],
                publishing_house=dict_data['publisher'],
                description=dict_data['description'],
                price=round(random.uniform(10, 40), 2),
                release_date=dict_data['datePublished'],
                pages=dict_data['numberOfPages'],
                image=dict_data['image']
                )
    book.save()


if __name__ == '__main__':
    result = requests.get(BOOK_DEPO)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
        books_ulr = find_all_books(soup)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        books_html_data = asyncio.run(get_book_content(books_ulr))

        for book_data in books_html_data:
            dict_data = retrieve_data(book_data)
            insert_into_db(dict_data)
