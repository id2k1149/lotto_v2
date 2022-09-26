from card import Card
from cross_out_error import CrossOutError
from pytest import raises


class TestCard:
    def setup(self):
        self.card = Card
        numbers_on_card = self.card.get_numbers(self)
        print(numbers_on_card)

    def test_cross_out(self):
        with raises(CrossOutError):
            self.card.cross_out(99)
