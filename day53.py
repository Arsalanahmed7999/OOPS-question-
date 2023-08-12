# --------------------- Polymorphism --------------------------


# ------------------- Question -------------------------


# Create a class hierarchy with a base class "Game" and two subclasses "ActionGame" and "StrategyGame". Implement a method called "play" in each class. Demonstrate polymorphism by creating an array of "Game" objects, including instances of both "ActionGame" and "StrategyGame", and calling the "play" method on each object.


# Parent Class

class Game:
    def play(self):
        pass #we will be overriding this method

# Child Class ActionGame

class ActionGame(Game):
    def play(self):
        print('Playing an action game')

# Child Class Strategy Game

class StrategyGame(Game):
    def play(self):
        print('I am playing a strategy Game')

actiongame1 = ActionGame()
strategygame1 = StrategyGame()

games = [actiongame1, strategygame1]

for game in games:
    game.play()