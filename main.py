# Library Imports
import nextcord, os, re, urllib, pytube, asyncio, datetime, pickledb, requests, random, instaloader
from nextcord.utils import get
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from config import TOKEN, spotify_client_secret, spotify_client_id

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents = intents)

# Lists
star = []
files = []
leaderboard = []
emotes = {}

# Files and Folders
audiopeg = "C:/ffmpeg/ffmpeg.exe"
folder = r'C:/Users/a/Documents/GitHub/discord bot/sound' # Soundbite directories
won = r'C:/Users/a/Documents/GitHub/soundboard/wonbonk.mp4' # Video variable
dir = os.listdir(folder)

# Databases
attend = pickledb.load('C:/Users/a/Documents/GitHub/discord bot/db/attend.db', True)
clock = pickledb.load('C:/Users/a/Documents/GitHub/discord bot/db/clock.db', True)

# Spotify API (not used)
# spotify_client_credentials = SpotifyClientCredentials(client_id = spotify_client_id, client_secret = spotify_client_secret)
# spotify = spotipy.Spotify(client_credentials_manager=spotify_client_credentials)

# Ready message
@client.event
async def on_ready():
    print("Soundboard is now online")

# Shutdown command
@client.command(description = "Shutdown bot")
@commands.is_owner()
async def shutdown(ctx): # Shutdown command
    exit()

# Message detector
@client.event
async def on_message(message):
    if "valorant" in message.content.lower() or "valo" in message.content.lower():
        print('valorant detected')
        await message.channel.send("https://media.giphy.com/media/uBRwFMpdukW1hf8yqS/giphy.gif")
    if message.content.lower() in ['apex', 'apex legend', 'ape sex']:
        print('apex detected')
        await message.channel.send("https://media.giphy.com/media/U3stv4FYyWQ6XddMBf/giphy.gif")
    if message.content.lower() in ['league', 'lol', 'league of legends']:
        print('league detected')
        await message.channel.send("https://media.giphy.com/media/OjPLhlq1wubJ8D8uP3/giphy.gif")
    if message.content.lower() in ['dying light']:
        print('dying light detected')
        await message.channel.send("https://tenor.com/btPFC.gif")
    if message.content.lower() in ['divinity']:
        print('divinity detected')
        await message.channel.send("https://tenor.com/bDkIX.gif")
    if message.content.lower() in ['euro', 'convoy', 'truck', 'ets2']:
        print('ets2 detected')
        await message.channel.send("https://tenor.com/blduy.gif")
    if message.content.lower() in ['genshin', 'genshin impact']:
        print('genshin detected')
        await message.channel.send("https://media.giphy.com/media/mKHOtvOT8ljlkr3Tsi/giphy.gif")
    if message.content.lower() == 'wonyoung':
        print('wonyoungg detected')
        vid = nextcord.File(won)
        await message.channel.send(file = vid)
    if message.content.lower() == 'no':
        print("no detected")
        await message.channel.send("https://media.giphy.com/media/fXnRObM8Q0RkOmR5nf/giphy.gif")
    if message.content.lower() in ['dream', 'desire', 'sandman']:
        print("sandman boi detected")
        await message.channel.send("https://cdn.discordapp.com/attachments/766470595109453846/1017097797167755274/SPOILER_unknown.png")
    if message.content.lower() == 'why god':
        print("cringe detected")
        await message.channel.send("https://media.discordapp.net/attachments/819083097395167244/1102759213484216431/20230423_100533.jpg")
    if message.content.lower() == "i dont forgive":
        print("no forgiven detected")
        await message.channel.send("https://media.discordapp.net/attachments/819083097395167244/1102759125668069406/20230425_131535.jpg")
    if message.content.lower() == "iou":
        print("i owe u detected")
        await message.channel.send("https://media.discordapp.net/attachments/819083097395167244/1103502798030639175/images.jpg")
    if message.content.lower() in ['honkai', 'honkai impact 3', 'hi3']:
        print("honkai detected")
        await message.channel.send("https://tenor.com/bJcM6.gif")
    if message.content.lower() == "sus":
        print("amogus detected")
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
    if message.content.lower() == "server sucks":
        print("ahole detected")
        await message.channel.send("You know what? I'm just going to say it. This server fucking sucks. I don't give a shit if the admins will mute me or if I get banned, but I want to get my message across, because it amazes me how many idiots in this server have a poor taste in quality. This server is like a fucking mental ward, and you all need to seek help. It's always the same damn shit everyday, and nothing new ever comes out of anyone's shriveled brains. Where are all the dank memes? Where are all of the good jokes? Where is all the dark humour? All I see is the same fucking Tumblr screenshots, and it's honestly boring as fuck. ALL of you are boring as fuck, if I'm being frank. I have pity for your parents, because I wouldn't question how would I able to nurture someone so milquetoast and ignorant for 18 years without putting a bullet through my head. You're all lame as fuck. I feel more stupider interacting with you all, and I wouldn't want to spend another second in this toxic atmosphere. Hell I'm actually glad this group exists. It keeps all the unfunny pricks away from the server that appreciate quality in their content. I hope you all get drafted and never come back. I'm done with you assholes.")
    if "joever" in message.content.lower() or "jover" in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/766470595109453846/1122505985009926215/20230519_111854.jpg")
    if "bozo" in message.content.lower():
        await message.channel.send("https://tenor.com/bJpmN.gif")
    if 'crazy' in message.content.lower() and not message.author.bot:
        await message.channel.send("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room filled with rats. And rats make me crazy. Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room filled with rats. And rats make me crazy.")
    if 'instagram.com/' in message.content.lower():  #Check if the message contains an Instagram link
        print('Instagram link detected')
        if not message.author.bot: # Check if the message is from a user (not a bot)
            if 'ddinstagram.com' in message.content.lower():
                print('Already embedded')
            elif 'instagram.com' in message.content: # Check if the message contains an Instagram link
                await message.edit(suppress = True) # Remove embed rom previous message
                parts = message.content.split('instagram.com') # Split the message content by 'instagram.com'
                modified_link = parts[0] + 'ddinstagram.com' + parts[1] # Insert 'dd' between 'www.' and 'instagram.com'
                await message.channel.send(f'{modified_link} \n **Sent by @{message.author.name}**') # Send the modified link back to the user
    await client.process_commands(message)



