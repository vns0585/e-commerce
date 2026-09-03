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
