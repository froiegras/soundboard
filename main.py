# Library Imports
import nextcord, os, datetime, pickledb, json, time
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from config import TOKEN
import re

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents = intents)

# Lists
star = []
files = []
reminders = []
leaderboard = []
emotes = {}
msg_counts = {}
msg_time = {}
spam_reply = "I ain't reading all that. I'm sorry for you though or sorry that happened."


# Load folders and files
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Load bot replies from JSON file
with open('message.json', 'r') as reply_file:
    bot_reply = json.load(reply_file)

audiopeg = config.get('audiopeg')
playlist_dir = config.get('playlist_dir')
won = config.get('won')
saed = config.get('saed')
attenddb = config.get('attend')
clockdb = config.get('clock')

if not all([audiopeg, playlist_dir, won, saed, attenddb, clockdb]):
    raise ValueError("One or more paths not found in the configuration file.")

# Databases
attend = pickledb.load(attenddb, True)
clock = pickledb.load(clockdb, True)

# Ready message
@client.event
async def on_ready():
    print("KN Bot is now online")

# Shutdown command
@client.command(description = "Shutdown bot")
@commands.is_owner()
async def shutdown(ctx):
    exit()

# Message detector
@client.event
async def on_message(message):
    for pattern, response in bot_reply.items():
        if re.search(pattern, message):
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
    current_time = time.time()
    if message.author.id in msg_counts:
        msg_counts[message.author.id] += 1
    else:
        msg_counts[message.author.id] = 1
    if len(message.content) > 1000 and not message.author.bot:
        # print('long ass message deteceted') // for debugging
        await message.channel.send(spam_reply)
    if message.author.id in msg_time:
        time_difference = current_time - msg_time[message.author.id]
        if time_difference > 15:  # Adjust the threshold as needed (e.g., 60 seconds)
            msg_counts[message.author.id] = 1  # Reset the consecutive count if too much time has passed
    if msg_counts[message.author.id] % 10 == 0:
        await message.channel.send(spam_reply)
    msg_time[message.author.id] = current_time
    if "lang ako" in message.content.lower() and not message.author.bot:
        index_lang_ako = message.content.lower().find("lang ako")
        substring_before_lang_ako = message.content[:index_lang_ako].strip()
        await message.channel.send(f"no be. don't say that. you're more than just a {substring_before_lang_ako}, be. you are loved. you are valuable. you matter. everytime na maiisip mo na.. \"{substring_before_lang_ako} lang ako 😭\" no. be, you are a wonderful person and we appreciate you so much. i just want you to know na valid ka. hindi biro maging cr . it must've been tough pero you did it. you are so strong kaya sobrang proud kami sayo, be.")
    await client.process_commands(message)

# Process links sent by users and convert them to embeddable links
def process_links(message):
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

# Join command
@client.command(description = "Bot joins the user's current voice channel")
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        # print('Bot has connected') // for debugging
        voice.play(nextcord.FFmpegPCMAudio(executable = "C:/ffmpeg/ffmpeg.exe", source = f"{playlist_dir}/lily.mp3"))
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")
    await ctx.message.delete()

# Leave command
@client.command(descrption = "Bot leaves the current voice channel")
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye bye brother back to the lobby")
    else:
        await ctx.send("U good? ur not even in a voice channel")
    await ctx.message.delete()

