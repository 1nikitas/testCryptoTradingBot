import shutil
from pathlib import Path
from unittest.mock import AsyncMock

import pandas as pd
import pytest

from bot.bot_handlers import handle_document
from bot.csv_analyzer.csv_analyzer import CSVAnalyzer
from tests.enums import TestMimeTypes, TestFilePaths, ExpectedValues
from tests.utils import isclose


@pytest.mark.asyncio
async def test_handle_document_with_real_csv():
    """
    Тестирование функции обработки документа с реальным CSV.
    Проверяет, обработает ли функция документ правильно и вызовет ли она необходимые методы.
    """
    message = _mock_message()

    assert Path(TestFilePaths.REAL_CSV).exists(), f"File {TestFilePaths.REAL_CSV} does not exist!"
    message.document.download = _mock_download
    await handle_document(message)
    message.answer_photo.assert_called_once()


def test_calculate_ema():
    """Тестирование функции расчета EMA."""
    series_data = pd.Series(list(range(1, 11)))
    result = CSVAnalyzer()._calculate_ema(series_data, 3)

    assert len(result) == len(series_data)


def test_ema_from_file():
    """Тестирование расчета EMA на основе данных из файла."""
    data = pd.read_csv(TestFilePaths.REAL_CSV)
    ema_calculated = CSVAnalyzer()._calculate_ema(data['PRICE'], 14)

    assert isclose(ema_calculated.iloc[-1], ExpectedValues.EMA_VALUE), \
        f"Expected {ExpectedValues.EMA_VALUE}, but got {ema_calculated.iloc[-1]}"


async def _mock_download(destination_file: str) -> str:
    """Мок функции для скачивания."""
    shutil.copy(TestFilePaths.REAL_CSV, destination_file)
    return destination_file


def _mock_message() -> AsyncMock:
    """Создает мок-объект для сообщения."""
    message = AsyncMock()
    message.document.mime_type = TestMimeTypes.CSV_TEXT.value
    message.document.file_id = "mock_file_id"
    message.document.download = AsyncMock(return_value=TestFilePaths.REAL_CSV)
    message.answer_photo = AsyncMock()
    return message
