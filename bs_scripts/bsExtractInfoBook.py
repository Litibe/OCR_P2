import requests
from bs4 import BeautifulSoup
website = "http://books.toscrape.com/"

def extractInfoBook(url) :
    response = requests.get(url)
    if response.ok :
        soup = BeautifulSoup(response.text, 'html.parser')
        #rename url
        product_page_url = url
        #extract img
        extractImg = soup.article.find("img")
        title = (extractImg["alt"])
        image_url = website + (extractImg["src"]).strip("../..")

        #extract info dans tableau
        allTr = soup.findAll("tr")
        for tr in allTr :
            if (tr.find("th").text) == "UPC" :
                universal_product_code = (tr.find("td").text)
            if (tr.find("th").text) == "Price (excl. tax)" :
                price_excluding_tax = (tr.find("td").text)
            if (tr.find("th").text) == "Price (incl. tax)" :
                price_including_tax = (tr.find("td").text)
            if (tr.find("th").text) == "Availability" :
                number_available = ""
                available = (tr.find("td").text)
                for element in available :
                    try :
                        if int(element) in range(0, 10) :
                            number_available += str(element)
                    except :
                        pass
                try :
                    number_available = int(number_available)
                except :
                    number_available = int(0)
            if (tr.find("th").text) == "Number of reviews":
                review_rating = int((tr.find("td").text))
        #extract product description
        product_description = soup.select_one("article > p")
        product_description = product_description.contents[0]

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
        return product_page_url, universal_product_code , title , price_including_tax, price_excluding_tax, number_available,product_description, review_rating, image_url

