# Library Imports
import nextcord, os
from nextcord.ext import commands
from config import TOKEN
import re

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

# Ready message
@bot.event
async def on_ready():
    print(f"{bot.user.name} is now online")

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Shutdown command
@bot.command(description = "Shutdown bot")
@commands.is_owner()
async def shutdown():
    exit()

bot.run(TOKEN)