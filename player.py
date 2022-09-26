import random
from card import Card


class Player:
    def __init__(self, is_human):
        self.is_human = is_human
        self.player_card = Card()

    def ask_question(self, number):
        if self.is_human:
            self.player_card.check_number_in_card(number)
        else:
            self.player_card.cross_out(number)


if __name__ == '__main__':
    player = Player(False)
    if player.is_human:
        print('Human')
    else:
        print('CPU')
    print(player.player_card)
    print(player.player_card.numbers)
    for each in player.player_card.numbers:
        player.ask_question(each)
    print(player.player_card)
