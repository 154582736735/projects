import asyncio
from aiogram import Bot, Dispatcher
from project.handlers import router
from project.config import TOKEN
from project.database.models import init_db

async def main():
    await init_db()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("программа завершила выполнение")
