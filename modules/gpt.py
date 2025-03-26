"""
Модуль для роботи з API OpenAI

У цьому модулі прописана логіка взаємодії бота із серверами OpenAI
"""

import openai
import dotenv
import os

# 
dotenv.load_dotenv()

# 
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")

# 
client_openAI = openai.AsyncOpenAI(
    api_key = OPENAI_SECRET_KEY
)

async def get_response_from_chatgpt(question):
    """
    Функція відповідає за формування запиту до серверів OpenAI,
    з метою отримання відповіді, згенерованої на основі ChatGPT
    """

    # 
    response = await client_openAI.chat.completions.create(
        model = "gpt-4o-mini", #
        messages = [{
            "role": "user", #
            "content": question #
        }]
    )

    # 
    return response.choices[0].message.content
