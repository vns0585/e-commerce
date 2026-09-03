import json

import pytest

from src.category import Category
from src.product import Product


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
