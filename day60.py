# --------------------- Polymorphism --------------------------

# ---------------------- Question -----------------------------

# Create a class hierarchy with a base class called "Game" and subclasses "ActionGame", "PuzzleGame", and "SportsGame". Implement a method called "play" in each class, but override it differently in each subclass.

# Now, imagine you have a dictionary where keys are game names and values are instances of different game classes. Your task is to iterate through this dictionary and call the "play" method on each object.

# Describe how the concept of polymorphism is being demonstrated in this scenario, especially when the same method name "play" is being used across different subclasses of the "Game" class.

# Parent Class
class Game:
    def play(self):
        pass #It will be overridden

# Child Class ActionGame

class ActionGame(Game):
    def play(self):
        return 'This is an action game'

# Child Class PuzzleGame

class PuzzleGame(Game):
    def play(self):
        return 'I am solving the puzzle game this time'

# Child Class SportsGame

class SportsGame(Game):
    def play(self):
        return 'Time to play a sports game'
        # return ['1', '2', '3']
    
# Instances of the child classes 

actiongameinstance = ActionGame() 
puzzlegameinstance = PuzzleGame() 
sportsgameinstance = SportsGame() 


games = {
    'actiongame': actiongameinstance,
    'puzzlegame': puzzlegameinstance,
    'sportsgame': sportsgameinstance
}

# print(games['actiongame'].play())

for gameName, gameInstance in games.items():
    print(f"{gameName} : {gameInstance.play()}")















# dictionary = {
#     key : value
# }

# myGrades = {
#     "Maths": 90,
#     "Science": 80,
#     'English':86
# }
# print(myGrades['Maths'])
# print(myGrades['Science'])
# print(myGrades['English'])

# for subject, grades in myGrades.items():
#     print(f'{subject}: {grades}')