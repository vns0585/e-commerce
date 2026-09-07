from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Product 0"
    assert product.description == "Product 0 Description"
    assert product.price == 1000.1
    assert product.quantity == 100


def test_product_set_price(product: Product, capsys: CaptureFixture[str]) -> None:
    product.price = 2000
    assert product.price == 2000
    product.price = -1
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"
    with patch('builtins.input', return_value='y') as mock_input:
        product.price = 1500
        mock_input.assert_called_once_with("Вы хотите понизить цену? y/N ")
        assert product.price == 1500
        message = capsys.readouterr()
        assert message.out == ""


def test_product_new_product(product: Product, new_product_dict_same: dict, new_product_list: list) -> None:
    test_product = product.new_product(new_product_dict_same, new_product_list)
    assert isinstance(test_product, Product)
    assert test_product.name == "Product 1"
    assert test_product.description == "Product 1 Description"
    assert test_product.price == 100
    assert test_product.quantity == 20

    new_product_dict_same["price"] = 1
    test_product.new_product(new_product_dict_same, new_product_list)
    assert isinstance(test_product, Product)
    assert test_product.name == "Product 1"
    assert test_product.description == "Product 1 Description"
    assert test_product.price == 100
    assert test_product.quantity == 20


def test_product_new_product_typeerror(product: Product, new_product_dict_same: dict, new_product_list: list) -> None:
    new_product_dict_same["price"] = "price"
    with pytest.raises(TypeError, match="Цена продукта должна быть числом"):
        product.new_product(new_product_dict_same, new_product_list)
    new_product_dict_same["price"] = 10000
    new_product_dict_same["quantity"] = "quantity"
    with pytest.raises(TypeError, match="Количество продукта должно быть целым числом"):
        product.new_product(new_product_dict_same, new_product_list)
    new_product_dict_same["quantity"] = 10
    new_product_list = [1, 2, 3]
    with pytest.raises(TypeError, match="Продукт должен принадлежать классу Product"):
        product.new_product(new_product_dict_same, new_product_list)
