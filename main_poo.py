# coding: utf-8

import csv
import os
import shutil
import urllib.request
import requests
from bs4 import BeautifulSoup

website = "http://books.toscrape.com/"


def init_folders_results():
    current_dir = os.path.dirname(__file__)
    dossier_extraction = os.path.join(current_dir, "resultat_extraction")
    dossier_img_categories = os.path.join(dossier_extraction, "Fichiers IMG par catégorie")
    dossier_fichiers_csv = os.path.join(dossier_extraction, "Fichiers CSV")
    if os.path.exists(dossier_extraction):
        try:
            shutil.rmtree(dossier_extraction)
        except OSError as e:
            print(f"Error:{e.strerror}")
    os.makedirs(dossier_extraction)
    os.makedirs(dossier_fichiers_csv)
    os.makedirs(dossier_img_categories)


def extract_categories_books(website):
    try:
        response = requests.get(website)
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
            link = website + a["href"]

            # extraction du nom de la categorie
            for content in a.contents:
                """ Modification String title car sinon : 
                '\n                            \n                                Health\n                            \n                        '
                """
                title = content.split("\n")
                title = title[2].strip("  ")
                categoriesBook[title] = link
        for name_category_book, url_category_book in categoriesBook.items():
            name_category_book = CategoryBook(name_category_book, url_category_book)

class CategoriesBook:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class CategoryBook(CategoriesBook):
    def __init__(self, name, url):
        CategoriesBook.__init__(self, name, url)

    def __str__(self):
        return f"La catégorie {self.name} est accessible via : {self.url}"


def main():
    init_folders_results()
    extract_categories_books(website)