# Pause command
@client.command()
async def pause(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No song is playing m8!')

# Resume command
@client.command(description = "Bot resumes playing the paused music/audio")
async def resume(ctx):# Resume command
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('The song is already playing!')

# Stop command
@client.command(description = "Stops the bots from playing music/audio")
async def stop(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    voice.stop()

# Play command
@client.command(description = "Bot plays songs from playlist")
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    song = f'{playlist_dir}/' + arg + '.mp3'
    source = FFmpegPCMAudio(executable = audiopeg, source = song)
    voice.play(source)
    print(f'Now Playing: {arg}')

# Playlist command
@client.command(description = "Shows soundboard playlist")
async def playlist(ctx):
    print(";playlist command has been called")
    for file in playlist_dir:
        f, _ = os.path.splitext(playlist_dir + '/' +  file)
        fname = f.split('/')
        re_name = fname[-1]
        files.append(re_name)
    embed = nextcord.Embed(title = 'Sound List')
    filelist = '\n'.join(files)
    embed.add_field(name = 'List of available sounds', value = filelist)
    await ctx.send(embed = embed)

# Star list command
@client.command(description = "Shows the list of stars of users")
async def stars(ctx):
    users = list(attend.getall())
    sorted_users = sorted(users)
    for i in range(len(sorted_users)):
        leaderboard.append(sorted_users[i])
        star.append(attend.get(sorted_users[i]))
    starlist = '\n'.join(map(str, star)) # fix star
    ldb = '\n'.join(map(str, leaderboard)) # fix star
    embed = nextcord.Embed(title = '⭐ List')
    embed.add_field(name = 'User', value = f"{ldb}")
    embed.add_field(name = '⭐', value = f"{starlist}")
    await ctx.send(embed = embed)

# Clock in command
@client.command(description = "Clock in")
async def clockin(ctx):
    try:
        now = datetime.datetime.now()
        date = [now.year, now.month, now.day]
        hour = now.hour
        minute = now.minute
        second = now.second

        formatted_time = f"{hour:02}:{minute:02}:{second:02}"  # Format time with at least 2 digits

        author = str(ctx.message.author)
        memb = author.split('#')
        user = memb[0]

        if not attend.exists(user):
            attend.set(user, 0)
            clock.set(user, [1997, 1, 1])
            print(f'new user added at {date}')

        if clock.get(user) != date:
            await ctx.reply(f'✅ **Congrats!** {user} has clocked in for today at {formatted_time}. Here have a gold star [⭐]')
            attend.append(user, 1)
            clock.set(user, date)
            if attend.get(user) != 0:
                if attend.get(user) == 7:  # week
                    await ctx.send(f"{user}, you've logged in for a week!")
                elif attend.get(user) == 30:  # month
                    await ctx.send(f"{user}, you've logged in for a month!")
                elif attend.get(user) == 180:  # 6 months
                    await ctx.send(f"{user}, you've logged in for half a year!")
                elif attend.get(user) == 365:  # year
                    await ctx.send(f"{user}, you've logged in for a year!")
            print(f'{user} +1 attendance')
        else:
            await ctx.send(f'{user} has already clocked in for today at {formatted_time}, come back tomorrow!')
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


# Add stars to @user command
@client.command()
@commands.is_owner()
async def adds(ctx):
    uname = str(ctx.message.mentions[0])
    memb = uname.split('#')
    user = memb[0]
    if attend.exists(user):
        attend.append(user, 1)
    print(f'Added +1 to {user}')

# Check attendance command
@client.command(description = "Shows the user's number of stars")
async def attendance(ctx):
    user = str(ctx.message.author.name)
    member = ctx.author
    nickname = member.nick if member.nick else member.name
    accolades = [
        (366, "WELL DONE! YOU HAVE DONE IT {nickname} YOU HAVE BEEN WITH US FOR MORE THAN A YEAR (get a life m8)"),
        (210, "You do know that you're not being paid to do this right, {nickname}?"),
        (183, "WOW! {nickname} MORE THAN 6 MONTHS?? GADDAMN"),
        (150, "~5 months really? {nickname} r u sure ur touching grass?"),
        (120, "almost 4 months now, do u have a life {nickname}?"),
        (101, "Damn {nickname}, you've logged in for more than 100 days"),
        (90, "3 months, r u ok {nickname}?"),
        (60, "2 months wow! {nickname}"),
        (30, "Congrats {nickname}! You've logged in more days than there are in February"),
        (14, "Damn {nickname}, you've logged in for more than 2 weeks?"),
        (7, "Damn {nickname}, you've logged in for more than a week?"),
    ]

    if attend.exists(user):
        days_logged_in = attend.get(user)
        await ctx.reply(f'{nickname} has {days_logged_in} ⭐ ( ﾟ∀ﾟﾉﾉﾞ')

        # Check for accolades based on days_logged_in
        for days, accolade_msg in accolades:
            if days_logged_in >= days:
                await ctx.send(accolade_msg.format(nickname = nickname))
            break
    else:
        await ctx.reply('You haven\'t clocked in a single time? We should fire you.')

client.run(TOKEN)