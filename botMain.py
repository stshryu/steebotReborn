import configparser
from discord.ext import commands
import time
import os


class Bot(commands.Bot):

    start_time = time.time()

    def __init__(self, command_prefix, formatter=None, description=None, **options):
        super().__init__(command_prefix, formatter, description, **options)
        self.initialize_config()
        self.initialize_extensions()

    def initialize_config(self):
        ini_path = os.path.join(os.getcwd(), 'config/baseconfig.ini')
        config = configparser.ConfigParser()
        config.read_file(open(ini_path))
        self.token = config['Token Information']['BotToken']

    def initialize_extensions(self):
        def load_extension(name):
            self.load_extension('botModules.{0}'.format(name))
        load_extension('util')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready')