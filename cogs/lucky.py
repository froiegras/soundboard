import asyncio
import random
from collections import Counter

from nextcord.ext import commands


def get_most_frequent_numbers(
    pool_min: int = 1,
    pool_max: int = 58,
    picks_per_draw: int = 6,
    num_draws: int = 10_000,
    top_n: int = 6,
    seed: int | None = None,
) -> list[tuple[int, int]]:
    """ Simulates many draws and returns the top_n most frequent numbers as (number, count) pairs. """
    if picks_per_draw > (pool_max - pool_min + 1):
        raise ValueError("picks_per_draw cannot exceed the size of the number pool.")

    rng = random.Random(seed)
    counts: Counter[int] = Counter()
    population = range(pool_min, pool_max + 1)

    for _ in range(num_draws):
        counts.update(rng.sample(population, k=picks_per_draw))

    return counts.most_common(top_n)


class Lucky(commands.Cog):
    """ Lucky number generator """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Get your lucky numbers (optional: highest number in the pool)")
    async def lucky(self, ctx, pool_max: int = 49):
        """ Usage: !lucky  or  !lucky 60 """
        if not 6 <= pool_max <= 1000:
            await ctx.send("Pick a maximum between 6 and 1000, e.g. `!lucky 60`.")
            return

        top = await asyncio.to_thread(get_most_frequent_numbers, 1, pool_max)
        numbers = sorted(num for num, _ in top)
        await ctx.send("🍀 Your lucky numbers: " + " · ".join(map(str, numbers)))

    @lucky.error
    async def lucky_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("That needs to be a whole number, e.g. `!lucky 60`.")
        else:
            raise error


def setup(bot):
    bot.add_cog(Lucky(bot))