import os
import datetime
import nextcord
import pickledb

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Lists
star = []
reminders = []
leaderboard = []

class Attendance(commands.Cog):
    """ A cog for handling attendance and star tracking """
    def __init__(self, bot):
        self.bot = bot
        self.collection = bot.db["attendance"]

    # Star list command
    @commands.command(description="Shows the list of stars of users")
    async def stars(self, ctx):
        """ Shows the list of stars of users """
        cursor = self.collection.find({})
        records = await cursor.to_list(length=None)

        if not records:
            await ctx.send("No one has clocked in yet!")
            return

        # Sort alphabetically by username (change key if you'd rather sort by streak)
        sorted_records = sorted(records, key=lambda r: r["username"].lower())

        usernames = [r["username"] for r in sorted_records]
        streaks = [str(r["streak"]) for r in sorted_records]

        ldb = '\n'.join(usernames)
        starlist = '\n'.join(streaks)

        embed = nextcord.Embed(title='⭐ List')
        embed.add_field(name='User', value=ldb)
        embed.add_field(name='⭐', value=starlist)
        await ctx.send(embed=embed)

    # Clock in command
    @commands.command(description="Clock in")
    async def clockin(self, ctx):
        """ Clock in for the day """
        try:
            now = datetime.datetime.now()
            today = [now.year, now.month, now.day]
            formatted_time = f"{now.hour:02}:{now.minute:02}:{now.second:02}"

            user_id = ctx.author.id
            display_name = ctx.author.display_name  # server nickname if set, else username

            record = await self.collection.find_one({"_id": user_id})

            if record is None:
                # New user, never clocked in before
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
                            "username": display_name,  # keep display name fresh in case they changed it
                        },
                        "$inc": {"streak": 1},
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


    # Add stars to @user command
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
            await self.collection.update_one(
                {"_id": user_id},
                {"$inc": {"streak": 1}}
            )
            print(f"Added +1 to {target.display_name}")
        else:
            await ctx.send(f"{target.display_name} hasn't clocked in yet, can't add a star.")

    # Check attendance command
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

            # Check for accolades based on days_logged_in, highest threshold first
            for days, accolade_msg in accolades:
                if days_logged_in >= days:
                    await ctx.send(accolade_msg.format(nickname=nickname))
                    break  # now correctly inside the if — stops at first match
        else:
            await ctx.reply('You haven\'t clocked in a single time? We should fire you.')

def setup(bot):
    """ Load the Attendance cog """
    bot.add_cog(Attendance(bot))
