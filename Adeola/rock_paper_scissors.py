import random


def decide_win(player):
    options = ['ROCK', 'PAPER', 'SCISSORS']
    computer = random.choice(options)
    if player in options:
        print(f'Player choice is {player}')
        print(f'Computer choice is {computer}')
        if player == computer:
            print('Game ends in a draw.')
        elif player == 'ROCK' and computer == 'PAPER':
            print('Computer wins!')
        elif player == 'PAPER' and computer == 'ROCK':
            print('Players wins!')
        elif player == 'SCISSORS' and computer == 'ROCK':
            print('Computer wins!')
        elif player == 'ROCK' and computer == 'SCISSORS':
            print('Player wins!')
        elif player == 'PAPER' and computer == 'SCISSORS':
            print('Computer wins!')
        elif player == 'SCISSORS' and computer == 'PAPER':
            print('Player wins!')
    else:
        print('Enter rock, paper, or scissors.')


if __name__ == '__main__':
    player_choice = input('Pick rock, paper, or scissors: ')
    player_choice = player_choice.upper()
    decide_win(player_choice)
