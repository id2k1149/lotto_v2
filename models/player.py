from models.card import Card


class CPUPlayer:

    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.is_winner = None

    def turn(self, number):
        if number in self.card:
            self.card.cross_out(number)
            if self.card.is_empty():
                self.is_winner = True


class HumanPlayer(CPUPlayer):

    def turn(self, number):
        answer = input('Cross out? y/n ')
        if answer == 'y':
            if number in self.card:
                self.card.cross_out(number)
                if self.card.is_empty():
                    self.is_winner = True
            else:
                self.is_winner = False
        else:
            if number in self.card:
                self.is_winner = False


CPU = 'CPU'
HUMAN = 'HUMAN'


def create_player(name, player_type, card):
    players = {
        '1': CPUPlayer,
        '0': HumanPlayer
    }
    player = players[player_type](name, card)
    return player


if __name__ == '__main__':
    card = Card()
    player = CPUPlayer('CPU', card)
    print(player.name, player.is_winner)
    for each in card.numbers:
        player.turn(each)
    print(player.name, player.is_winner)