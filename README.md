# OCR_P2 - Script for Scraping http://books.toscrape.com
***
## General Info
The script was developed to extract all of the books from the http://books.toscrape.com site.
The script will thus extract all the categories offered as well as the books contained in each of them.
For each book, it will be extracted:

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

All the books in a category will be saved in a summary CSV file, in the name of the category, 
and in a separate folder will be saved a copy of the book cover (jpg format) noted under its code UPC.jpg

***
## Installation virtual environment in terminal
$ python3 -m venv env
$ source env/bin/activate
$ git clone https://github.com/Litibe/OCR_P2.git
$ cd OCR_P2
$ pip install -r requirements.txt
$ python3 main.py

**
## Results
The script will create a "resultat_extraction" folder
containing a folder for csv files and another folder with the covers of each book in code_UPC.JPG format

