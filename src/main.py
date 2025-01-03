import asyncio, requests

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import json



token = ''
API = ''

bot = Bot(token)

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, напиши назву свого міста!")


@dp.message(F.text)
async def get_weathere(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        symbols = ("☀️", "⛅", "❄️")
        current_temp = ""
        if temp > 5.0:
            current_temp = symbols[0]
        elif temp < 0:
            current_temp = symbols[2]
        elif temp != 5.0:
            current_temp = symbols[1]
        
        await message.reply(text=f"Зараз погода: {temp} {current_temp}")
    else:
        await message.reply(text="Місто вказано невірно")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())