"""
Модуль для роботи з API Discord

У цьому модулі прописана логіка взаємодії бота із Discord-сервером
"""

import discord
import os
import dotenv

from .gpt import get_response_from_chatgpt


# завантажуемо вміст файлу .env
dotenv.load_dotenv()

# отримуемо токен нашого дискорд бот
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# об'єкт що задає доступ боту до наших подій дискорду 
intents = discord.Intents.default()

# Доступ боту до читання контенту повідомлень
intents.message_content = True

# Об'єкт боту
bot_client = discord.Client(intents = intents)


@bot_client.event
async def on_ready():
    """
    Функція відпрацьовує, коли бот запущено
    """

    # Повідомлення про запуск боту
    print("Бот запущено")


@bot_client.event
async def on_message(message):
    """
    Функція-подія, що відпрацьовує, коли від користувачів надходить повідомлення
    """

    # Якщо автором повідомлення не є сам бот
    if message.author != bot_client.user:
        # Отримуємо контент повідомлення 
        message_content = message.content
        message_id = message.id

        # отримуємо відповідь від Chatgpt
        response = await get_response_from_chatgpt(message_content)

        # отримаємо повідомлення, з чату на яке треба відповісти, за його id
        message_for_reply = await message.channel.fetch_message(message_id)

        # Надсилаємо у канал повідомлення від імені бота
        await message_for_reply.reply(response)

