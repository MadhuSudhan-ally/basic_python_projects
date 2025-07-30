#the pig dice game!
import random

game_map = {1:[], 2:[]}

class Game:
    def __init__(self, player_id, points):
        self.player_id = player_id
        self.points = points
    
    def roll_again(self):
        choice = input("Roll again? (y/n): ").lower()
        if choice == 'y' or choice == 'n':
            return choice
        
    def change_player(self, player_id):
        if player_id == 1:
            return  2
        else:
            return 1

    def current_score(self, player_id):
        return sum(game_map[player_id])
    
    def check_winner(self, player_id):
        if self.current_score(player_id) >= 50:
            print(f"Player {player_id} is the winner!")
            return True
        else:
            pass
    
    def logic(self):
        while True:
            print(f"\nPlayer {self.player_id}'s turn")
            result = random.randint(1,6)
            if result == 1:
                print("You rolled a 1")
                game_map[self.player_id] = []
                print(f'Current score = {self.current_score(self.player_id)}')

                self.player_id = self.change_player(self.player_id)
                
            else:
                game_map[self.player_id].append(result)
                print(f"You rolled a {result}\nCurrent score = {self.current_score(self.player_id)}")
                if self.check_winner(self.player_id):
                    break
                else:
                    if self.roll_again() == 'y':
                        self.logic()
                    else:
                        self.player_id = self.change_player(self.player_id)

                    
player = Game(1, 0)
player.logic()



