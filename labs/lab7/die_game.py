import random

def roll_die():
    return random.randint(1, 6)


def player_turn(player_name, other_player, player_score):
    option = 'r'
    print(f'\n*******{player_name}\'s turn********\n')
    while option == 'r':
        score1 = roll_die()
        score2 = roll_die()
        score3 = roll_die()
        print(f'Scores: {score1}, {score2}, and {score3}.')
        #player_score += score1 + score2 + score3
        if score1 == 2 or score2 == 2 or score3 == 2:
            player_score = 0
            print(f'{player_name} got at least one 2.')
            print(f'{player_name}\'s score: {player_score} ')
            input(f'\nPress <enter> to continue ...')
            return player_score
        else:
            player_score += score1 + score2 + score3
            print(f'{player_name}\'s score: {player_score} ')
            print()
            if player_score > 18:
                return player_score
            else:
                option = input('(p)ass or (r)oll? ')
            print()
    return player_score


def main():
    player1_name = input('Enter the first player name: ')
    player2_name = input('Enter the second player name: ')
    print()
    player1_score = 0
    player2_score = 0

    while True:
        if player1_score > 18 or player2_score > 18:
            break
        player1_score = player_turn(player1_name, player2_name, player1_score)
        player2_score = player_turn(player2_name, player1_name, player2_score)


    if player1_score > player2_score:
        print(f'{player1_name} wins with a score of {player1_score}')
    elif player2_score > player1_score:
        print(f'{player2_name} wins with a score of {player2_score}')
    else:
        print('Both players got the same score')
        print(f'{player1_name}: {player1_score} scores')
        print(f'{player2_name}: {player2_score} scores')


if __name__ == '__main__':
    main()
