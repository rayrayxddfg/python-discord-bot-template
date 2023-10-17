import discord
import os
import time
from discord.ext import commands
from keep_alive import keep_alive

# Your Discord token
DT = os.environ['DT']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    '7/'), case_insensitive=True, intents=intents)


@bot.event
async def on_message(message):
    # Check if the message is from a server (guild)
    if message.guild:
        await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    # Start a timer
    start_time = time.time()

    # Send a message to the channel
    await ctx.send("Ping...")

    # End the timer
    end_time = time.time()

    # Calculate the ping time
    ping_time = end_time - start_time

    # Send the ping time to the channel
    await ctx.send(f"Pong! {ping_time * 1000:.0f}ms")


keep_alive()
bot.run(DT)
