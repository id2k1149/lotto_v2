from card import Card


class TestCard:
    def setup(self):
        self.card = Card()

    def test_cross_out(self):
        self.card.cross_out(99)
