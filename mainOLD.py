# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event #initializing event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def threadfrom()


@bot.command()
async def threadfrom(ctx):
    # pick a message to start the thread on (here: the command's own message)
    message = ctx.message  

    thread = await message.create_thread(
        name="Discussion Thread",  # thread name
        auto_archive_duration=60   # in minutes (valid: 60, 1440, 4320, 10080)
    )

    await ctx.send(f"Thread created: {thread.mention}")


bot.run(TOKEN)