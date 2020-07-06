import os
from game_bot import BotFactory, keep_alive

keep_alive()
bot_token = os.getenv("BOT_TOKEN")
bot = BotFactory('bot_functions', ('guess', 'hangman', 'game_cogs'))
bot.run(bot_token)
