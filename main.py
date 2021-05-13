import csv
import os
import shutil
import urllib.request

from bs_scripts.categories_books import extract_categories_books as extract_categories_books
from bs_scripts.books_in_categorie import extract_books_from_categorie as extract_books_from_categorie
from bs_scripts.extract_info_book import extract_info_book as extract_info_book

WEBSITE = "http://books.toscrape.com/"

current_dir = os.path.dirname(__file__)
dossier_extraction = os.path.join(current_dir, "resultat_extraction")
dossier_img_categories = os.path.join(dossier_extraction, "Fichiers IMG par catégorie")
dossier_fichiers_csv = os.path.join(dossier_extraction, "Fichiers CSV")
if os.path.exists(dossier_extraction):
    try:
        shutil.rmtree(dossier_extraction)
    except OSError as e:
        print(f"Error:{ e.strerror}")
os.makedirs(dossier_extraction)
os.makedirs(dossier_fichiers_csv)
os.makedirs(dossier_img_categories)

def main(WEBSITE):
    # extraction des catégories de livres
    categories_book = extract_categories_books(WEBSITE)
    if isinstance(categories_book, dict):

        for category, url_categorie in categories_book.items():
            # creation fichier au nom de la catégorie
            fichier_csv = os.path.join(dossier_fichiers_csv, (str(category) + ".csv"))
            with open(fichier_csv, "w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product_page_url", "universal_product_code", "title", "price_including_tax",
                                     "price_excluding_tax", "number_available", "product_description", "category",
                                     "review_rating", "image_url"])

            # extraction des url des livres présents dans chaque catégorie
            url_books_in_categorie = extract_books_from_categorie(url_categorie)
            print("\n la Catégorie", category, "contient", len(url_books_in_categorie), "livres")
            print(url_categorie)
            #creation dossier au nom de la categorie dans dossier IMG
            dossier_category = os.path.join(dossier_img_categories, category)
            os.makedirs(dossier_category)

            # extraction info d'un livre issue d'une catégorie
            i=1
            for product_page_url in url_books_in_categorie:
                print("extraction", i, "sur", len(url_books_in_categorie))
                product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,\
                number_available, product_description, category, review_rating,\
                image_url = extract_info_book(WEBSITE, product_page_url, category)

                with open(fichier_csv, "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([product_page_url, universal_product_code, title, price_including_tax,
                                     price_excluding_tax, number_available, product_description, category,
                                     review_rating, image_url])

                # enregistrement fichier img dans dossier :
                urllib.request.urlretrieve(image_url, dossier_category+"/"+title+".jpg")
                i+=1
        print("fin du programme")


    else:
        print("Une erreur est survenue ou pb Internet")


if __name__ == "__main__":
    main(WEBSITE)
else:
    print("Merci d'exécuter le fichier main.py directement")
