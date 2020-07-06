import os
from game_bot import BotFactory, keep_alive

keep_alive()
bot_token = os.getenv("TOKEN")
bot = BotFactory('cog_extensions', ('mini_games', 'admin', 'game_cogs'))
bot.run(bot_token)
