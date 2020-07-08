from game_bot import GameCog

# For each new GameCog, import the class here
from cog_extensions.maths_game import MathsGame
from cog_extensions.other_games import OtherGames
from cog_extensions.fruit_game import FruitGame

# Add the new game classes onto the end of this list
class Games(GameCog, MathsGame, OtherGames, FruitGame):
  game_command_prefix = '!'
  pass

def setup(client):
  client.add_cog(Games(client))

