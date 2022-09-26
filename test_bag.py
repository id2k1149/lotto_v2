from bag import Bag, EmptyBagError
from pytest import raises


class TestBag:
    def setup(self):
        self.bag = Bag(3)

    def test_init(self):
        assert self.bag._numbers == [1, 2, 3]

    def test_len(self):
        assert len(self.bag) == 3

    def test_get_random_numbers(self):
        random_numbers = self.bag.get_random_numbers(2)
        assert len(random_numbers) == 2
        for each in random_numbers:
            assert each in self.bag._numbers

    def test_get_next_barrel(self):
        old_numbers = self.bag._numbers[:]
        barrel = self.bag.get_next_barrel()
        assert len(self.bag) == 2
        assert barrel in old_numbers

        self.bag.get_next_barrel()
        self.bag.get_next_barrel()
        with raises(EmptyBagError):
            barrel = self.bag.get_next_barrel()

