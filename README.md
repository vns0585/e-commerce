# E-commerce

## О проекте
E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы не реализовали систему платежей, однако готовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Основные возможности
1. На данный момент реализованы 5 классов для работы с продуктами и их категориями.
2. Реализована функция загрузки объектов из json-файла.

## Структура проекта

Основные модули находятся в директории src/: 

- category.py - содержит класс Category
- category_iterator.py - содержит класс CategoryIterator
- lawngrass.py - содержит класс LawnGrass
- product.py - содержит класс Product
- smartphone.py - содержит класс Smartphone
- utils.py - содержит функции для загрузки объектов из json-файла

## Установка и использование

### Требования
- [Python 3.13 или выше](https://www.python.org/downloads/)
- [Poetry 2.0.0 или выше](https://python-poetry.org/docs/#installation) (для управления зависимостями проекта)
- Pytest 9.1.1 или выше (для тестирования)

### Установка
1. Клонируйте репозиторий:

```bash
git clone https://github.com/vns0585/e-commerce.git
cd e-commerce
```

2. Установите зависимости:

```bash
poetry install
```

3. Установите pytest и плагины (для тестирования)
```bash
poetry add --group dev pytest pytest-cov
```
### Использование
Функционал пока дорабатывается. Можно ознакомиться с содержанием файла main.py, находящимся в корне проекта, как с примером использования.

1. Импортируйте нужные модули из проекта
```python
# Для загрузки и создания объектов
from src.utils import load_from_json, create_objects_from_json

# Для работы с классами Product, Category, CategoryIterator, LawnGrass, Smartphone
from src.product import Product
from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone
```
2. Примеры использования функций загрузки из файла
```python
dict_data = load_from_json("путь к вашему json-файлу")
categories = create_objects_from_json(dict_data)
```
3. Примеры использования классов Product и Category
```python
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product.new_product(
    {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }
)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

products_sum = product1 + product2
print(products_sum)

category1 = Category("Смартфоны", 
                     "Смартфоны, как средство не только коммуникации, но и получения дополнительных"
                     " функций для удобства жизни",
                     [product1, product2])

print(category1.name == "Смартфоны")
print(category1.description)
print(len(category1.products))
print(category1.category_count)
print(category1.product_count)

category1.add_product(product3)
print(category1.products)

list_of_products = category1.get_products()
```
4. Примеры использования классов Smartphone и LawnGrass
```python
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                         180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                         98.2, "15", 512, "Gray space")
smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                         90.3, "Note 11", 1024, "Синий")

print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)

grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                   "Россия", "7 дней", "Зеленый")
grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                   "США", "5 дней", "Темно-зеленый")

print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)

smartphone_sum = smartphone1 + smartphone2
print(smartphone_sum)

grass_sum = grass1 + grass2
print(grass_sum)
```

## Тестирование проекта

### Общие принципы

Тестирование в проекте построено на фреймворке pytest.

Основные подходы:

- **Модульность**: каждый модуль приложения тестируется изолированно.

- **Переиспользуемость**: общие настройки и зависимости вынесены в фикстуры.

- **Покрытие сценариев**: проверка как штатных, так и граничных случаев через параметризацию.

### Структура тестов

```text
tests/
├── conftest.py                # Общие фикстуры для всех тестов
├── test_category.py           # Тесты для класса Category
├── test_category_iterator.py  # Тесты для класса CategoryIterator
├── test_lawngrass.py          # Тесты для класса LawnGrass
├── test_product.py            # Тесты для класса Product
├── test_smartphone.py         # Тесты для класса Smartphone
├── utils.py                   # Тесты функций для загрузки из json-файла
└── ...
```

### Запуск тестов
```bash
# Запуск всех тестов
pytest

# Запуск с детализацией
pytest -v

# Запуск конкретного файла
pytest tests/test_category.py

# Генерация отчета о покрытии (с плагином pytest-cov)
pytest --cov=src --cov-report=html
```

### Рекомендации по написанию тестов
- Имена тестов: должны отражать сценарий тестов.

- Изоляция: каждый тест должен быть независимым.

- Параметризация: используйте для проверки множества похожих кейсов, избегая дублирования кода.

- Фикстуры: выносите повторяющиеся настройки в conftest.py, чтобы поддерживать читаемость тестов.

- Ожидаемые исключения: проверяйте ожидаемые ошибки через pytest.raises.

## Лицензия
Этот проект лицензирован по [лицензии MIT](LICENSE).