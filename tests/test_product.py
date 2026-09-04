from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Product 0"
    assert product.description == "Product 0 Description"
    assert product.price == 1000.1
    assert product.quantity == 100
