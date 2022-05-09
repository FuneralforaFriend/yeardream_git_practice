#%%
import random as rd
doors = ['goat',
         'goat',
         'car',
         ]

player1_wins = 0
player2_wins = 0

for i in range(1, 1000+1):    
    player_choice = rd.choice(doors)
    player1_choice = player_choice
    player2_choice = player_choice

    player1 = True
    player2 = False

    players = [player1, player2]


    if player1:
        for i in doors:
            if i != player1_choice:
                player1_choice = i
                break

    if player1_choice == 'car':
        player1_wins += 1
    if player2_choice == 'car':
        player2_wins += 1

print(player1_wins, player2_wins)
# %%