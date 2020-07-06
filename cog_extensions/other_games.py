from discord.ext import commands
from game_bot import start_game, wait_for_player_response

class OtherGames(object):

  @commands.group(invoke_without_command=True)
  @start_game
  async def game2(self,ctx, state=None):
    """Game number 2"""
    return None

  
  @commands.group(invoke_without_command=True)
  @start_game
  async def game3(self,ctx, state=None):
    """Game number 3"""
    return None