@client.command(description = "Bot joins the user's vurrent voice channel")
async def join(ctx): # Join command 
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        print('Bot has connected')
        voice.play(nextcord.FFmpegPCMAudio(executable = "C:/ffmpeg/ffmpeg.exe", source = f"{folder}/lily.mp3"))
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")
    await ctx.message.delete()

@client.command(descrption = "Bot leaves the current voice channel")
async def leave(ctx): # Leave command
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye bye brother back to the lobby")
    else:
        await ctx.send("U good? ur not even in a voice channel")
    await ctx.message.delete()

@client.command()
async def pause(ctx): # Pause command
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No song is playing m8!')

@client.command(description = "Bot resumes playing the paused music/audio")
async def resume(ctx): # Resume command
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('The song is already playing!')

@client.command(description = "Stops the bots from playing music/audio")
async def stop(ctx): # Stop command
    voice = nextcord.utils.get(client.voice_clients, guild = ctx.guild)
    voice.stop()

@client.command(description = "Bot plays songs from playlist")
async def play(ctx, arg): # Play command
    voice = ctx.guild.voice_client
    song = f'{folder}/' + arg + '.mp3'
    source = FFmpegPCMAudio(executable = audiopeg, source = song)
    voice.play(source)
    print(f'Now Playing: {arg}')

@client.command(description = "Shows soundboard playlist")
async def playlist(ctx): # Playlist command
    print(";playlist command has been called")
    for file in dir:
        f, e = os.path.splitext(folder + '/' +  file)
        fname = f.split('/')
        re_name = fname[-1]
        files.append(re_name)
    embed = nextcord.Embed(title = 'Sound List')
    filelist = '\n'.join(files)
    embed.add_field(name = 'List of available sounds', value = filelist)
    await ctx.send(embed = embed)

@client.command(description = "Shows the list of stars of users")
async def stars(ctx): # Star list command
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

@client.command(description = "Clock in")
async def clockin(ctx): # Clock in command
    now = datetime.datetime.now()
    date = [now.year, now.month, now.day]
    author = str(ctx.message.author)
    memb = author.split('#')
    user = memb[0]
    
    if not attend.exists(user):
        attend.set(user, 0)
        clock.set(user, [1997, 1, 1])
        print(f'new user added at {date}')

    if clock.get(user) != date: 
        await ctx.reply(f'✅ **Congrats!** {user} has clocked in for today. Here have a gold star [⭐]')
        attend.append(user, 1)
        clock.set(user, date)
        if attend.get(user) != 0:
            if attend.get(user) == 7: # week
                await ctx.send(f"{user}, you've logged in for a week!")
            elif attend.get(user) == 30: # month
                await ctx.send(f"{user}, you've logged in for a month!")
            elif attend.get(user) == 180: # 6 months
                await ctx.send(f"{user}, you've logged in for half a year!")
            elif attend.get(user) == 365: # year
                await ctx.send(f"{user}, you've logged in for a year!")
        print(f'{user} +1 attendance')
    else:
        await ctx.send(f'{user} has already clocked in for today comeback tomorrow!')

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
        (365, "WELL DONE YOU HAVE DONE IT {nickname} YOU HAVE BEEN WITH US FOR MORE THAN A YEAR"),
        (210, "You do know that you're not being paid to this right, {nickname}?"),
        (180, "WOW! {nickname} MORE THAN 6 MONTHS?? GADDAMN"),
        (150, "5 months really? {nickname} r u sure ur touching grass?"),
        (120, "4 months now, do u have a life {nickname}?"),
        (101, "Damn {nickname}, you've logged in for more than 100 days"),
        (90, "3 months, r u ok {nickname}?"),
        (60, "2 months wow! {nickname}"),
        (30, "Congrats {nickname}! You've logged in more than there are days in February"),
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

# Advice command from API
@client.command()
async def fortunecookie(ctx):
    print('advice was called')
    response = requests.get('https://api.adviceslip.com/advice') 
    if response.status_code == 200:
        advice = response.json()['slip']['advice']
        print(f'{advice} sent')
        await ctx.send(advice)
    else:
        await ctx.send("Hmmm, looks to me like you don't need any adivce for now (✿◡‿◡)")

# Check age based from name from API
@client.command()
async def age(ctx, name):
    print('age was called')
    try:
        response = requests.get(f'https://api.agify.io/?name={name}') # Get API response
        if response.status_code == 200:
            data = response.json()
            age = data['age']
            await ctx.send(f"The estimated age for {name} is {age} years old.")
        else:
            await ctx.send("Sorry, I couldn't retrieve the age information.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Genshin randomizer 
@client.command()
async def genshinrandom(ctx):
    file_path = "C:/Users/a/Documents/GitHub/soundboard/genshincharacters.txt" # Genshin character list
    with open(file_path, "r") as gname:
        content_list = gname.readlines()
    name_list = [line.strip() for line in content_list]
    rand_team = random.sample(name_list, 4)
    print(rand_team)
    await ctx.send(f'Your random Geshin team is **{rand_team[0]}, {rand_team[1]}, {rand_team[2]}, {rand_team[3]}**')

client.run(TOKEN)