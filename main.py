"""
Головний модуль для запуску Discord бота
"""

from modules import discord, gpt

# 
def main():
    """
    Головна функція, що відповідає за запуск бота
    """

    # 
    discord.bot_client.run(token = discord.TOKEN)

# 
if __name__ == "__main__":
    # 
    main()
