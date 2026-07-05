import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', '0'))
SECRET_KEY = os.getenv('SECRET_KEY', 'twoj-tajny-klucz-do-flaska-2026')
