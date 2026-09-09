from src.category import Category
from src.product import Product


def test_category_init(first_category: Category,
                       second_category: Category,
                       first_category_products: str,
                       second_category_products: str) -> None:
    assert first_category.name == "First Category"
    assert first_category.description == "First Category Description"
    assert first_category.products == first_category_products
    assert second_category.name == "Second Category"
    assert second_category.description == "Second Category Description"
    assert second_category.products == second_category_products

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_str(first_category: Category) -> None:
    assert str(first_category) == "First Category, количество продуктов: 45 шт."


def test_category_add_product(product: Product, first_category: Category, first_category_products: str) -> None:
    first_category.add_product(product)
    assert first_category.products == first_category_products + "Product 0, 1000.1 руб. Остаток: 100 шт.\n"
