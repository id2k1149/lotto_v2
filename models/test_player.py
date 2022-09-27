from models.player import CPUPlayer
from models.card import Card


class TestCPUPlayer:

    def setup(self):
        card = Card()
        self.cpu_player = CPUPlayer('CPU', card)

    def test_turn(self):
        assert self.cpu_player.is_winner is None
        for each in self.cpu_player.card.numbers:
            self.cpu_player.turn(each)
        assert self.cpu_player.is_winner is True
