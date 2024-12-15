import asyncio
from aiogram import Bot, Dispatcher
from bot_token import BOT_TOKEN
from fastapi import FastAPI
from apps.api import router

app = FastAPI()

app.include_router(router)


async def main():
    from apps.handlers import router
    bot = Bot(token=BOT_TOKEN)
    dp=Dispatcher()
    
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())


