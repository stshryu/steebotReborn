from discord.ext import commands

class Dota(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    dota = Dota(bot)
    bot.add_cog(dota)