import os
import discord

bot = discord.Client(intents=discord.Intents.none())

@bot.event
async def on_ready():
    print(f"Online as {bot.user}")

bot.run(os.environ["DISCORD_TOKEN"])
