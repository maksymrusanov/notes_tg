import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv

from bot.handlers import router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
