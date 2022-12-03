# https://medium.com/codex/learn-web-scraping-the-fun-way-with-a-discord-bot-704d3422a6a2
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands


class WebScrape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print('WebScrape Cog Loaded')


async def setup(bot):
    await bot.add_cog(WebScrape(bot))
