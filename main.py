# imports
import  os
import discord
from discord.ext import commands
from dummy_web import keep_alive

bot_token = os.getenv("TOKEN")
shrimp = commands.Bot(command_prefix = '.')


# @shrimp.event
# async def on_ready(ctx):
#     print("bot is ready")

@shrimp.command()
async def load(ctx,bot_extension):
  """loads extension"""
  # if author is izzy, load extension
  # otherwise say not allowed
  
  # author has to be an approved id
  if ctx.message.author.id == 670027514206224404:
    # load the extension and confirm to user
    shrimp.load_extension(f'cog_extensions.{bot_extension}')
    await ctx.send(f'{bot_extension} has loaded')
  else:
    # tell the user they cannot do it
    await ctx.send(f"you can't load {bot_extension} because you don't have permission to")
 

@shrimp.command()
async def unload(ctx,bot_extension):
  """unloads extension"""
  if ctx.message.author.id == 670027514206224404:
    # load the extension and confirm to user
    shrimp.unload_extension(f'cog_extensions.{bot_extension}')
    await ctx.send(f'{bot_extension} has unloaded')
  else:
    # tell the user they cannot do it
    await ctx.send(f"you can't unload {bot_extension} because you don't have permission to")


@shrimp.command()
async def reload(ctx,bot_extension):
  """reloads extension"""
  if ctx.message.author.id == 670027514206224404:
    shrimp.reload_extension(f'cog_extensions.{bot_extension}')
    await ctx.send(f'{bot_extension} has reloaded')
  else:
    # tell the user they cannot do it
    await ctx.send(f"you can't reload {bot_extension} because you don't have permission to")
  

@shrimp.command()
async def load_admin(ctx, bot_extension):
    await shrimp.load_extension('cog_extensions.admin')
    await ctx.send('admin has loaded')

    # if no mention 
    #await ctx.send (embed=show_avatar of current member)

shrimp.load_extension('cog_extensions.mini_games')
shrimp.load_extension('cog_extensions.admin')
shrimp.load_extension('cog_extensions.topic')
shrimp.load_extension('cog_extensions.commands')
@shrimp.event
async def on_message(message):
    if message.author == shrimp.user:
        return
    print(f'message from {message.author} who said {message.content} ')
    # process message to see if the author has a survey running
    await shrimp.process_commands(message)


keep_alive()
shrimp.run(bot_token)
 