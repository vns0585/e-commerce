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


    @classmethod
    def new_product(cls, product_params: dict, products_list=None) -> Product:
        pp_name = product_params.get("name")
        pp_description = product_params.get("description")
        pp_price = product_params.get("price")
        pp_quantity = product_params.get("quantity")

        if isinstance(products_list, list):
            for product in products_list:
                if isinstance(product, Product):
                    if pp_name == product.name:
                        pp_quantity += product.quantity
                        if pp_price < product.__price:
                            pp_price = product.__price

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
            user_answer = input("Вы хотите понизить цену? y/N")
            if user_answer.lower() == "y":
                self.__price = price
        else:
            self.__price = price
        return
