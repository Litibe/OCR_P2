import requests
from bs4 import BeautifulSoup


def extract_categories_books(Website):
    try:
        response = requests.get(Website)
    except:
        pb = "Un problème de connexion est survenue, pas de code Réponse 200"
        return pb
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        categoriesBook = {}
        # extraction des "li" présent dans la 2e div de l'aside
        # sinon extrait que le lien Book
        liInAside = soup.aside.li.a.find_next().findAll("li")
        for element in liInAside:
            a = element.find("a")
            link = Website + a["href"]

            # extraction du nom de la catégorie
            for content in a.contents:
                title = content.split("\n")
                title = title[2].strip("  ")
            categoriesBook[title] = link
        return categoriesBook


if __name__ == "__main__" :
    print("Merci d'exécuter le fichier Main.py directement, présent à la racine du dossier")