# imports
import  os
import discord
from discord.ext import commands
from dummy_web import keep_alive

bot_token = os.getenv("TOKEN")
shrimp = commands.Bot(command_prefix = '.')



@shrimp.command()
async def load(ctx):
  """loads extension"""
  bot.load_extension()
    
@shrimp.command()
async def unload(ctx):
  """unloads extension"""
  bot.unload_extension()

@shrimp.command()
async def reload(ctx):
  """reloads extension"""
  bot.reload_extension()


@shrimp.command()
async def admin(ctx, bot_extension):
    await shrimp.process_commands('cog_extensions.admin')

    # if no mention 
    #await ctx.send (embed=show_avatar of current member)



@shrimp.event
async def on_message(message):
    if message.author == shrimp.user:
        return
    print(f'message from {message.author} who said {message.content} ')
    # process message to see if the author has a survey running


keep_alive()
shrimp.run(bot_token)
 