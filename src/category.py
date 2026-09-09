from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {sum([p.quantity for p in self.__products])} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    def get_products(self) -> list[Product]:
        return self.__products

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += str(product) + "\n"
        return products_str
