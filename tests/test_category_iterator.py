from src.category import Category
from src.category_iterator import CategoryIterator


def test_category_iterator(first_category: Category) -> None:
    category_iterator = CategoryIterator(first_category)
    i = 0
    for product in category_iterator:
        assert product.name == first_category.get_products()[i].name
        assert product.description == first_category.get_products()[i].description
        assert product.price == first_category.get_products()[i].price
        assert product.quantity == first_category.get_products()[i].quantity
        i += 1
