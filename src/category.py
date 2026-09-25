from src.exceptions import ZeroQuantityException
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
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityException("Нельзя добавить продукт с нулевым количеством")
            except ZeroQuantityException as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка добавления продукта завершена")
        else:
            raise TypeError

    def get_products(self) -> list[Product]:
        return self.__products

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += str(product) + "\n"
        return products_str

    def middle_price(self) -> float:
        try:
            return float(sum(product.price for product in self.__products) / len(self.__products))
        except ZeroDivisionError:
            return 0
