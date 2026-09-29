import pytest
from _pytest.capture import CaptureFixture

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


def test_category_add_product_typeerror(first_category: Category) -> None:
    with pytest.raises(TypeError):
        first_category.add_product(1)  # type: ignore


def test_category_middle_price(first_category: Category, category_without_products: Category) -> None:
    assert round(first_category.middle_price(), 2) == 150.17
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys: CaptureFixture[str], first_category: Category) -> None:
    assert len(first_category.get_products()) == 3
    product = Product(name="Product 0", description="Product 0 Description", price=1000.1, quantity=1)
    first_category.add_product(product)
    assert len(first_category.get_products()) == 4
    message = capsys.readouterr().out
    assert message.strip().split("\n")[-2] == "Продукт добавлен успешно"
    assert message.strip().split("\n")[-1] == "Обработка добавления продукта завершена"
    product.quantity = 0
    first_category.add_product(product)
    message = capsys.readouterr().out
    assert message.strip().split("\n")[-2] == "Нельзя добавить продукт с нулевым количеством"
    assert message.strip().split("\n")[-1] == "Обработка добавления продукта завершена"
