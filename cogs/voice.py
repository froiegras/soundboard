import os
import nextcord

from nextcord import FFmpegPCMAudio
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

playlist_dir = os.getenv('PLAYLIST_DIR')
audiopeg = os.getenv('FFMPEG_LOCATION')
files = []

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Join command
    @commands.command(description = "Bot joins the user's current voice channel")
    async def join(self, ctx):
        """ Bot joins the user's current voice channel """
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice = await channel.connect()
            voice.play(
                nextcord.FFmpegPCMAudio(
                    executable=audiopeg,
                    source=f"{playlist_dir}/lily.mp3"
                )
            )
        else:
            await ctx.send(f"{ctx.author.name} is not in a channel.")
            await self.bot.process_commands(ctx)

    # Leave command
    @commands.command(description = "Bot leaves the current voice channel")
    async def leave(self, ctx):
        """ Bot leaves the current voice channel """
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Bye bye brother back to the lobby")
        else:
            await ctx.send("U good? ur not even in a voice channel")

    # Pause command
    @commands.command()
    async def pause(self, ctx):
        """ Bot pauses the current song """
        voice = nextcord.utils.get(self.bot.voice_clients, guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send('No song is playing m8!')

    # Resume command
    @commands.command(description = "Bot resumes playing the paused music/audio")
    async def resume(self, ctx):
        """ Bot resumes playing the paused music/audio """
        voice = nextcord.utils.get(self.bot.voice_clients, guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send('The song is already playing!')

    # Stop command
    @commands.command(description = "Stops the bots from playing music/audio")
    async def stop(self, ctx):
        """ Stops the bots from playing music/audio """
        voice = nextcord.utils.get(self.bot.voice_clients, guild = ctx.guild)
        voice.stop()

    # Play command
    @commands.command(description = "Bot plays songs from playlist")
    async def play(self, ctx, arg):
        """ Bot plays songs from playlist """
        voice = ctx.guild.voice_client
        song = f'{playlist_dir}/' + arg + '.mp3'
        source = FFmpegPCMAudio(executable = audiopeg, source = song)
        voice.play(source)
        print(f'Now Playing: {arg}')

    # Playlist command
    @commands.command(description = "Shows soundboard playlist")
    async def playlist(self, ctx):
        """ Shows soundboard playlist """
        for file in playlist_dir:
            f, _ = os.path.splitext(playlist_dir + '/' +  file)
            fname = f.split('/')
            re_name = fname[-1]
            files.append(re_name)
        embed = nextcord.Embed(title = 'Sound List')
        filelist = '\n'.join(files)
        embed.add_field(name = 'List of available sounds', value = filelist)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Voice(bot))
