from card import Card


class TestCard:
    def setup(self):
        self.card = Card()

    def test_cross_out(self):
        self.card.cross_out(99)

    def test_is_empty(self):
        assert not self.card.is_empty()
        for each in self.card.numbers:
            self.card.cross_out(each)
        assert self.card.is_empty()
