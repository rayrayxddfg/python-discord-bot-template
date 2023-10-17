import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()  # Create a default intent
intents.typing = False
intents.presences = False

# Create a bot instance with specified intents
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='ping', help='Check the bot\'s ping time.')
async def ping(ctx):
    latency = bot.latency  # Get the bot's latency

    # Calculate the ping time in milliseconds
    ping_time = round(latency * 1000)

    await ctx.send(f'Pong! Bot latency is {ping_time}ms')

# Use an environment variable for your bot token
TOKEN = os.environ.get('DT')

if TOKEN is not None:
    keep_alive()
    bot.run(TOKEN)
else:
    print("DISCORD_TOKEN environment variable not set. Please set it with your bot token.")
