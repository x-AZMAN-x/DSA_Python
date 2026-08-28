import discord
from discord.ext import commands

# 1. Setup bot intentions (what data your bot is allowed to read)
intents = discord.Intents.default()
intents.message_content = True  # Allows bot to read message text

# 2. Initialize the bot with a command prefix (e.g., !help, !ping)
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Runs when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user.name}!")

# Command: Responds to "!ping" with "Pong!"
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Command: Echoes back whatever the user says after "!repeat"
@bot.command()
async def repeat(ctx, *, message: str):
    await ctx.send(message)

# 3. Start the bot (Replace 'YOUR_BOT_TOKEN_HERE' with your actual token)
bot.run("YOUR_BOT_TOKEN_HERE")