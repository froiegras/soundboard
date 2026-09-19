import os
import nextcord
import motor.motor_asyncio

from config import MONGO_URI
from nextcord.ext import commands
from dotenv import load_dotenv

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

bot.db_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
bot.db = bot.db_client["soundboard"]

load_dotenv()

# Bot start log
@bot.event
async def on_ready():
    """ This function is called when the bot is ready and online. """
    print(f"{bot.user.name} is now online")

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Shutdown command
@bot.command(description = "Shutdown bot")
@commands.is_owner()
async def shutdown():
    """ Shuts down the bot. Only the owner can use this command. """
    exit()

bot.run(os.getenv('TOKEN'))