from textwrap import dedent
import discord
from discord.ext import commands

from . import wait_for_player_response

class GameCog(commands.Cog):

  game_command_prefix = ''

  built_in_game_help = ['help', 'pause', 'quit']
  custom_game_help = []

  def __init__(self, client):
    self.client = client
    self.users = self.client._users
    self.game_flow = {}
  
  @commands.Cog.listener()
  async def on_message(self, message):
    
    state = self.users.get_active_game(message.author.id)
    
    if state is None:
      return
    
    help_commands = self.__help_commands()
    if message.content in help_commands:
      response = getattr(self, help_commands[message.content])(message, state)
      if response is not None:
        await message.channel.send(dedent(response))
      return
    
    if not message.content.startswith('.'):
      state.current_turn += 1
      await self.execute_game_flow(message, state)
      
  async def execute_game_flow(self, message, state):
      loop_count = 0
      while True:
        loop_count +=1
        if loop_count>50:
          raise RunTimeError('Logic is not exiting - check flow')
          break
        response = self.do_next_game_action(message, state)
        if len(response)==2:
          if response[0]:
            await message.channel.send(dedent(response[1]))
          break
        if response is not None:
          await message.channel.send(dedent(response))


  def __help_commands(self):
    return {self.game_command_prefix+c:c for c in\
                    self.built_in_game_help + self.custom_game_help}

  # Builtin game commands
  def help(self, message, state):
    """Shows this help message"""
    response = f'In game help for {state.game}:\n\n'
    for cmd, func in self.__help_commands().items():
      response += f"{cmd}\t\t\t{getattr(self,func).__doc__}\n"

    return response

  def quit(self, message, state):
    """Stop playing"""
    self.custom_game_help = []
    self.users.remove_game(state.user, state.game)
    return f'{message.author.name} no longer playing {state.game}'

  def pause(self, message, state):
    """Pause playing"""
    state.active = False
    self.custom_game_help = []
    return f'{message.author.name} has paused the {state.game}.  Type .{state.game} to resume'

  def connect_to(self, message, state):
    return True

  def otherwise(self, message, state):
    return True


  def do_next_game_action(self, message, state):
    response = None
    for exit_logic, next_state in self.game_flow[state.game][state.current_state]:
      move_on = getattr(self, exit_logic)(message, state)
      if move_on:
        response = getattr(self, next_state)(message, state)
        state.current_state = next_state
        break
    return response

  @wait_for_player_response
  def demo_q1(self, message, state):
    return (f'{message.author.name} is playing {state.game} and is on turn {state.current_turn}')

  def end(self, message, state):
    return((False, self.quit(message, state)))
  

  @commands.group(invoke_without_command=True)
  async def my_games(self,ctx):
    """Shows any games in progress"""
    games = self.users.get_all_games(ctx.message.author.id)

    if games is None:
      await ctx.send(f'No games in progress for {ctx.message.author}')
      return
    
    active = [g.game for g in games if g.active]
    inactive = [g.game for g in games if not g.active]
    
    active = [g.game for g in games if g.active]
    inactive = ','.join([g.game for g in games if not g.active])

    active = [g.game for g in games if g.active]
    inactive = ', '.join([g.game for g in games if not g.active])
    response = f'Paused Games for {ctx.message.author}: {inactive}'
    if len(active)==1:
      if response != '': response += ' and '
      response += f'game {active[0]} is currently active'
    await ctx.send(response)