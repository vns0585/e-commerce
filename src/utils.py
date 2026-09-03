import json
import os

from src.category import Category
from src.product import Product


def load_from_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        return {}
    return data


def create_objects_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
