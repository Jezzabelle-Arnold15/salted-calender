import pickle
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print("Bot is ready")


# functions for message processing
async def add_date(message):
    await message.channel.send("add date")


async def remove_date(message):
    await client.wait_for('reaction_add', timeout=60.0, check=check)


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot or not message.content.startswith("$"):
        return
    if message.content.startswith("$add date"):
        await add_date(message)


if __name__ == "__main__":
    try:
        f = open("dates.pickle", "rb")
        dates = pickle.load(f)
        f.close()
        print("read file")
    except:
        f = open("dates.pickle", "wb")
        dates = ""
        pickle.dump(dates, f)
        f.close()
        print("made file")
#this string is left blank but is filled in using running versions of the code. Removed for security
client.run('')
