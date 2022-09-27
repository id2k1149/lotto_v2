from models.bag import Bag
from models.card import Card
from models.player import create_player


def is_continue_game(players):
    for each in players:
        if not (each.is_winner is None):
            return False
    return True


bag = Bag(90)
player_count = int(input('Input number of players '))
players = []
for i in range(player_count):
    name = input(f'Enter player name {i + 1} ')
    player_type = input(f'Enter player type. CPU - 1, Human - 0 ')
    card = Card()
    player = create_player(name, player_type, card)
    players.append(player)

while is_continue_game(players):
    barrel = bag.get_next_barrel()
    print(barrel)
    for player in players:
        print(player.card)
        player.turn(barrel)


has_winner = False
has_looser = False
for player in players:
    if player.is_winner is None:
        pass
    else:
        if player.is_winner:
            has_winner = True
        else:
            has_looser = True


if has_winner:
    for player in players:
        if player.is_winner:
            print(player.name, 'win!')
        else:
            print(player.name, 'loose!')
elif has_looser:
    for player in players:
        if player.is_winner is None:
            print(player.name, 'win!')
        else:
            print(player.name, 'loose!')
    print()
else:
    print('Error')




