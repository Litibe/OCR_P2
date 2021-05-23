import os
import shutil

from scripts_for_BeautifulSoup.categories_books import extract_categories_books
from scripts_for_BeautifulSoup.books_from_category import extract_books_from_category
from scripts_for_BeautifulSoup.extract_info_book import extract_info_book
from scripts_for_csv.save_in_csv import save_in_csv_file
from script_save_img.save_img import save_img_in_folder

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

def extract_book_from_category_to_create_csv(url_books_in_category, launch_img) :
    data_to_write_for_csv = []
    for product_page_url in url_books_in_category:
        product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, \
        number_available, product_description, category, review_rating, \
        image_url = extract_info_book(WEBSITE, product_page_url)
        print("La catégorie contient : " + title + " " + product_page_url)
        if launch_img == True:
            save_img_in_folder(img_by_categories_folder, category, image_url, universal_product_code)

        data_to_write_for_csv.append([product_page_url, universal_product_code, title, price_including_tax,
                                      price_excluding_tax, number_available, product_description, category,
                                      review_rating, image_url])
    return img_by_categories_folder, title, product_page_url, category, image_url, universal_product_code, data_to_write_for_csv

def extract_all(WEBSITE,launch_csv, launch_img):
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
            img_by_categories_folder, title, product_page_url, category, image_url, universal_product_code, \
            data_to_write_for_csv = extract_book_from_category_to_create_csv(url_books_in_category, launch_img)


            if launch_csv == True :
                save_in_csv_file(files_csv_folder, category, data_to_write_for_csv)

            print(f"Etat de l'extraction : {i} catégorie(s) sur 50 extraite(s) ")
            i += 1

        print("fin du programme")


    else:
        print("Une erreur est survenue ou pb Internet")

def extract(url_books_in_category,launch_csv, launch_img ) :

    # extraction des url des livres présents dans chaque catégorie
    url_books_in_category = extract_books_from_category(url_books_in_category)
    print("\n La Catégorie contient", len(url_books_in_category), "livres")

    img_by_categories_folder, title, product_page_url, category, image_url, universal_product_code, \
    data_to_write_for_csv = extract_book_from_category_to_create_csv(url_books_in_category, launch_img)

    if launch_csv == True:
        save_in_csv_file(files_csv_folder, category, data_to_write_for_csv)
    print("Fin de l'extraction")

def summary_choice2X_extract_books_from_category():
    categoriesBook = extract_categories_books(WEBSITE)
    i = 0
    choix_categories_liste = []
    print("Voici la liste des Catégories de Livres : ")
    for category in categoriesBook:
        print("\t choix n°" + str(i) + " pour " + category)
        choix_categories_liste.append(category)
        i += 1
    validation = False
    while validation == False :
        choix = input("Taper votre N° de Catégorie à traiter svp : ")
        try :
            if int(choix) < len(choix_categories_liste):
                validation = True
            else :
                print("Merci de saisir un chiffre compris dans la liste ci-dessus")
        except :
            print("Merci de saisir un chiffre valide svp")


    print("Vous avez choisi : " + str(choix_categories_liste[int(choix)]))
    url_category = (categoriesBook.get(choix_categories_liste[int(choix)], ""))
    return url_category

def main() :
    run = True
    while run == True :
        print("""
        Sommaire : 
            11 => Extraction de tous les livres de toutes les catégories + Tableaux CSV + Dossier JPG
            12 => Extraction de tous les livres de toutes les catégories + Tableaux CSV 
            13 => Extraction de tous les livres de toutes les catégories + Dossier JPG 
            
            21 => Extraction Livres d'une catégories + Tableau CSV + Dossier JPG
            22 => Extraction Livres d'une catégories + Tableau CSV 
            23 => Extraction Livres d'une catégories + Dossier JPG
            
            0 => Sortie du programme
        """)

        action = (input("Que souhaitez vous faire : "))
        try :
            action = int(action)
        except ValueError as e:
            print(f"Merci de saisir un nombre - erreur : {e}")

        if action == 11 :
            extract_all(WEBSITE, launch_csv=True, launch_img=True)
            run = True
        elif action == 12 :
            extract_all(WEBSITE, launch_csv=True, launch_img=False)
            run = True
        elif action == 13 :
            extract_all(WEBSITE, launch_csv=False, launch_img=True)
            run = True

        elif action == 21 :
            url_category = summary_choice2X_extract_books_from_category()
            extract(url_category, launch_csv=True, launch_img=True)
            run = True
        elif action == 22 :
            url_category = summary_choice2X_extract_books_from_category()
            extract(url_category, launch_csv=True, launch_img=False)
            run = True
        elif action == 23 :
            url_category = summary_choice2X_extract_books_from_category()
            extract(url_category, launch_csv=False, launch_img=True)
            run = True
        elif action == 0 :
            run = False
        else :
            run = True

    print("Fin du programme")

if __name__ == "__main__":
    print("Lancement du script scraping pour " + WEBSITE )
    reset_folders()
    main()
else:
    print("Merci d'exécuter le fichier main.py directement")
