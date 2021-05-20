import requests
from bs4 import BeautifulSoup


def extract_info_book(Website, product_page_url):
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract category
        category = soup.find("ul", attrs={"class": "breadcrumb"})
        category = category.find_all("a")
        category = category[2].text

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
                price_excluding_tax = "£" + str((tr.find("td").text).split("£")[1])
            if tr.find("th").text == "Price (incl. tax)":
                price_including_tax =  "£" + str((tr.find("td").text).split("£")[1])
            if tr.find("th").text == "Availability":
                number_available = ""
                available = tr.find("td").text
                for element in available:
                    try:
                        # extraction des chiffres dans la quantité  : In stock (20 available)
                        if int(element) in range(0, 10):
                            number_available += str(element)
                    except ValueError :
                        # on a pas besoin d'afficher l'erreur, si en stock extraction chiffre sinon ZERO
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

        return product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,\
               number_available, product_description, category, review_rating, image_url


if __name__ == "__main__" :
    Website = "http://books.toscrape.com/"
    # exemple url livre : "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
    #input_url = str(input("Merci de saisir l'url du livre dont vous souhaitez extraire les informations : "))
    product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url = extract_info_book(Website,"http://books.toscrape.com/catalogue/sharp-objects_997/index.html")
    print("\nproduct_page_url : " + product_page_url)
    print("universal_product_code : " + universal_product_code)
    print("title : " + title)
    print("price_including_tax : " + price_including_tax + " et " + "price_excluding_tax : " + price_excluding_tax)
    print("number_available : " + str(number_available))
    print("product_description : \n" + product_description)
    print("review_rating : " + str(review_rating))
    print("image_url : " + image_url)
    print("category = " + str(category))

