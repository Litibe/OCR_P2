import requests
from bs4 import BeautifulSoup

url_website_catalogue = "http://books.toscrape.com/catalogue/"

def extractBooksFromListPage(url) :
    response = requests.get(url)
    if response.ok:
        books = []
        soup = BeautifulSoup(response.text, 'lxml')
        #extraction des livres présent dans <section> puis dans 2e div, puis dans <ol>
        li_books = soup.section.ol.findAll("li")
        for elt in li_books :
            a = elt.find("a")
            books.append(url_website_catalogue + a["href"].strip("../../.."))

        #recherche dans la page si bouton Next avec modification de l'url de la futur page à scrapper
        next = soup.select(".next a ")
        #si pas de lien Next, renvoi une liste vide
        try :
            url = ("/".join(url.split("/")[:-1] ) + "/") + (str(next).split('"')[1])
        except :
            pass
        return books, next, url


def extractBooksFromCategorie(url) :
    urlBooks = []
    next = ["Next"]
    url = url
    while len(next) > 0 : # si bouton next trouvé dans page, on refait scrapping de la nouvelle page sinon arret
        books, next, url = extractBooksFromListPage(url)
        urlBooks.extend(books)
    return(urlBooks)

