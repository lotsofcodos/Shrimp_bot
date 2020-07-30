import random
import discord
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

hangman_game_flow = {
'start':          [
                    ('connect_to', 'ask_level'),
                  ],
'ask_level': [
                    ('connect_to', 'is_level_valid'),
                  ],
'is_level_valid': [
                    ('is_level_valid', 'game_setup'),
                    ('connect_to', 'wrong_level'),
                  ],
'wrong_level': [
                    ('connect_to', 'ask_level'),
                  ],
'check_guess':    [
                    ('has_game_finished', 'show_score'),
                    ('connect_to', 'guess_again'),
                  ],
'guess_again':    [
                    ('connect_to', 'check_guess'),
                  ],
'show_score':     [   
                    ('connect_to', 'end'),
                  ],
}




hangman_custom_help = {'clue': 'hangman_clue'}

class HangmanGame(object):

  @commands.group(invoke_without_command=True)
  @start_game(game_flow = hangman_game_flow, custom_help = hangman_custom_help)
  def hangman(self,message, state=None):
    """guess the word game"""
    state.current_state = 'start'
    response = f"""
              Welcome to the Hangman {message.author.name}!
              You can use !help during the game for ingame help and advisement.
              """
    state.score = 0
    state.level= None
    state.current_go = 1
    #state.number_of_goes_allowed = 6
    state.letters_guessed = []
    return response

  @wait_for_player_response
  def ask_level(self,message, state):
    response = "Which level do you want? 1, 2 or 3? " 

    return response

  def is_level_valid(self,message,state):
    # player has just entered their level
    state.level = message.content
    # make a decision if it's valid
    if state.level in ['1','2','3']:
      return True
    else:
      return False
    
  def wrong_level(self, message,state):
    return "The level input that you have typed is invalid."

    

  def game_setup(self, message, state):
    pass

  def show_fruitbowl(self, message, state):
    response = '  '.join([':'+f+':' for f in state.fruit])
    state.start_timer(10)
    state.player_guessed_early = 0
    state.start_guessing = False
    return self.disappearing_response(response, 10)
  
  @wait_for_player_response
  def fruit_display_timer(self, message, state):
    response = None
    if state.has_timer_expired():
      state.start_guessing = True
      response = self.check_guess(message, state)
      response += "\nGuess again"
    elif state.player_guessed_early > 0:
      response = f"wait ..... it's not disappearing yet ...."
    state.player_guessed_early += 1

    return response

  def is_timer_active(self, message, state):
    if not state.start_guessing:
      return True
    return False
  
  def check_guess(self, message, state):
    guess = message.content
    if guess in state.fruit and guess not in state.fruit_guessed:
      response = f":{guess}: Correct!!"
      state.score += 2
      state.fruit_guessed.append(guess)
    elif guess in state.fruit and guess in state.fruit_guessed:
      response = f"You already guessed :{guess}:"
    else:
      response = f"Nope. {guess} is not in my bowl"
    
    state.number_of_goes += 1
    return response
  
  def has_game_finished(self, message, state):
    if state.number_of_goes > state.number_of_goes_allowed:
      return True
    if len(state.fruit) == len(state.fruit_guessed):
      return True
    return False
  
  @wait_for_player_response
  def guess_again(self, message, state):
    return "Guess another one"
  
  def show_score(self, message, state):
    response = "\n\nGame Over\n\n"
    all_fruit = '  '.join([':'+f+':' for f in state.fruit])
    fruit_not_guessed = '  '.join([':'+f+':' for f in self.unguessed_fruit(state)])
    fruit_guessed_correctly = '  '.join([':'+f+':' for f in state.fruit_guessed])
    if len(state.fruit) == len(state.fruit_guessed):
      response += "Congratulations!!! You remembered all the fruit\n"
      response += all_fruit
    elif len(state.fruit_guessed)==0:
      response += f"You didn't remember a single thing!  Here's my bowl:\n"
      response += all_fruit
    else:
      response += f"You remembered {len(state.fruit_guessed)} correctly!  {fruit_guessed_correctly}\nHere's the rest of my bowl:\n"
      response += fruit_not_guessed
    
    response += f"\nYour score is {state.score}"

    if state.score != 2* len(state.fruit_guessed):
      response += "\n(you had some points deducted because you asked for a clue)"
    
    return response

  def unguessed_fruit(self, state):
    return ([f for f in state.fruit if f not in state.fruit_guessed])

  def fruit_clue(self, message, state):
    """Gives a hint about what the fruit might be"""
    state.score += -1
    return fruit_clues[random.choice(self.unguessed_fruit(state))]

  
  