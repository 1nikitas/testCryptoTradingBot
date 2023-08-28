from enum import Enum


class TestMimeTypes(Enum):
    """Типы MIME для тестов."""
    PLAIN_TEXT = "text/plain"
    CSV_TEXT = "text/csv"


class TestFilePaths:
    """Пути к файлам для тестирования."""
    REAL_CSV = 'files/prices.csv'


class ExpectedValues:
    """Ожидаемые значения для тестирования."""
    EMA_VALUE = 1875.366233