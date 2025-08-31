import discord
import os # default module
from dotenv import load_dotenv

load_dotenv(".gitignore.env") # load all the variables from the env file
TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"{bot.user} is ready and online!")

""" #for rapid development
GUILD_ID = 1036149549468749904  # put your server's ID here
@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.sync_commands(guild=guild)  # syncs only in this guild
    print(f"Synced commands in guild {GUILD_ID} for {bot.user}") """

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

from notion import add_entry_to_person_property
@bot.slash_command(name="register", description="Register your Discord account")
async def register(ctx: discord.ApplicationContext, first_name: str):
    msg = await ctx.respond("⏳ Working on it...")
    user_id = ctx.author.id
    username = str(ctx.author)
    first_name = first_name.capitalize()
    database_id = "25a82fd5864f81689d2cca589643471e"
    result = await add_entry_to_person_property(
        database_id, first_name, "Discord ID", user_id
    )
    if result:
        print(f"Registered {first_name} with ID {user_id}")
        await msg.edit_original_response(content=f"✅ Registered {first_name} with {user_id}")
    else:
        print(f"Failed {first_name} with ID {user_id}")
        await msg.edit_original_response(content=f"⚠️ Could not find {first_name} in the database. Please try again.")



bot.run(TOKEN) # run the bot with the token