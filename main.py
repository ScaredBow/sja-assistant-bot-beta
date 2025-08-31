import discord
import os # default module
from dotenv import load_dotenv

load_dotenv(".gitignore.env") # load all the variables from the env file
TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name="register", description="Register your Discord account")
async def register(ctx: discord.ApplicationContext):
    user_id = ctx.author.id      # This is their Discord user ID (a unique int)
    username = str(ctx.author)   # e.g. "ScarboChan#1234"

    # For now, just log it and reply
    print(f"Registered user {username} with ID {user_id}")
    await ctx.respond(f"✅ Registered you with ID `{user_id}`")


bot.run(TOKEN) # run the bot with the token