import os
from Alive import keep_alive
import discord

client = discord.Client()





@client.event
async def on_ready():
    activity = discord.Game(name="Ragnarok Server For Ever | 1 Server :)", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


@client.event
async def on_message(message):

    print(message)


keep_alive()

client.run("OTA5Nzk0NjMzMDYyNzAzMTU0.YZJeRw.bxfzQhwlVqp2-RIFq83m5MwMlrA")