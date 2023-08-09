# Multilevel -
# Create a class called "Game" with attributes "title" and "genre". Implement a method called "display_info" that prints out the title and genre of the game.

# Create a child class called "VideoGame" that inherits from the "Game" class. Add an additional attribute called "platform" to represent the gaming platform of the video game (e.g., PC, Xbox, PlayStation). Implement a method called "display_platform" that prints out the gaming platform of the video game.

# Create a grandchild class called "RPG" that inherits from the "VideoGame" class. Add an additional attribute called "character_level" to represent the level of the player's character in the RPG game. Implement a method called "display_character_level" that prints out the character level of the player.

# Create an instance of the "RPG" class with specific values for the title, genre, gaming platform, and character level. Call the "display_info", "display_platform", and "display_character_level" methods to print out the information of the RPG game.

# Parent class

class Game:
    def __init__(self, title, genre) -> None:
        self.title = title
        self.genre = genre

    def display_info(self):
        print(f'Title: {self.title}\nGenre: {self.genre}')


#  Child Class 1
class VideoGame(Game):
    def __init__(self, title, genre, platform) -> None:
        super().__init__(title, genre)
        self.platform = platform

    def display_platform(self):
        print(f"Platform: {self.platform}")
        
        
# Child Class 2

class RPG(VideoGame):
    def __init__(self, title, genre, platform, character_level) -> None:
        super().__init__(title, genre, platform)
        self.character_level = character_level
    
    def display_character_level(self):
        print(f"Character Level: {self.character_level}")

# a = RPG('xtitle', 'xgenre', 'XBOX', 10)
# (a.display_info())
# (a.display_platform())
# (a.display_character_level())


b = Game('ytitle', 'ygenre')
b.display_info()
b.display_platform()
