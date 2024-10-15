import random
import sys

print("LET'S PLAY ROCK PAPER SCISSORS!")

# Storing data about wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print(f"Wins: {wins} - Losses: {losses} - Ties: {ties}")
    
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or press (q) to quit")
        player_move = input().lower()  
        if player_move == 'q':
            print('Shutting down...')
            sys.exit()
        if player_move in ['r', 'p', 's']:
            break
        print('Type one of r, p, s, or q.')
    
    # Display player's move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    
    # Generate computer's move
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    else:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
