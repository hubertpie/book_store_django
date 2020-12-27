# book_store_django
books_store_django it's  project, created for practicing django basics. On this site you can:
- browse books by categories
- look for specific author or title by search bar
- add/delete book to cart
- place order 
- pay with your card by braintree payment gateway
- create user and check his previous orders

## Installation (windows)
First you will need virtualenv
```
python -m venv myenv
myenv\Scripts\activate
```
Then install packages from requirements.txt
```
pip install -r requirements.txt
```
Meanwhile create your braintree account on https://www.braintreepayments.com/
to get your API keys and merchant ID.
Then you have to create your secrets.py file, and create there variables
```python
BRAINTREE_MERCHANT_ID = 'your BRAINTREE_MERCHANT_ID'
BRAINTREE_PUBLIC_KEY = 'your BRAINTREE_PUBLIC_KEY' 
BRAINTREE_PRIVATE_KEY = 'your BRAINTREE_PRIVATE_KEY'
SECRET_KEY = 'your SECRET_KEY' 
DB_PASSWORD = 'your DB_PASSWORD' 
```
Then of course you need to create your user and database for project
```bash
postgres=# create database bookstore;
CREATE DATABASE
postgres=# create user bookstore with encrypted password 'DB_PASSWORD';
CREATE ROLE
postgres=# grant all privileges on database bookstore to bookstore;
GRANT
```
Then make all migrations
```
python .\manage.py migrate
```
and populate data
```
python .\populate_data2.py
```
