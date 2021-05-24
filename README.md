# OCR_P2 - Projet P2 -  Scraping du site http://books.toscrape.com
***
## Présentation
Le script a été conçu pour détecter l'ensemble des catégories de livres présentes sur le site http://books.toscrape.com.
Une extraction de l'ensemble des livres présents dans une même catégorie sera réalisée puis une compilation en fichier CSV sera exécutée avec l'ensemble des informations caractéristiques de chaque livre. Une sauvegarde de toutes les couvertures de livres au format .JPG est prévue dans le programme.

***
## Installation d'un environnement virtuel ainsi que les dépendances associées pour l'exécution du programme :  
<br/>

### Pour MAC/linux
création de l'environnement virtuel<br/>

        $ python3 -m venv [nom_de_votre_environnement_virtuel] 

activation de l'environnement virtuel <br/>

        $ source [nom_de_votre_environnement_virtuel]/bin/activate
        
Clonage Repository depuis dépot GitHub<br/>

        $ git clone https://github.com/Litibe/OCR_P2.git

Aller dans le dossier OCR_P2 contenant les fichiers<br/>

        $ cd OCR_P2 
        
Installation des packages nécessaires en utilisant Pip (requests, lxml, BeautifulSoup4)<br/>

        $ pip install -r requirements.txt 
        
Exécution du Programme via le fichier principal : main.py<br/>

        $ python3 main.py 

### Pour windows 
création de l'environnement virtuel<br/>

        $ python3 -m venv [nom_de_votre_environnement_virtuel] 

activation de l'environnement virtuel <br/>

        $ source [nom_de_votre_environnement_virtuel]\Scripts\activate
        
Clonage Repository depuis dépot GitHub<br/>

        $ git clone https://github.com/Litibe/OCR_P2.git

Aller dans le dossier OCR_P2 contenant les fichiers<br/>

        $ cd OCR_P2 
        
Installation des packages nécessaires en utilisant Pip (requests, lxml, BeautifulSoup4)<br/>

        $ pip install -r requirements.txt 
        

***
## Lancement du programme : 
Exécution du Programme via le fichier principal : main.py présent dans le dossier OCR_P2 <br/>

        $ python3 main.py 


Le programme d'un interface dans le terminal pour laisser à l'utilisateur le choix dans son extraction : <br/>

        
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

 <br/>
Le programme laisse le choix à l'utilisateur, d'extraire les livres présents dans une catégorie précises ou de toutes les catégories présentes sur le sitehttp://book.toscrape.com/. <br/>
Lors de l'extraction, le programme affiche quel livre est extrait ainsi que son adresse URL pour un accès rapide pour l'utilisateur. <br/>
On peut egalement enregistrer les extractions des catégories sous forme de récapitulatif au format CSV. Voici les données extraites pour chaque livre : 
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
Le programme dispose de la fonctionnalité d'enregistrer des images de couvertures des livres, les enregistrant ainsi sous la référence code UPC du livre (exemple : "universal_ product_code".jpg) dans un dossier au nom de la catégorie auquel appartient le livre. <br/>
 <br/>
 Le programme va créé dans le dossier "OCR_P2", un dossier "Resultat_extraction" contenant les données extraites du site. Le dossier comprenant un dossier regroupant les export CSV ("Fichiers CSV") et un autre dossier contenant les export Image au format JPG ("Fichiers IMG par catégorie").
 
 !! ATTENTION, à chaque lancement du programme, ce dernier efface les résultats d'extractions obtenus précédement (= reset). Par contre, tant que le script est ouvert, on peut additionner le résultat de ses extractions (exemple : on peut extraire plusieurs catégories de livres, qui seront regroupés dans le même dossier "résultat_extraction")

## Extraction des informations d'un seul livre manuellement : 
Vous pouvez extraire manuellement les informations d'un seul livre en exécutant un fichier précis du programme au lieu du main.py principal : 
Exécution du Fichier : extract_info_book.py présent dans le dossier scripts_for_BeautifulSoup <br/>

        $ python3 scripts_for_BeautifulSoup/extract_info_book.py
        
        Exécution du script pour les renseignement d'un seul livre
	 exemple url livre : http://books.toscrape.com/catalogue/sharp-objects_997/index.html 
        Merci de saisir l'url du livre dont vous souhaitez extraire les informations :

