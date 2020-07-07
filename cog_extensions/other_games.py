import discord
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

vanish_game_flow = {
    'start': [
              ('connect_to', 'embed_test'),
              ],
    'embed_test': [
              ('connect_to', 'disappear'),
              ],
    'disappear': [
              ('connect_to', 'end'),
              ],
  }

fruit_game_flow = {
    'start': [
              ('connect_to', 'embed_test'),
              ],
    'embed_test': [
              ('connect_to', 'disappear'),
              ],
    'disappear': [
              ('connect_to', 'end'),
              ],
  }



class OtherGames(object):

  @commands.group(invoke_without_command=True)
  @start_game(game_flow = fruit_game_flow)
  def fruit(self,message, state=None):
    """Game number 2"""
    return None

  
  @commands.group(invoke_without_command=True)
  @start_game(game_flow = vanish_game_flow)
  def vanish(self,message, state=None):
    """A game that just disappears for no reason"""
    return None

  def embed_test(self, message, state):
    embed = self.make_embed(title='Hangman', 
                            description='Play hangman with me',
                            colour=0x3615c4,
                            author=message.author.name,
                            icon="https://cdn.statically.io/gh/connectedblue/pylearn/0d90038e/images/hangman.png",
                            thumbnail="https://cdn.statically.io/gh/connectedblue/pylearn/0d90038e/images/hangman.png",
                            footer = "(c) 2020",
            fields=[
              {
                  'name': "last letter guessed", 
                  'value': "Y",
                  'inline': False
              },
              {
                  'name': "Word to guess", 
                  'value': "\- D D - - E",
                  'inline': True
              },
              ])

    return self.disappearing_response(embed, 15)

  def disappear(self, message, state):
    return self.disappearing_response("This will disappear soon", 10) 

