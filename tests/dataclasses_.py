from dataclasses import dataclass


@dataclass
class TestMessages:
    """Тестовые сообщения."""
    START_MESSAGE: str = "Привет! Отправьте мне CSV файл, и я обработаю его."
    NOT_CSV_MESSAGE: str = "Пожалуйста, отправьте CSV файл."


