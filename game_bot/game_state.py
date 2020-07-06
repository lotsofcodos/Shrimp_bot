class GameState(object):
  def __init__(self, user, game, initial_state):
    self.user = user
    self.game = game
    self.active = False
    self.current_state = initial_state
    self.current_turn = 0
    self.score = 0
    self.new_game = True