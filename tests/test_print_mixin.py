from _pytest.capture import CaptureFixture

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys: CaptureFixture[str]) -> None:
    Product("Product 1", description="Product 1 Description", price=100, quantity=10)
    message = capsys.readouterr().out.rstrip()
    assert message == "Product(Product 1, Product 1 Description, 100, 10)"
    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
               5, 95.5, "S23 Ultra", 256, "Серый")
    message = capsys.readouterr().out.rstrip()
    assert message == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
              "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr().out.rstrip()
    assert message == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
