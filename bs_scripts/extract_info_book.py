# coding: utf-8

import requests
from bs4 import BeautifulSoup


def extract_info_book(Website, product_page_url, category):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract img
        extract_img = soup.article.find("img")
        title = (extract_img["alt"])
        image_url = Website + (extract_img["src"]).strip("../..")

        # extract info dans tableau
        tableau_description_product = soup.findAll("tr")
        for tr in tableau_description_product:
            if tr.find("th").text == "UPC":
                universal_product_code = tr.find("td").text
            if tr.find("th").text == "Price (excl. tax)":
                price_excluding_tax = tr.find("td").text
            if tr.find("th").text == "Price (incl. tax)":
                price_including_tax = tr.find("td").text
            if tr.find("th").text == "Availability":
                number_available = ""
                available = tr.find("td").text
                for element in available:
                    try:
                        # extraction des chiffres dans la quantité  : In stock (20 available)
                        if int(element) in range(0, 10):
                            number_available += str(element)
                    except ValueError:
                        pass
                try:
                    number_available = int(number_available)
                except ValueError:
                    number_available = int(0)

        # extract product description
        product_description = soup.select_one("article > p")
        product_description = product_description.decode_contents(indent_level=None, eventual_encoding='utf-8', formatter='minimal')
        # extract review_rating
        review_rating = soup.article.find("p", attrs={"class": "star-rating"})
        review_rating = review_rating["class"][1]

        """
            product_page_url
            universal_product_code
            title
            price_including_tax
            price_excluding_tax
            number_available
            product_description
        category
            review_rating
            image_url
        """
        return product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,\
               number_available, product_description, category, review_rating, image_url


if __name__ == "__main__" :
    Website = "http://books.toscrape.com/"

    product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, \
    product_description, category, review_rating, image_url = extract_info_book(Website,
    "http://books.toscrape.com/catalogue/sharp-objects_997/index.html", "categor")
