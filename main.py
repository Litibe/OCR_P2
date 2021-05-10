import csv, os

from bs_scripts.bsCategoriesBooks import extract_categories_books as extract_categories_books
from bs_scripts.bsBooksInCategorie import extractBooksFromCategorie as extractBooksFromCategorie
from bs_scripts.bsExtractInfoBook import extractInfoBook as extractInfoBook

current_dir = os.path.dirname(__file__)
dossier_extraction = os.path.join(current_dir, "resultat_extraction")
if not os.path.exists(dossier_extraction) :
    os.makedirs(dossier_extraction)
else :
    os.remove(dossier_extraction)
    os.makedirs(dossier_extraction)

def main() :
    categoriesBook = extract_categories_books()
    if isinstance(categoriesBook, dict) :
        for categorie, urlCategorie in categoriesBook.items() :
            urlBooksInCategorie = extractBooksFromCategorie(urlCategorie)
            print("la Catégorie", categorie, "contient", len(urlBooksInCategorie), "livres")
            for urlbook in urlBooksInCategorie :
                product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, review_rating, image_url = extractInfoBook(urlbook)
                print(categorie, product_page_url,universal_product_code, title, price_including_tax, price_excluding_tax, number_available,review_rating, image_url)
    else :
        print("Une erreur est survenue ou pb Internet")
    """
    PSEUDO CODE
    for categorie in categories :
        extractUrlProductsFromCategorie()
        for urlproduct in urlProducts :
            dicoProduct = extractInfosFromUrlProduct()
            creationCSVCategorie
    """

if __name__ == "__main__":
    main()
else :
    print("Merci d'exécuter le fichier main.py directement")