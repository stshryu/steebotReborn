import botMain
import logging

### Logging disabled during dev

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
#
# # Info Logger
# handlerInfo = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
# handlerInfo.setLevel(logging.INFO)
# handlerInfo.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handlerInfo)
#
# # Debug Logger
# handlerDebug = logging.FileHandler(filename='logs/discord.debug.log', encoding='utf-8', mode='w')
# handlerDebug.setLevel(logging.DEBUG)
# handlerDebug.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handlerDebug)

steebot = botMain.Bot('!')
steebot.run(steebot.token)
