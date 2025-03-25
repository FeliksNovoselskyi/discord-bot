"""
Модуль для роботи з API Discord

У цьому модулі прописана логіка взаємодії бота із Discord-сервером
"""

import discord
import os
import dotenv

# 
dotenv.load_dotenv()

# 
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# 
intents = discord.Intents.default()

# 
intents.message_content = True

# 
bot_client = discord.Client(intents = intents)


@bot_client.event
async def on_ready():
    """
    Функція відпрацьовує, коли бот запущено
    """

    # 
    print("Бот запущено")


@bot_client.event
async def on_message(message):
    """
    Функція-подія, що відпрацьовує, коли від користувачів надходить повідомлення
    """

    # 
    if message.author != bot_client.user:
        # 
        message_content = message.content

        # 
        await message.channel.send(message_content)

