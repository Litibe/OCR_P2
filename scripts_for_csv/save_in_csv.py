import csv
import os

def save_in_csv_file(files_csv_folder,category, data_to_write_for_csv):
    file_csv = os.path.join(files_csv_folder, (str(category) + ".csv"))
    with open(file_csv, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["product_page_url", "universal_product_code", "title", "price_including_tax",
                                     "price_excluding_tax", "number_available", "product_description", "category",
                                     "review_rating", "image_url"])
            for book in data_to_write_for_csv:
                writer.writerow(book)