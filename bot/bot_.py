from aiogram import Bot, Dispatcher, executor, types

from bot import bot_handlers
from dataclasses_ import Config

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await bot_handlers.handle_start(message)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def on_document(message: types.Message):
    await bot_handlers.handle_document(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
