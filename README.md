# OCR_P2 - Projet P2 -  Scraping du site [http://books.toscrape.com](http://books.toscrape.com)
***
## Présentation
![project status](https://img.shields.io/pypi/status/ansicolortags.svg)

Le script a été conçu pour détecter l'ensemble des catégories de livres présentes sur le site http://books.toscrape.com.
Une extraction de l'ensemble des livres présents dans une même catégorie sera réalisée puis une compilation en fichier CSV pour la catégorie sera possible. Une sauvegarde de toutes les couvertures de livres au format .JPG est également possible.
<br/><br/>
Le programme laisse le choix à l'utilisateur, d'extraire les livres présents dans une catégorie précises ou de toutes les catégories présentes sur le site. <br/>
Lors de l'extraction, le programme affiche quel livre est extrait ainsi que son adresse URL pour un accès rapide pour l'utilisateur. <br/>
Voici les données extraites pour chaque livre : 
````text
product_page_url (adresse http du livre)
universal_ product_code (upc)
title 
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating 
image_url
````
Le programme peut enregistrer les couvertures de chaque livre, enregistrant ainsi les images .JPG sous la référence code UPC du livre (exemple : "universal_ product_code".jpg) dans un dossier au nom de la catégorie auquel appartient le livre. <br/>

***
## Prérequis : 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python badge](https://img.shields.io/badge/Python->=3.6-blue.svg)](https://www.python.org/)
***
## Clonage du Repository :
````shell
git clone https://github.com/Litibe/OCR_P2.git
````
***
## Environnement Virtuel :
création de l'environnement virtuel
```shell
python3 -m venv [nom_de_votre_environnement_virtuel] 
```
activation de l'environnement virtuel
### Mac/Linux
````shell
source [nom_de_votre_environnement_virtuel]/bin/activate
````
### Windows
````shell
source .\[nom_de_votre_environnement_virtuel]\Scripts\activate
````

Aller dans le dossier OCR_P2 contenant les fichiers
```shell
cd OCR_P2 
```
***
## Installation des packages nécessaires
````shell
pip install -r requirements.txt 
````
***
## Lancement du programme : 
Exécution du Programme via le fichier principal : main.py présent dans le dossier OCR_P2
````shell
python3 main.py 
````
Cette commande produit le resultat suivant car le programme dispose d'une interface dans le terminal pour laisser à l'utilisateur le choix dans son extraction :

```shell
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
```

Le choix N°11 dure environ une quinzaine de minutes d'exécution.

***
## Résultats du programme : 
Le programme va créer dans le dossier "OCR_P2", un dossier "Resultat_extraction" contenant les données extraites du site. Le dossier comprenant un dossier regroupant les export CSV ("Fichiers CSV") et un autre dossier contenant les export Image au format JPG ("Fichiers IMG par catégorie").
 
**!! ATTENTION !!** A chaque lancement du programme, ce dernier efface les résultats d'extractions obtenus précédement (= reset). Par contre, tant que le script est ouvert, on peut additionner le résultat de ses extractions (exemple : on peut extraire plusieurs catégories de livres, qui seront regroupés dans le même dossier "résultat_extraction")
