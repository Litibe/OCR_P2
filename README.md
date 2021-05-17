# OCR_P2 - Script for Scraping http://books.toscrape.com
***
## General Info
The script was developed to extract all of the books from the http://books.toscrape.com site.
The script will thus extract all the categories offered as well as the books contained in each of them.
For each book, it will be extracted:
<br/>
product_page_url <br/>
universal_ product_code (upc) <br/>
title <br/>
price_including_tax <br/>
price_excluding_tax <br/>
number_available <br/>
product_description <br/>
category <br/>
review_rating <br/>
image_url <br/>
<br/>
All the books in a category will be saved in a summary CSV file, in the name of the category, 
and in a separate folder will be saved a copy of the book cover (jpg format) noted under its code UPC.jpg

***
## Installation virtual environment in terminal
<br/>
$ python3 -m venv env <br/>
$ source env/bin/activate <br/>
$ git clone https://github.com/Litibe/OCR_P2.git <br/>
$ cd OCR_P2 <br/>
$ pip install -r requirements.txt <br/>
$ python3 main.py <br/>

***
## Results
The script will create a "resultat_extraction" folder
containing a folder for csv files and another folder with the covers of each book in code_UPC.JPG format

