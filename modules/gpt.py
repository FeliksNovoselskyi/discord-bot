"""
Модуль для роботи з API OpenAI

У цьому модулі прописана логіка взаємодії бота із серверами OpenAI
"""

import openai
import dotenv
import os

# Завантажуємо вміст .env файлу
dotenv.load_dotenv()

# Отримуємо секретний ключ OpenAI з .env файлу
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")

# Об'єкт для взаємодії з клієнтом OpenAI API 
client_openAI = openai.AsyncOpenAI(
    api_key = OPENAI_SECRET_KEY
)

async def get_response_from_chatgpt(question):
    """
    Функція відповідає за формування запиту до серверів OpenAI,
    з метою отримання відповіді, згенерованої на основі ChatGPT
    """

    # Об'єкт response, який зберігає відповідь ChatGPT
    response = await client_openAI.chat.completions.create(
        model = "ft:gpt-4o-mini-2024-07-18:worldit::BFltyNXl", # модель нашого ChatGPT
        messages = [{
            "role": "user", # роль авторо запитання
            "content": question # контент/текст запитання
        }]
    )

    # Повертаємо текст першої відповіді чатбота 
    return response.choices[0].message.content
