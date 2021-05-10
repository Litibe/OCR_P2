from bs_scripts.bsCategoriesBooks import extract_categories_books as extract_categories_books
from bs_scripts.bsBooksInCategorie import extractBooksFromCategorie as extractBooksFromCategorie
def main() :
    categoriesBook = extract_categories_books()
    if isinstance(categoriesBook, dict) :
        for categorie, urlCategorie in categoriesBook.items() :
            urlBooksInCategorie = extractBooksFromCategorie(urlCategorie)
            print("la Catégorie ", categorie, "contient ", len(urlBooksInCategorie), "livres")
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