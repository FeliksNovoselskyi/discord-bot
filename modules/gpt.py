"""
Модуль для роботи з API OpenAI

У цьому модулі прописана логіка взаємодії бота із серверами OpenAI
"""

import openai
import dotenv
import os
import io

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


async def get_image_from_dalle(prompt):
    """
    Функція відповідає за формування запиту до серверів OpenAI
    з метою отримання зображення, згенерованого за допомогою DALL-E
    """

    # Отримуємо згенеровану зображення
    response = await client_openAI.images.generate(
        model="dall-e-2", # Модель для генерації зображення
        prompt=prompt, # Завдання для генерації зображення
        size="1024x1024", # Розміри зображення
        quality="standard" # Якість зображення
    )

    # Повертаємо посилання на зображення
    return response.data[0].url


async def get_voice_from_tts(input):
    """
    Функція відповідає за повернення аудіофайлу з озвученим текстом від користувача
    """

    # tts - text to speech

    # Отримуємо у відповідь згенерований аудіофайл
    response = await client_openAI.audio.speech.create(
        model="gpt-4o-mini-tts", # Модель для генерації аудіофайлу
        voice="coral", # Голос аудіофайлу
        input=input # Текст для озвучування
    )

    # Зберігаємо аудіофайл в оперативній пам'яті
    audio_file = io.BytesIO(response.content)

    # Повертаємо аудіофайл
    return audio_file