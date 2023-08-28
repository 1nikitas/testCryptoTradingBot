import io
import os
import tempfile

from aiogram import types

from bot.csv_analyzer.csv_analyzer import CSVAnalyzer, logger


async def handle_start(message: types.Message):
    """Обработчик команды /start."""
    await message.answer("Привет! Отправьте мне CSV файл, и я обработаю его.")


async def handle_document(message: types.Message):
    """Обработчик для документов."""
    if not message.document.mime_type.startswith("text/csv"):
        await message.answer("Пожалуйста, загрузите CSV файл.")
        logger.error("Not a CSV file.")
        return

    temp_file_path = tempfile.mktemp(suffix=".csv")
    await message.document.download(destination_file=temp_file_path)

    try:
        fig = CSVAnalyzer().process_csv(temp_file_path)
        if fig:
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            await message.answer_photo(buffer)
            buffer.close()
    except Exception as e:
        logger.error(f"Error processing file: {e}")

    if os.path.exists(temp_file_path):
        try:
            os.remove(temp_file_path)
        except FileNotFoundError:
            logger.warning(f"File {temp_file_path} not found for deletion.")
