import discord
from discord.ext import commands


class FunStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print('FunStuff Cog Loaded')

    @commands.command()
    async def info(self, ctx):
        """--Prints the users name, this channel, and the server"""
        await ctx.send(f'You are {ctx.author}, this is the {ctx.channel} channel in the {ctx.guild} server')


async def setup(bot):
    await bot.add_cog(FunStuff(bot))
