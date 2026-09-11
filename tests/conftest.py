import json

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="First Category",
        description="First Category Description",
        products=[
            Product("Product 1", description="Product 1 Description", price=100, quantity=10),
            Product("Product 2", description="Product 2 Description", price=200, quantity=20),
            Product("Product 3", description="Product 3 Description", price=150.50, quantity=15)
        ]
    )


@pytest.fixture
def first_category_products() -> str:
    return ("Product 1, 100 руб. Остаток: 10 шт.\nProduct 2, 200 руб. Остаток: 20 шт.\nProduct 3, 150.5 руб. Остаток:"
            " 15 шт.\n")


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Second Category",
        description="Second Category Description",
        products=[
            Product("First Product", description="First Product Description", price=400, quantity=12),
            Product("Second Product", description="Second Product Description", price=800.95, quantity=3)
        ]
    )


@pytest.fixture
def second_category_products() -> str:
    return "First Product, 400 руб. Остаток: 12 шт.\nSecond Product, 800.95 руб. Остаток: 3 шт.\n"


@pytest.fixture
def product() -> Product:
    return Product(
        name="Product 0",
        description="Product 0 Description",
        price=1000.1,
        quantity=100
    )


utils_data = [
    {
        'name': 'Смартфоны',
        'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций'
                       ' для удобства жизни',
        'products':
            [
                {
                    'name': 'Samsung Galaxy C23 Ultra',
                    'description': '256GB, Серый цвет, 200MP камера',
                    'price': 180000.0,
                    'quantity': 5
                },
                {
                    'name': 'Iphone 15',
                    'description': '512GB, Gray space',
                    'price': 210000.0,
                    'quantity': 8
                },
                {
                    'name': 'Xiaomi Redmi Note 11',
                    'description': '1024GB, Синий',
                    'price': 31000.0,
                    'quantity': 14
                }
            ]
    },
    {
        'name': 'Телевизоры',
        'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и'
                       ' помощником',
        'products':
            [
                {
                    'name': '55" QLED 4K',
                    'description': 'Фоновая подсветка',
                    'price': 123000.0,
                    'quantity': 7
                }
            ]
    }

]


@pytest.fixture
def utils_json_data() -> str:
    return json.dumps(utils_data)


@pytest.fixture
def utils_load_from_json_result() -> list:
    return utils_data


@pytest.fixture
def new_product_dict_same() -> dict:
    return {
        "name": "Product 1",
        "description": "Product 1 Description",
        "price": 100,
        "quantity": 10
    }


@pytest.fixture
def new_product_list() -> list:
    return [
        Product("Product 1", description="Product 1 Description", price=100, quantity=10),
        Product("Product 2", description="Product 2 Description", price=200, quantity=20),
        Product("Product 3", description="Product 3 Description", price=150.50, quantity=15)
    ]


@pytest.fixture
def smartphone1() -> Smartphone:
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")
