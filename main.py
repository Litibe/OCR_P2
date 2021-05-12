import csv, os

from bs_scripts.categories_books import extract_categories_books as extract_categories_books
from bs_scripts.books_in_categorie import extract_books_from_categorie as extract_books_from_categorie
from bs_scripts.extract_info_book import extract_info_book as extract_info_book

Website = "http://books.toscrape.com/"

current_dir = os.path.dirname(__file__)
dossier_extraction = os.path.join(current_dir, "resultat_extraction")
if not os.path.exists(dossier_extraction):
    os.makedirs(dossier_extraction)
#else:
    #os.removedirs(dossier_extraction)
    #os.makedirs(dossier_extraction)


def main(Website):
    # extraction des catégories de livres
    categories_book = extract_categories_books(Website)
    if isinstance(categories_book, dict):
        for category, url_categorie in categories_book.items():

            #creation fichier au nom de la catégorie
            fichier_csv = os.path.join(dossier_extraction, (str(category) + ".csv"))
            with open(fichier_csv, "w", newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["product_page_url", "universal_product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"])

            # extraction des url des livres présents dans chaque catégorie
            url_books_in_categorie = extract_books_from_categorie(url_categorie)
            print("la Catégorie", category, "contient", len(url_books_in_categorie), "livres")

            # extraction info d'un livre issue d'une catégorie
            for product_page_url in url_books_in_categorie:
                product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available,\
                    product_description, category, review_rating, image_url = extract_info_book(Website, product_page_url, category)
                """
                with open(fichier_csv, "w", newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([category, product_page_url, universal_product_code, title, price_including_tax,
                      price_excluding_tax, number_available, review_rating, image_url])
                """
            # création du fichier csv au nom de la catégorie
            # with open ((str(categorie)+".csv"),"w", newline='') as csvfile:

    else:
        print("Une erreur est survenue ou pb Internet")


if __name__ == "__main__":
    main(Website)
else:
    print("Merci d'exécuter le fichier main.py directement")
