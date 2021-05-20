import csv
import os
import shutil
import urllib.request

from scripts_for_BeautifulSoup.categories_books import extract_categories_books
from scripts_for_BeautifulSoup.books_from_category import extract_books_from_category
from scripts_for_BeautifulSoup.extract_info_book import extract_info_book

WEBSITE = "http://books.toscrape.com/"

current_dir = os.path.dirname(__file__)
extract_folder = os.path.join(current_dir, "resultat_extraction")
img_by_categories_folder = os.path.join(extract_folder, "Fichiers IMG par catégorie")
files_csv_folder = os.path.join(extract_folder, "Fichiers CSV")


def reset_folders():
    if os.path.exists(extract_folder):
        try:
            shutil.rmtree(extract_folder)
        except OSError as e:
            print(e.strerror)
    os.makedirs(extract_folder)
    os.makedirs(files_csv_folder)
    os.makedirs(img_by_categories_folder)


def extract_all(WEBSITE):
    # extraction des catégories de livres
    categories_book = extract_categories_books(WEBSITE)
    if isinstance(categories_book, dict):

        i = 1

        for category, url_category in categories_book.items():

            # extraction des url des livres présents dans chaque catégorie
            url_books_in_category = extract_books_from_category(url_category)
            print("\n La Catégorie", category, "contient", len(url_books_in_category), "livres")
            print(url_category)



            # extraction info d'un livre issue d'une catégorie
            data_to_write_for_csv = []
            for product_page_url in url_books_in_category:
                product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, \
                number_available, product_description, category, review_rating, \
                image_url = extract_info_book(WEBSITE, product_page_url, category)
                data_to_write_for_csv.append([product_page_url, universal_product_code, title, price_including_tax,
                                              price_excluding_tax, number_available, product_description, category,
                                              review_rating, image_url])

                # enregistrement fichier img dans dossier :
                # creation dossier au nom de la categorie dans dossier IMG
                category_folder = os.path.join(img_by_categories_folder, category)
                os.makedirs(category_folder)
                urllib.request.urlretrieve(image_url, category_folder + "/" + universal_product_code + ".jpg")

                print("Etat de l'extraction : ", str(round(i / 10, 1)) + "%")
                i += 1

            # creation fichier au nom de la catégorie
            file_csv = os.path.join(files_csv_folder, (str(category) + ".csv"))
            with open(file_csv, "w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product_page_url", "universal_product_code", "title", "price_including_tax",
                                 "price_excluding_tax", "number_available", "product_description", "category",
                                 "review_rating", "image_url"])
                for book in data_to_write_for_csv:
                    writer.writerow(book)
        print("fin du programme")


    else:
        print("Une erreur est survenue ou pb Internet")


def main() :
    run = True
    while run == True :
        print("""
        Sommaire : 
            11 => Extraction de tous les livres de toutes les catégories + Tableaux CSV + Dossier JPG
            12 => Extraction de tous les livres de toutes les catégories + Tableaux CSV 
            13 => Extraction de tous les livres de toutes les catégories + Dossier JPG 
            
            21 => Extraction Livres d'une URL de catégories précises + Tableau CSV + Dossier JPG
            22 => Extraction Livres d'une URL de catégories précises + Tableau CSV 
            23 => Extraction Livres d'une URL de catégories précises + Dossier JPG
    
            31 => Extraction Informations d'un Livre précis + Tableau CSV + Dossier JPG
            32 => Extraction Informations d'un Livre précis + Tableau CSV
            33 => Extraction Informations d'un Livre précis + Dossier JPG
            
            0 => Sortie du programme
        """)

        action = (input("Que souhaitez vous faire : "))
        try :
            action = int(action)
        except ValueError as e:
            print(f"Merci de saisir un nombre - erreur : {e}")

        if action == 11 :
            extract_all(WEBSITE)
            run = True
        elif action == 0 :
            run = False

    print("Fin du programme")

if __name__ == "__main__":
    print("Lancement du script scraping pour " + WEBSITE )
    reset_folders()
    main()
else:
    print("Merci d'exécuter le fichier main.py directement")
