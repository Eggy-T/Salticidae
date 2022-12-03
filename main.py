import asyncio
import discord
import logging
import os
from discord.ext import commands
# starts logs and puts them into discord.log, change logging level for more granularity
logging.basicConfig(filename='discord.log', filemode='w',format='%(asctime)s %(message)s', level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='>')


@bot.event
async def on_ready():
    print(f'Ready: Logged in as {bot.user}')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(f'Cog: {filename} attempting...')
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(os.getenv("TOKEN"))


try:
    asyncio.run(main())
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
