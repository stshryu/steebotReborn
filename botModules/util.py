from botMain import Bot
from discord.ext import commands
import time, datetime


class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def runtime(self, ctx):
        """ USAGE: !runtime """
        current_time = (int(time.time()) - int(Bot.start_time))
        delta = str(datetime.timedelta(seconds=current_time))
        print('Bot has been running for: {} hours'.format(delta))
        await ctx.send('Bot has been running for: **{}** hours'.format(delta))


def setup(bot):
    util = Utilities(bot)
    bot.add_cog(util)