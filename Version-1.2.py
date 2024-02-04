#!/usr/bin/python3

from colorama import Fore, Style, init

# SCORING FUNCTION
def scoring_function():
    for player in player_scores:
        while True:
            try:
                add_points = int(input(f"How many points for {player}? "))
            except ValueError:
                print (f"Invalid input!")
                continue
                # continue will make it go back to the top of the function
            else:
                break
                # this will exit the loop
        player_scores[player] += add_points

# This is old code I didn't want to delete. This made it so everything in the new code happens except for the fact that this gave a ValueError when inputting a string or float.
        # add_points = int(input(f"How many points did {player} get this round? "))
        # if add_points is str:
        #     int(input(f"Invalid input! Please input the number of points {player} got this round! "))
        # if add_points is float:
        #     int(input(f"Invalid input! Please input the number of points {player} got this round! "))
        # if add_points is int:
        #     player_scores[player] += add_points

    for player in player_scores:
        if player_scores[player] == 50:
            player_scores[player] = 0
            
    for player in player_scores:
        if player_scores[player] == 100:
            player_scores[player] = 50 

# WHO IS PLAYING?
player_scores = {}
name = input("Enter a name. ")
player_scores.update({name: 0})

while name:
    player_scores[name] = 0
    name = input("Enter a name. ")

# GAME LOOP        
game_over = False
while not game_over:
    for player in player_scores:
        if player_scores[player] >= 100:
            game_over = True
            break
    else:
        print(f"{str(player_scores)}")
        scoring_function()

print(Fore.RED + f"THE GAME IS OVER!")
min_score = min(player_scores.values())
winner = [key for key in player_scores if player_scores[key] == min_score] 
print (Fore.RED + f"THE WINNER IS {str(winner)}")
print (Fore.RED + f"THE FINAL SCORE IS {str(player_scores)}")

input ("Enter to close the game. ")
