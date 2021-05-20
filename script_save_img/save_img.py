import urllib.request
import os


def save_img_in_folder(img_by_categories_folder, category, image_url, universal_product_code) :
    category_folder = os.path.join(img_by_categories_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
    urllib.request.urlretrieve(image_url, category_folder + "/" + universal_product_code + ".jpg")