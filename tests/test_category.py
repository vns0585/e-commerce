from src.category import Category


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "First Category"
    assert first_category.description == "First Category Description"
    assert len(first_category.products) == 3
    assert second_category.name == "Second Category"
    assert second_category.description == "Second Category Description"
    assert len(second_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
