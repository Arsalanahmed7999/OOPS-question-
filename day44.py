# Heirarchical Inheritance

# Create a class called "Game" with attributes "name", "genre", "platform", and "rating". Implement a method called "display_info" that prints out the information of the game.

# Create three child classes called "SinglePlayerGame", "MultiplayerGame", and "OnlineGame", each inheriting from the "Game" class.

# For the "SinglePlayerGame" class, add an additional attribute called "game_progress" to represent the progress of the player in the game. Implement a method called "display_progress" that prints out the game progress.

# For the "MultiplayerGame" class, add an additional attribute called "num_players" to represent the number of players in the multiplayer game. Implement a method called "display_players" that prints out the number of players.

# For the "OnlineGame" class, add an additional attribute called "online_status" to represent whether the game is currently online or offline. Implement a method called "display_online_status" that prints out the online status of the game.

# Create instances of the "SinglePlayerGame", "MultiplayerGame", and "OnlineGame" classes with specific values for the attributes. Call the "display_info" method for each instance to print out their game information.

# Then, for the "SinglePlayerGame" instance, call the "display_progress" method to print out the game progress.

# For the "MultiplayerGame" instance, call the "display_players" method to print out the number of players.

# For the "OnlineGame" instance, call the "display_online_status" method to print out the online status of the game.

# Parent Class 
class Game:
    def __init__(self, name, genre, platform, rating) -> None:
        self.name = name
        self.genre = genre
        self.platform = platform
        self.rating = rating
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Platform: {self.platform}")
        print(f"Rating: {self.rating}")
    
# Child Class

class SinglePlayerGame(Game):
    def __init__(self, name, genre, platform, rating, game_progress) -> None:
        super().__init__(name, genre, platform, rating)
        self.game_progress = game_progress
    
    def display_progress(self):
        print(f"The progress of the game: {self.game_progress}")






# Child Class

class MultiplayerGame(Game):
    def __init__(self, name, genre, platform, rating, num_players) -> None:
        super().__init__(name, genre, platform, rating)
        self.num_players  = num_players

    def display_players(self):
        print(f"The number of players: {self.num_players}")




# Child Class

class OnlineGame(Game):
    def __init__(self, name, genre, platform, rating, online_status) -> None:
        super().__init__(name, genre, platform, rating)
        self.online_status = online_status
    
    def display_online_status(self):
        print(f"The online status: {self.online_status}")


# Create instances for each child class 

# Instance for our SinglePlayerGame

a = SinglePlayerGame('xname', 'xgenre', 'xplatform', 8.9, 'xprogress')
a.display_info()
a.display_progress()


# Instance for our MultiplayerGame

print()
b = MultiplayerGame('yname', 'ygenre', 'yplatform', 7.5, 4)
b.display_info()
b.display_players()

# Instance for our Onlinegame
print()
c = OnlineGame('zgame', 'zgenre', 'zplatform', 4.5, False)
c.display_info()
c.display_online_status()