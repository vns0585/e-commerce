class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_params: dict, products_list: list = []) -> 'Product':
        pp_name = str(product_params.get("name"))
        pp_description = str(product_params.get("description"))
        pp_price = product_params.get("price")
        if isinstance(pp_price, (float, int)):
            pp_price = float(pp_price)
        else:
            raise TypeError("Цена продукта должна быть числом")
        pp_quantity = product_params.get("quantity")
        if not isinstance(pp_quantity, int):
            raise TypeError("Количество продукта должно быть целым числом")

        if len(products_list) > 0:
            for product in products_list:
                if isinstance(product, Product):
                    if pp_name == product.name and isinstance(pp_quantity, int):
                        pp_quantity += product.quantity
                        if pp_price < product.__price:
                            pp_price = product.__price
                else:
                    raise TypeError("Продукт должен принадлежать классу Product")

        return cls(pp_name, pp_description, pp_price, pp_quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.__price:
            user_answer = input("Вы хотите понизить цену? y/N ")
            if user_answer.lower() == "y":
                self.__price = price
        else:
            self.__price = price
        return
