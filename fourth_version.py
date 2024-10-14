from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7216240691:AAGQus0Z0NqcbLy5USkpAFDkm3R5V1cTD68'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

buttons: list[KeyboardButton] = []
keyboard: list[list[KeyboardButton]] = []

# Заполняем список списками с кнопками
for i in range(1, 1201):
    buttons.append(KeyboardButton(text=str(i)))
    if not i % 12:
        keyboard.append(buttons)
        buttons = []

# Создаем объект клавиатуры, добавляя в него список списков с кнопками
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Четвёртый вариант расположение кнопок',
        reply_markup=my_keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)