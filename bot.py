import asyncio
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ==============================
# ВСТАВ СВІЙ ТОКЕН
# ==============================
TOKEN = "8525083487:AAFRRXMyPJvGKcCPO9ZReBlbKbG39bm3RlQ"

# ==============================
# ДАНІ ГРУПИ
# ==============================
CHAT_ID = -1003714795267
THREADS = [3, 5, 7, 9]

bot = Bot(token=TOKEN)
scheduler = AsyncIOScheduler()


async def send_daily_reminder():
    for thread in THREADS:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="Нагадую за звіти 🐺",
            message_thread_id=thread
        )

    print("Нагадування надіслано")


async def main():
    scheduler.add_job(
        send_daily_reminder,
        trigger="cron",
        hour=19,
        minute=30
    )

    scheduler.start()

    print("Бот запущено. Щоденне нагадування о 19:30.")
    
    # тримаємо бота активним
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
