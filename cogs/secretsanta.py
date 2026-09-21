import random
import nextcord
from nextcord.ext import commands

class SecretSanta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.collection = bot.db["secret_santa"]

    @commands.command(description="Join the Secret Santa pool")
    async def joinsanta(self, ctx):
        """ Adds the user to the Secret Santa pool """
        user_id = ctx.author.id
        username = ctx.author.display_name

        existing = await self.collection.find_one({"_id": user_id})
        if existing:
            await ctx.send(f"{username}, you've already joined the pool! 🎅")
            return

        await self.collection.insert_one({
            "_id": user_id,
            "username": username,
            "assigned_to": None,  # who this person is buying for
        })
        await ctx.send(f"🎁 {username} has joined the Secret Santa pool!")

    @commands.command(description="Leave the Secret Santa pool")
    async def leavesanta(self, ctx):
        """ Removes the user from the pool, if they haven't been assigned yet """
        user_id = ctx.author.id
        result = await self.collection.delete_one({"_id": user_id})
        if result.deleted_count:
            await ctx.send(f"{ctx.author.display_name} has left the pool.")
        else:
            await ctx.send("You weren't in the pool.")

    @commands.command(description="Show everyone currently in the pool")
    async def poolsanta(self, ctx):
        """ Lists current participants """
        cursor = self.collection.find({})
        participants = await cursor.to_list(length=None)

        if not participants:
            await ctx.send("No one has joined yet!")
            return

        names = '\n'.join(p["username"] for p in participants)
        embed = nextcord.Embed(title="🎄 Secret Santa Pool", description=names)
        await ctx.send(embed=embed)

    @commands.command(description="Start Secret Santa and assign names")
    @commands.is_owner()
    async def startsanta(self, ctx):
        """ Randomly assigns each participant someone else to buy a gift for """
        cursor = self.collection.find({})
        participants = await cursor.to_list(length=None)

        if len(participants) < 3:
            await ctx.send("Need at least 3 participants for Secret Santa to work properly!")
            return

        givers = [p["_id"] for p in participants]
        receivers = givers.copy()

        # Keep shuffling until no one is assigned to themselves
        assignment = None
        for _ in range(1000):  # safety cap, effectively never hit for reasonable group sizes
            random.shuffle(receivers)
            if all(g != r for g, r in zip(givers, receivers)):
                assignment = dict(zip(givers, receivers))
                break

        if assignment is None:
            await ctx.send("Failed to generate valid assignments, try again!")
            return

        # Build a lookup for usernames and user objects
        id_to_data = {p["_id"]: p for p in participants}

        failed_dms = []
        for giver_id, receiver_id in assignment.items():
            receiver_name = id_to_data[receiver_id]["username"]

            # Save the assignment in the DB
            await self.collection.update_one(
                {"_id": giver_id},
                {"$set": {"assigned_to": receiver_id}}
            )

            # DM the giver their assigned recipient
            try:
                user = await self.bot.fetch_user(giver_id)
                await user.send(
                    f"🎅 **Secret Santa Assignment!**\n"
                    f"You are getting a gift for: **{receiver_name}** 🎁\n"
                    f"Shhh, keep it secret!"
                )
            except (nextcord.Forbidden, nextcord.HTTPException):
                failed_dms.append(id_to_data[giver_id]["username"])

        if failed_dms:
            await ctx.send(
                f"✅ Assignments complete! However, I couldn't DM: {', '.join(failed_dms)} "
                f"(they may have DMs disabled)."
            )
        else:
            await ctx.send("✅ Secret Santa assignments have been sent out via DM to everyone!")

    @commands.command(description="Reset the Secret Santa pool for next time")
    @commands.is_owner()
    async def resetsanta(self, ctx):
        """ Clears the pool, ready for a new round """
        await self.collection.delete_many({})
        await ctx.send("🧹 Secret Santa pool has been reset for next time.")


def setup(bot):
    bot.add_cog(SecretSanta(bot))