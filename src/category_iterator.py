from src.category import Category
from src.product import Product


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> 'CategoryIterator':
        self.index = 0
        return self

    def __next__(self) -> Product:
        products = self.category.get_products()
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
