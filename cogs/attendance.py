import datetime
from zoneinfo import ZoneInfo
import nextcord

from nextcord.ext import commands, tasks
from dotenv import load_dotenv

from config import TIMEZONE, PA_CHANNEL_ID

load_dotenv()

# Lists
star = []
reminders = []
leaderboard = []
PHT = datetime.timezone(datetime.timedelta(hours=8))

class Attendance(commands.Cog):
    """ A cog for handling attendance and star tracking """
    def __init__(self, bot):
        self.bot = bot
        self.collection = bot.db["attendance"]
        self.tz = ZoneInfo(TIMEZONE)
        self.year_end_check.start()
        self.year_end_check.cancel()

    @commands.command(description="Shows the list of stars of users")
    async def stars(self, ctx):
        """ Shows the list of stars of users """
        cursor = self.collection.find({})
        records = await cursor.to_list(length=None)

        if not records:
            await ctx.send("No one has clocked in yet!")
            return

        sorted_records = sorted(records, key=lambda r: r["username"].lower())

        usernames = [r["username"] for r in sorted_records]
        streaks = [str(r["streak"]) for r in sorted_records]

        ldb = '\n'.join(usernames)
        starlist = '\n'.join(streaks)

        embed = nextcord.Embed(title='⭐ List')
        embed.add_field(name='User', value=ldb)
        embed.add_field(name='⭐', value=starlist)
        await ctx.send(embed=embed)

    @commands.command(description="Clock in")
    async def clockin(self, ctx):
        """ Clock in for the day """
        try:
            now = datetime.datetime.now(self.tz)
            today = [now.year, now.month, now.day]
            formatted_time = f"{now.hour:02}:{now.minute:02}:{now.second:02}"
            year_key = str(now.year)

            user_id = ctx.author.id
            display_name = ctx.author.display_name

            record = await self.collection.find_one({"_id": user_id})

            if record is None:
                record = {
                    "_id": user_id,
                    "username": display_name,
                    "streak": 0,
                    "last_clock_date": [1997, 1, 1],
                }
                await self.collection.insert_one(record)
                print(f"new user added at {today}")

            if record["last_clock_date"] != today:
                new_streak = record["streak"] + 1

                await self.collection.update_one(
                    {"_id": user_id},
                    {
                        "$set": {
                            "last_clock_date": today,
                            "username": display_name,
                        },
                        "$inc": {"streak": 1, f"yearly.{year_key}": 1},
                    },
                )

                await ctx.reply(
                    f"✅ **Congrats!** {display_name} has clocked in for today at "
                    f"{formatted_time}. Here have a gold star [⭐]"
                )

                milestones = {7: "a week", 30: "a month", 180: "half a year", 365: "a year"}
                if new_streak in milestones:
                    await ctx.send(f"{display_name}, you've logged in for {milestones[new_streak]}!")

                print(f"{display_name} +1 attendance")
            else:
                await ctx.send(
                    f"{display_name} has already clocked in for today at "
                    f"{formatted_time}, come back tomorrow!"
                )
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


    @commands.command()
    @commands.is_owner()
    async def adds(self, ctx):
        """ Adds a star to the mentioned user """
        if not ctx.message.mentions:
            await ctx.send("You need to mention a user!")
            return

        target = ctx.message.mentions[0]
        user_id = target.id

        record = await self.collection.find_one({"_id": user_id})
        if record:
            year_key = str(datetime.datetime.now(self.tz).year)

            await self.collection.update_one(
                {"_id": user_id},
                {"$inc": {"streak": 1, f"yearly.{year_key}": 1}}
            )

            await ctx.message.add_reaction("⭐")
            print(f"Added +1 to {target.display_name}")
        else:
            await ctx.send(f"{target.display_name} hasn't clocked in yet, can't add a star.")

    @commands.command(description="Shows the user's number of stars")
    async def attendance(self, ctx):
        """ Shows the user's number of stars and accolades """
        member = ctx.author
        user_id = member.id
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

        record = await self.collection.find_one({"_id": user_id})

        if record:
            days_logged_in = record["streak"]
            await ctx.reply(f'{nickname} has {days_logged_in} ⭐ ( ﾟ∀ﾟﾉﾉﾞ')

            for days, accolade_msg in accolades:
                if days_logged_in >= days:
                    await ctx.send(accolade_msg.format(nickname=nickname))
                    break
        else:
            await ctx.reply('You haven\'t clocked in a single time? We should fire you.')

    async def get_year_winners(self, year: int):
        """ Returns (winners, top_count). More than one winner means a tie. """
        key = str(year)
        records = await self.collection.find({f"yearly.{key}": {"$gt": 0}}).to_list(length=None)
        if not records:
            return [], 0
        top = max(r["yearly"][key] for r in records)
        return [r for r in records if r["yearly"][key] == top], top

    async def announce_year_winner(self, year: int, channel=None, force=False) -> bool:
        meta = self.bot.db["attendance_meta"]
        if not force and await meta.find_one({"_id": f"announced:{year}"}):
            return False

        winners, top = await self.get_year_winners(year)
        channel = channel or self.bot.get_channel(PA_CHANNEL_ID)
        if not winners or channel is None:
            return False

        mentions = " ".join(f"<@{w['_id']}>" for w in winners)
        await channel.send(
            f"🏆 **{year} Attendance Champion{'s' if len(winners) > 1 else ''}** 🏆\n"
            f"Congratulations {mentions}, you clocked in **{top}** times in {year}! ⭐"
        )

        if not force:
            await meta.insert_one({"_id": f"announced:{year}"})
        return True

    @tasks.loop(time=datetime.time(hour=0, minute=5, tzinfo=PHT))
    async def year_end_check(self):
        now = datetime.datetime.now(self.tz)
        if now.month == 1 and now.day == 1:
            await self.announce_year_winner(now.year - 1)

    @year_end_check.before_loop
    async def before_year_end_check(self):
        await self.bot.wait_until_ready()
        now = datetime.datetime.now(self.tz)
        if now.month == 1:
            await self.announce_year_winner(now.year - 1)

def setup(bot):
    """ Load the Attendance cog """
    bot.add_cog(Attendance(bot))
