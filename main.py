# Library Imports
import nextcord, os, datetime, pickledb, random, time
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from config import TOKEN

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


# Files and Folders
audiopeg = "C:/ffmpeg/ffmpeg.exe"
folder = r'C:/Users/a/Documents/GitHub/discord bot/sound' # Soundbite directories
won = r'C:/Users/a/Documents/GitHub/soundboard/wonbonk.mp4' # Video variable
saed = r'C:/Users/a/Documents/GitHub/soundboard/whysaed.mp4' # Video variable
dir = os.listdir(folder)

# Databases
attend = pickledb.load('C:/Users/a/Documents/GitHub/discord bot/db/attend.db', True)
clock = pickledb.load('C:/Users/a/Documents/GitHub/discord bot/db/clock.db', True)

# Ready message
@client.event
async def on_ready():
    print("KN Bot is now online")

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
    if message.content.lower() == 'sad':
        print('saed detected')
        vid = nextcord.File(saed)
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
    if message.content.lower() == "audacity":
        print("audacity detected")
        await message.channel.send("https://media.discordapp.net/attachments/1040089640050372769/1153529599003725835/audacity_cover.png?width=885&height=498")
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
    if 'barack' in message.content.lower() or "were so barack" in message.content.lower() or "obama" in message.content.lower() or "we're back" in message.content.lower() or "were back" in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/766470595109453846/1147847134410981438/FwhNQWKWwAYVrjg.png?width=498&height=498")
    # Streamable link dead
    # if 'bad' in message.content.lower() or "so bad" in message.content.lower():
    #     await message.channel.send("https://streamable.com/wv85uj")
    if 'goat' in message.content.lower() and not message.author.bot:
        await message.channel.send("https://media.discordapp.net/attachments/766470595109453846/1153549726160011376/dont_underestimate_a_goat.png")
    if 'instagram.com/' in message.content.lower():  #Check if the message contains an Instagram link
        print('Instagram link detected')
        if not message.author.bot: # Check if the message is from a user (not a bot)
            if 'ddinstagram.com' in message.content.lower():
                print('Already embedded')
            elif 'instagram.com' in message.content: # Check if the message contains an Instagram link
                await message.edit(suppress = True) # Remove embed rom previous message
                parts = message.content.split('instagram.com') # Split the message content by 'instagram.com'
                modified_link = parts[0] + 'ddinstagram.com' + parts[1] # Insert 'dd' between 'www.' and 'instagram.com'
                await message.reply(f'{modified_link} \n **Sent by @{message.author.name}**', mention_author = False) # Send the modified link back to the user
    if 'tiktok.com/' in message.content.lower():  #Check if the message contains an tiktok link
        print('Tiktok link detected')
        if not message.author.bot: # Check if the message is from a user (not a bot)
            if 'vxtiktok.com' in message.content.lower():
                print('Already embedded')
            elif 'tiktok.com' in message.content: # Check if the message contains an Tiktok link
                await message.edit(suppress = True) # Remove embed rom previous message
                parts = message.content.split('tiktok.com') # Split the message content by 'tiktok.com'
                modified_link = parts[0] + 'vxtiktok.com' + parts[1] # Insert 'vx' between 'www.' and 'tiktok.com'
                await message.reply(f'{modified_link} \n **Sent by @{message.author.name}**', mention_author = False) # Send the modified link back to the user
    if 'twitter.com/' in message.content.lower() or 'x.com/' in message.content.lower():
        print('Twitter link detected')
        if not message.author.bot:
            if 'vxtwitter.com' in message.content.lower():
                print('Already embedded')
            elif 'twitter.com' in message.content.lower() or 'x.com' in message.content.lower():
                await message.edit(suppress=True)
                modified_content = message.content.replace('twitter.com', 'vxtwitter.com').replace('x.com', 'vxtwitter.com')
                await message.reply(f'{modified_content}\n**Sent by @{message.author.name}**', mention_author=False)
    current_time = time.time()
    if message.author.id in msg_counts:
      msg_counts[message.author.id] += 1
    else:
      msg_counts[message.author.id] = 1
    if len(message.content) > 1000 and not message.author.bot:
      print('long ass message deteceted')
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
    if "spotify" in message.content.lower() and not message.author.bot:
      print('spotify detected')
      await message.channel.send("Whether you're up in the clouds or going way underground, it's easy to take your music with you whereever you go. With Spotify Premium, you can save your favorite songs to your phone and listen offline. That means you can play anywhere, anytime without using any data. And right now, you can try Premium free for 30 days. Ready to make the move? Tap the banner to learn more.")
    if "tito badang" in message.content.lower():
      await message.channel.send("DALAWANG BESES NA YAN! Unang una pinagtanggol kita sa lahat ng tropa, hah? Kahit takpan mo pa yang mukha mo mo hah, ilalabas ko to, dahil iSA KANG GAGO! Dito ka pa nakatira sa bahay ko? Pinapatira kita, tinuring kitang... ka-kaibigan, tol! Hah? Kahit anong sabihin mo tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Badang hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko.” GAGO KA BA? SISIRAIN KITA NGAYON, YANG PANGALAN MO? PUTANG INA MO! LUMAYAS KA! TANGINA MO!")
    if "why not" in message.content.lower():
      await message.channel.send("https://www.youtube.com/watch?v=coY2IA-oBvw")
    if "ambatu" in message.content.lower() or message.content.lower() in ['bust', 'cum', 'coom', 'blow']:
      await message.channel.send("https://tenor.com/bSJ3l.gif")
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