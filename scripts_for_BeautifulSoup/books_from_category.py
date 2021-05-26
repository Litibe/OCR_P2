import requests
from bs4 import BeautifulSoup

url_website_catalogue = "http://books.toscrape.com/catalogue/"


def extract_books_from_list_page(url):
    response = requests.get(url)
    if response.ok:
        books = []
        soup = BeautifulSoup(response.content, 'html.parser')
        # extraction des livres présent dans <section> puis dans 2e div, puis dans <ol>
        liste_books = soup.section.ol.findAll("li")
        for book in liste_books:
            a = book.find("a")
            # extraction url dans lien a href pour chaque livre
            books.append(url_website_catalogue + a["href"].strip("../../.."))

        # recherche dans la page si bouton Next avec modification de l'url de la futur page à scrapper
        link_next = soup.select(".next a ")
        # si pas de lien Next, renvoi une liste vide
        try:
            url = ("/".join(url.split("/")[:-1]) + "/") + str(link_next).split('"')[1]
        except IndexError :
            # si pas d'autres pages à inspecter, pas besoin d'afficher l'erreur
            pass
        return books, link_next, url


def extract_books_from_category(url):
    url_books = []
    link_next = ["Next"]
    while len(link_next) > 0:  # si bouton next trouvé dans page, on refait scrapping de la nouvelle page sinon arret
        books, link_next, url = extract_books_from_list_page(url)
        url_books.extend(books)
    return (url_books)



if __name__ == "__main__" :
    print("Merci d'exécuter le fichier Main.py directement, présent à la racine du dossier")