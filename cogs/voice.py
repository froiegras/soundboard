import asyncio
import os
import sys
import nextcord

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

playlist_dir = os.getenv('PLAYLIST_DIR')
audiopeg = os.getenv('FFMPEG_LOCATION')
files = []

class SoundButton(nextcord.ui.Button):
    def __init__(self, sound_name: str):
        super().__init__(label=sound_name, style=nextcord.ButtonStyle.primary)
        self.sound_name = sound_name

    async def callback(self, interaction: nextcord.Interaction):
        # Check the person clicking is in a voice channel
        if not interaction.user.voice:
            await interaction.response.send_message(
                "You need to be in a voice channel to play a sound!", ephemeral=True
            )
            return

        voice = interaction.guild.voice_client

        # Connect if not already in a channel, otherwise move to the user's channel
        if not voice:
            voice = await interaction.user.voice.channel.connect()
        elif voice.channel != interaction.user.voice.channel:
            await voice.move_to(interaction.user.voice.channel)

        song_path = f'{playlist_dir}/{self.sound_name}.mp3'
        if not os.path.isfile(song_path):
            await interaction.response.send_message(
                f"Couldn't find `{self.sound_name}`.", ephemeral=True
            )
            return

        if voice.is_playing():
            voice.stop()

        source = nextcord.FFmpegPCMAudio(executable=audiopeg, source=song_path)
        voice.play(source)

        await interaction.response.send_message(f"▶️ Playing **{self.sound_name}**", ephemeral=True)
        print(f'Now Playing: {self.sound_name}')


class PlaylistView(nextcord.ui.View):
    def __init__(self, sound_names: list, page: int = 0):
        super().__init__(timeout=180)
        self.sound_names = sound_names
        self.page = page
        self.per_page = 20  # leaves row 4 free for Prev/Next

        start = page * self.per_page
        end = start + self.per_page
        page_sounds = sound_names[start:end]

        for name in page_sounds:
            self.add_item(SoundButton(name))

        if len(sound_names) > self.per_page:
            if page > 0:
                self.add_item(self.PageButton("◀ Prev", page - 1, sound_names))
            if end < len(sound_names):
                self.add_item(self.PageButton("Next ▶", page + 1, sound_names))

    class PageButton(nextcord.ui.Button):
        def __init__(self, label, target_page, sound_names):
            super().__init__(label=label, style=nextcord.ButtonStyle.secondary, row=4)
            self.target_page = target_page
            self.sound_names = sound_names

        async def callback(self, interaction: nextcord.Interaction):
            new_view = PlaylistView(self.sound_names, page=self.target_page)
            await interaction.response.edit_message(view=new_view)

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Join command
    @commands.command(description="Bot joins the user's current voice channel")
    async def join(self, ctx):
        """ Bot joins the user's current voice channel """
        if not ctx.author.voice:
            await ctx.send(f"{ctx.author.name} is not in a channel.")
            return

        channel = ctx.author.voice.channel

        if ctx.voice_client:
            await ctx.voice_client.move_to(channel)
        else:
            voice = await channel.connect()
            await asyncio.sleep(5)
            print(f"is_connected after 5s: {voice.is_connected()}")
            # voice.play(
            #     nextcord.FFmpegPCMAudio(
            #         executable=audiopeg,
            #         source=f"{playlist_dir}/lily.mp3",
            #         stderr=sys.stdout  # forces ffmpeg's own error output into your console
            #     )
            # )


    # Leave command
    @commands.command(description="Bot leaves the current voice channel")
    async def leave(self, ctx):
        """ Bot leaves the current voice channel """
        voice_client = ctx.voice_client
        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
            await voice_client.disconnect(force=True)
            await ctx.send("Bye bye brother back to the lobby")
        else:
            await ctx.send("U good? ur not even in a voice channel")

    # Pause command
    @commands.command()
    async def pause(self, ctx):
        voice = ctx.guild.voice_client
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.send('No song is playing m8!')

    # Resume command
    @commands.command(description="Bot resumes playing the paused music/audio")
    async def resume(self, ctx):
        voice = ctx.guild.voice_client
        if voice and voice.is_paused():
            voice.resume()
        else:
            await ctx.send('The song is already playing!')

    # Stop command
    @commands.command(description="Stops the bots from playing music/audio")
    async def stop(self, ctx):
        voice = ctx.guild.voice_client
        if voice:
            voice.stop()
        else:
            await ctx.send("I'm not even playing anything!")

    # Play command
    @commands.command(description="Bot plays songs from playlist")
    async def play(self, ctx, arg):
        """ Bot plays songs from playlist """
        print(f"play command triggered with arg: {arg}")  # debug line
        voice = ctx.guild.voice_client

        if not voice or not voice.is_connected():
            if ctx.author.voice:
                voice = await ctx.author.voice.channel.connect()
            else:
                await ctx.send("I'm not in a voice channel, and you're not either! Use `!join` first.")
                return

        song_path = f'{playlist_dir}/{arg}.mp3'
        if not os.path.isfile(song_path):
            await ctx.send(f"Couldn't find a sound called `{arg}`.")
            return

        if voice.is_playing():
            voice.stop()

        source = nextcord.FFmpegPCMAudio(executable=audiopeg, source=song_path)
        voice.play(source)
        print(f'Now Playing: {arg}')

    @commands.command(description="Shows soundboard playlist as buttons")
    async def playlist(self, ctx):
        """ Shows soundboard playlist as clickable buttons """
        files = []
        for file in os.listdir(playlist_dir):
            name, ext = os.path.splitext(file)
            if ext == '.mp3':
                files.append(name)

        if not files:
            await ctx.send("No sounds available!")
            return

        files.sort()
        view = PlaylistView(files)
        await ctx.send("🎵 **Sound List** — click a button to play:", view=view)

    # @commands.command(description="Shows soundboard playlist")
    # async def playlist(self, ctx):
    #     """ Shows soundboard playlist """
    #     files = []
    #     for file in os.listdir(playlist_dir):
    #         name, ext = os.path.splitext(file)
    #         if ext == '.mp3':
    #             files.append(name)

    #     if not files:
    #         await ctx.send("No sounds available!")
    #         return

    #     message = "**Sound List**\n" + '\n'.join(files)
    #     if len(message) > 2000:
    #         # still need chunking, just at 2000 instead of 1024
    #         for i in range(0, len(message), 2000):
    #             await ctx.send(message[i:i+2000])
    #     else:
    #         await ctx.send(message)

def setup(bot):
    bot.add_cog(Voice(bot))

