import random


class EmptyBagError(ValueError):
    def __str__(self):
        return "There are no barrels in bag"


class Bag:
    def __init__(self, total_numbers):
        self._numbers = list(range(1, total_numbers + 1))

    def __len__(self):
        return len(self._numbers)

    def get_random_numbers(self, total_numbers):
        result = random.sample(self._numbers, total_numbers)
        return result

    def get_next_barrel(self):
        try:
            result = random.choice(self._numbers)
        except IndexError:
            raise EmptyBagError
        else:
            self._numbers.remove(result)
            return result
