import datetime
from zoneinfo import ZoneInfo

import nextcord
from nextcord.ext import commands, tasks

from config import TIMEZONE, BIRTHDAY_CHANNEL_ID

PHT = datetime.timezone(datetime.timedelta(hours=8))

class Birthday(commands.Cog):
    """ A cog for tracking and announcing member birthdays """
    def __init__(self, bot):
        self.bot = bot
        self.collection = bot.db["birthdays"]
        self.tz = ZoneInfo(TIMEZONE)
        self.check_birthdays.start()

    def cog_unload(self):
        self.check_birthdays.cancel()

    @commands.command(description="Set another user's birthday")
    async def setbirthdayfor(self, ctx, member: nextcord.Member, date: str):
        """ Sets a birthday for a specific user, e.g. !setbirthdayfor @user 06-15-1998 """
        try:
            parsed = datetime.datetime.strptime(date, "%m-%d-%Y")
        except ValueError:
            await ctx.send("Invalid format! Use `MM-DD-YYYY`, e.g. `!setbirthdayfor @user 06-15-1998`")
            return

        user_id = member.id
        display_name = member.display_name

        await self.collection.update_one(
            {"_id": user_id},
            {"$set": {
                "username": display_name,
                "month": parsed.month,
                "day": parsed.day,
            }},
            upsert=True
        )

        await ctx.send(f"🎂 Set **{display_name}**'s birthday to **{parsed.strftime('%B %d')}**.")

    @commands.command(description="Set your birthday (format: MM-DD or MM-DD-YYYY)")
    async def setbirthday(self, ctx, date: str):
        """ Saves the user's birthday, e.g. !setbirthday 06-15 or !setbirthday 06-15-1998 """
        year = None
        parsed = None

        # Try MM-DD-YYYY first, then fall back to MM-DD
        for fmt in ("%m-%d-%Y", "%m-%d"):
            try:
                parsed = datetime.datetime.strptime(date, fmt)
                if fmt == "%m-%d-%Y":
                    year = parsed.year
                break
            except ValueError:
                continue

        if parsed is None:
            await ctx.send("Invalid format! Use `MM-DD` or `MM-DD-YYYY`, e.g. `!setbirthday 06-15` or `!setbirthday 06-15-1998`")
            return

        user_id = ctx.author.id
        display_name = ctx.author.display_name

        update_fields = {
            "username": display_name,
            "month": parsed.month,
            "day": parsed.day,
        }
        if year:
            update_fields["year"] = year
        else:
            # Explicitly unset year if they're re-setting without one
            update_fields["year"] = None

        await self.collection.update_one(
            {"_id": user_id},
            {"$set": update_fields},
            upsert=True
        )

        confirmation = f"🎂 Got it, {display_name}! Your birthday is set to **{parsed.strftime('%B %d')}**"
        confirmation += f", **{year}**." if year else "**."
        await ctx.send(confirmation)

    @commands.command(description="Check your saved birthday")
    async def mybirthday(self, ctx):
        """ Shows the user's currently saved birthday, and age if year was provided """
        record = await self.collection.find_one({"_id": ctx.author.id})
        if not record:
            await ctx.send("You haven't set a birthday yet! Use `!setbirthday MM-DD` or `MM-DD-YYYY`.")
            return

        date_str = datetime.date(2000, record["month"], record["day"]).strftime("%B %d")

        if record.get("year"):
            today = datetime.datetime.now(self.tz).date()
            birth_year = record["year"]
            age = today.year - birth_year - (
                (today.month, today.day) < (record["month"], record["day"])
            )
            await ctx.send(f"🎂 Your saved birthday is **{date_str}, {birth_year}** — that makes you **{age}** years old!")
        else:
            await ctx.send(f"🎂 Your saved birthday is **{date_str}** (no birth year on file).")

    @tasks.loop(time=datetime.time(hour=7, minute=0, tzinfo=PHT))
    async def check_birthdays(self):
        """ Runs daily at 7am (configured timezone), announces today's birthdays """
        now = datetime.datetime.now(self.tz)
        today_month = now.month
        today_day = now.day

        cursor = self.collection.find({"month": today_month, "day": today_day})
        birthday_people = await cursor.to_list(length=None)

        if not birthday_people:
            return

        channel = self.bot.get_channel(BIRTHDAY_CHANNEL_ID)
        if channel is None:
            print(f"Birthday channel ID {BIRTHDAY_CHANNEL_ID} not found or bot lacks access.")
            return

        for person in birthday_people:
            if person.get("year"):
                age = now.year - person["year"]
                await channel.send(
                    f"🎉 Happy Birthday, **{person['username']}**! "
                    f"Turning **{age}** today! Here's your cake (づ๑•ᴗ•๑)づ🎂! 🥳"
                )
            else:
                await channel.send(
                    f"🎉 Happy Birthday, **{person['username']}**! "
                    f"Here's your cake (づ๑•ᴗ•๑)づ🎂! 🥳"
                )

    @check_birthdays.before_loop
    async def before_check_birthdays(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Birthday(bot))