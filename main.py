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

@bot.slash_command(name="help", description="")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("Hi! For assistance, please contact @ccc")

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

@bot.slash_command(name="more", description="Advanced Settings")
async def more(ctx: discord.ApplicationContext):
    await ctx.respond("work in progress")

from discord import Option
@bot.slash_command(name="profile", description="Retrieve your profile information")
async def profile(
    ctx: discord.ApplicationContext,
    first_name: Option(str, "First name of the person to look up. Returns yourself if empty.") = None,
    search_depth: Option(int, "Level of search (0, 1, 2, 3). Restricted parameter.") = None
    ):
    msg = f'Profile for {ctx.author}'
    if first_name:
        msg += f"\nLooking up first name: {first_name}"
    if search_depth:
        msg += f"\nSearch depth: {search_depth}"
    await ctx.respond(msg) 

bot.run(TOKEN) # run the bot with the token