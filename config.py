import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PLAYLIST_DIR = os.getenv("PLAYLIST_DIR")
FFMPEG_LOCATION = os.getenv("FFMPEG_LOCATION")
WON_LOC = os.getenv("WON_LOC")
SAED_LOC = os.getenv("SAED_LOC")
MONGO_URI = os.getenv("MONGO_URI")
TIMEZONE = os.getenv("TIMEZONE", "Asia/Manila")
BIRTHDAY_CHANNEL_ID = int(os.getenv("BIRTHDAY_CHANNEL_ID", 0))

DATABASE_URL = os.getenv("DATABASE_URL")