# OCR_P2 - Projet P2 -  Scraping du site http://books.toscrape.com
***
## Présentation
Le script a été conçu pour détecter l'ensemble des catégories de livres présentes sur le site http://books.toscrape.com.
Une extraction de l'ensemble des livres présents dans une même catégorie sera réalisée puis une compilation en fichier CSV sera éxecutée avec l'ensemble des informations caractéristiques de chaque livre.

Voici les données extraites pour chaque livre : 
<br/>
product_page_url <br/>
universal_ product_code (upc) <br/>
title <br/>
price_including_tax <br/>
price_excluding_tax <br/>
number_available <br/>
product_description <br/>
category <br/>
review_rating <br/>
image_url <br/>
<br/>

***
## Installation d'un environnement virtuel ainsi que les dépendances associées pour l'exécution du programme :  
<br/>
### MAC
création de l'environnement virtuel
$ python3 -m venv [nom_de_votre_environnement_virtuel] <br/>
activation de l'environnement virtuel
$ source [nom_de_votre_environnement_virtuel]/bin/activate <br/>
récupération des fichiers sources du script depuis dépot GitHub
$ git clone https://github.com/Litibe/OCR_P2.git <br/>
Aller dans le dossier OCR_P2 contenant les fichiers
$ cd OCR_P2 <br/>
Installation des packages nécessaires (requests, lxml, BeautifulSoup4 = bs4)
$ pip install -r requirements.txt <br/>
Exécution du Programme via le fichier principal : main.py
$ python3 main.py <br/>

### Pour windows replacer [nom_de_votre_environnement_virtuel]/bin/ PAR  [nom_de_votre_environnement_virtuel]\Scripts\activate)

***
## Lancement du programme : 
Le programme d'un interface dans le terminal pour laisser à l'utilisateur le choix dans son extraction : <br/>
"""
        Lancement du script scraping pour http://books.toscrape.com/

        Sommaire : 
            11 => Extraction de tous les livres de toutes les catégories + Tableaux CSV + Dossier JPG
            12 => Extraction de tous les livres de toutes les catégories + Tableaux CSV
            13 => Extraction de tous les livres de toutes les catégories + Dossier JPG 
            
            21 => Extraction Livres d'une catégories + Tableau CSV + Dossier JPG
            22 => Extraction Livres d'une catégories + Tableau CSV 
            23 => Extraction Livres d'une catégories + Dossier JPG
            
            0 => Sortie du programme
        
        Que souhaitez vous faire : 
"""
 <br/>
Le programme laisse le choix à l'utilisateur, d'extraire tout ou une partie des livres présents dans une catégorie, depuis le site. <br/>
Lors de l'extraction, le programme affiche quel livre il est en train de traiter ainsi que son adresse URL pour un accès rapide. <br/>
On peut egalement enregistrer les extractions des catégories sous forme de récapitulatif au format CSV. <br/>
Le programme dispose de la fonctionnalité d'enregistrer des images de couvertures des livres, les enregistrant ainsi sous la référence code UPC du livre (exemple : "universal_ product_code".jpg) dans un dossier au nom de la catégorie auquel appartient le livre. <br/>
 <br/>
 Le programme va créé dans le dossier "OCR_P2", un dossier "Resultat_extraction" contenant les données extraites du site. Le dossier comprenant un dossier regroupant les export CSV ("Fichiers CSV") et un autre dossier contenant les export Image au format JPG ("Fichiers IMG par catégorie").
 
 !! ATTENTION, à chaque lancement du programme, ce dernier efface les résultats d'extractions obtenus précédement (= reset). Par contre, tant que le script est ouvert, on peut additionner le résultat de ses extractions (exemple : on peut extraire plusieurs catégories de livres, qui seront regroupés dans le même dossier "résultat_extraction")

## 
