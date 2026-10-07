import aiohttp
import nextcord
from nextcord.ext import commands


class Weather(commands.Cog):
    """ A cog for fetching weather data from wttr.in """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Shows current weather for a city")
    async def weather(self, ctx, *, city: str = None):
        """ Fetches current weather for a given city using wttr.in """
        if not city:
            await ctx.send("You need to tell me a city! e.g. `!weather Manila`")
            return

        url = f"https://wttr.in/{city}?format=j1"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        await ctx.send(f"Couldn't fetch weather for **{city}** (status {response.status}).")
                        return
                    data = await response.json(content_type=None)

            current = data["current_condition"][0]
            area = data["nearest_area"][0]

            location_name = area["areaName"][0]["value"]
            country = area["country"][0]["value"]
            temp_c = current["temp_C"]
            feels_like_c = current["FeelsLikeC"]
            description = current["weatherDesc"][0]["value"]
            humidity = current["humidity"]
            wind_kmph = current["windspeedKmph"]

            embed = nextcord.Embed(
                title=f"Weather in {location_name}, {country}",
                description=f"**{description}**",
                color=nextcord.Color.blue()
            )
            embed.add_field(name="🌡️ Temperature", value=f"{temp_c}°C (feels like {feels_like_c}°C)", inline=True)
            embed.add_field(name="💧 Humidity", value=f"{humidity}%", inline=True)
            embed.add_field(name="💨 Wind", value=f"{wind_kmph} km/h", inline=True)
            embed.set_footer(text="Data from wttr.in")

            await ctx.send(embed=embed)

        except aiohttp.ClientError as e:
            await ctx.send(f"Network error while fetching weather: {e}")
        except (KeyError, IndexError):
            await ctx.send(f"Couldn't find weather data for **{city}**. Check the spelling?")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}")


def setup(bot):
    bot.add_cog(Weather(bot))