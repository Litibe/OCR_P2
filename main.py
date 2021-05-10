from bs_scripts.bsCategoriesBooks import extract_categories_books as extract_categories_books

def main() :
    categoriesBook = extract_categories_books()
    if isinstance(categoriesBook, dict) :
        print(categoriesBook)
    else :
        print(categoriesBook)
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