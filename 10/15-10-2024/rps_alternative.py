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
        
        match player_move:
            case 'q':
                print('Shutting down...')
                sys.exit()
            case 'r' | 'p' | 's':
                break
            case _:
                print('Type one between "r", "p", "s" or "q"')
    
    # Display player's move
    match player_move:
        case 'r':
            print('ROCK versus...')
        case 'p':
            print('PAPER versus...')
        case 's':
            print('SCISSORS versus...')
    
    # Display computer's mvoe       
    computer_move = random.choice(['r', 'p', 's'])
    match computer_move:
        case 'r':
            print('ROCK')
        case 'p':
            print('PAPER')
        case 's':
            print('SCISSORS')


    matches={"r": "s", "p": "r", "s": "p"}
    # updates scoreboard
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (matches[player_move] == computer_move):
    # elif (player_move == 'r' and computer_move == 's') or \
    #      (player_move == 'p' and computer_move == 'r') or \
    #      (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1 

            
            
# parser = argparse.ArgumentParser()
# parser.add_argument('command', choices=['push', 'pull', 'commit'])
# args = parser.parse_args()

# match args.command:
#     case 'push':
#         print('pushing')
#     case 'pull':
#         print('pulling')
#     case _:
#         parser.error(f'{args.command!r} not yet implemented')