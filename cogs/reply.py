import re
import os
import json
import time
import nextcord

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Load bot replies from JSON file
with open('message.json', encoding="utf8") as reply_file:
    bot_reply = json.load(reply_file)

msg_counts = {}
msg_time = {}
spam_reply = "I ain't reading all that. I'm sorry for you though or sorry that happened."

won = os.getenv('WON_LOC')
saed = os.getenv('SAED_LOC')

class Reply(commands.Cog):
    """ A cog for handling replies to specific messages and patterns """
    def __init__(self, bot):
        self.bot = bot

    # Message detector
    @commands.Cog.listener()
    async def on_message(self, message):
        for pattern, response in bot_reply.items():
            if re.search(pattern, message.content) and not message.author.bot:
                await message.channel.send(response)
        if message.content.lower() == 'wonyoung':
            # print('wonyoungg detected') // for debugging
            vid = nextcord.File(won)
            await message.channel.send(file = vid)
        if message.content.lower() == 'sad':
            vid = nextcord.File(saed)
            await message.channel.send(file = vid)
        if message.content.lower() == "sus":
            # print("amogus detected") // for debugging
            await message.channel.send("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        if ".com/" in message.content.lower() and not message.author.bot:
            # print('link detected') // for debugging
            new_link = process_links(message)
            await message.channel.send(new_link)
        if long_message_detector(message):
            return spam_reply
        if "lang ako" in message.content.lower() and not message.author.bot:
            index_lang_ako = message.content.lower().find("lang ako")
            substring_before_lang_ako = message.content[:index_lang_ako].strip()
            await message.channel.send(
                f"""
                no be. don't say that. you're more than just a {substring_before_lang_ako}, be.
                you are loved. you are valuable. you matter. everytime na maiisip mo na..
                \" lang ako 😭\" no. be, you are a wonderful person
                and we appreciate you so much. i just want you to know na valid ka. hindi biro
                maging {substring_before_lang_ako} . it must've been tough pero you did it. you are so strong kaya
                sobrang proud kami sayo, be.
                """
            )
        await self.bot.process_commands(message)

def long_message_detector(message):
    """ Detect if a message is too long or if a user is spamming """
    current_time = time.time()
    if message.author.id in msg_counts:
        msg_counts[message.author.id] += 1
    else:
        msg_counts[message.author.id] = 1
    if len(message.content) > 1000 and not message.author.bot:
        return True
    if message.author.id in msg_time:
        time_difference = current_time - msg_time[message.author.id]
        if time_difference > 15:  # Adjust the threshold as needed (e.g., 60 seconds)
            msg_counts[message.author.id] = 1  # Reset the consecutive count after some time
    if msg_counts[message.author.id] % 10 == 0:
        return True
    msg_time[message.author.id] = current_time

def process_links(message):
    """ Process links sent by users and convert them to embeddable links """
    content = message.content.lower()
    author_is_bot = message.author.bot

    match True:
        case _ if 'instagram.com/' in content:
            if not author_is_bot and 'ddinstagram.com' not in content:
                parts = message.content.split('instagram.com')
                modified_link = parts[0] + 'ddinstagram.com' + parts[1]
                return modified_link
        case _ if 'tiktok.com/' in content:
            if not author_is_bot and 'vxtiktok.com' not in content:
                parts = message.content.split('tiktok.com')
                modified_link = parts[0] + 'vxtiktok.com' + parts[1]
                return modified_link
        case _ if 'twitter.com/' in content or 'x.com/' in content:
            if not author_is_bot and 'vxtwitter.com' not in content:
                modified_link = message.content.replace('twitter.com', 'vxtwitter.com').replace('x.com', 'vxtwitter.com')
                return modified_link
    return message.content

def setup(bot):
    """ Setup function to add the Reply cog to the bot """
    bot.add_cog(Reply(bot))
