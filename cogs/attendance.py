import nextcord, json, datetime, pickledb

from nextcord.ext import commands

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

attenddb = config.get('attend')
clockdb = config.get('clock')

# Databases
# attend = pickledb.load(attenddb, auto_dump=True)
# clock = pickledb.load(clockdb, auto_dump=True)

# Lists
star = []
reminders = []
leaderboard = []

class Attendance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Star list command
    @commands.command(description = "Shows the list of stars of users")
    async def stars(self, ctx):
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
    @commands.command(description = "Clock in")
    async def clockin(self, ctx):
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
    @commands.command()
    @commands.is_owner()
    async def adds(self, ctx):
        uname = str(ctx.message.mentions[0])
        memb = uname.split('#')
        user = memb[0]
        if attend.exists(user):
            attend.append(user, 1)
        print(f'Added +1 to {user}')

    # Check attendance command
    @commands.command(description = "Shows the user's number of stars")
    async def attendance(self, ctx):
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

def setup(bot):
    bot.add_cog(Attendance(bot))