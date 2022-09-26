from numbers_generator import NumbersGenerator


class Card:

    def __init__(self):
        total_numbers = 90
        rows = 3
        cols = 9
        generator = NumbersGenerator(total_numbers, rows, cols)
        self.numbers = generator.random_numbers
        self.numbers_on_card = generator.numbers_on_card

    def __str__(self):
        result = f"""
-----card numbers---------
{' '.join(self.numbers_on_card[0])}
{' '.join(self.numbers_on_card[1])}
{' '.join(self.numbers_on_card[2])}
--------------------------
                """
        return result

    def __contains__(self, item):
        return item in self.numbers

    def get_numbers(self):
        return self.numbers

    def cross_out(self, item):
        if item in self.numbers:
            number_index = self.numbers.index(item)
            cols_index = 8 if int(item) == 90 else int(item) // 10
            if number_index < 5:
                row = 0
                self.numbers_on_card[row][cols_index] = '--'
            elif 4 < number_index < 10:
                row = 1
                self.numbers_on_card[row][cols_index] = '--'
            elif number_index > 9:
                row = 2
                self.numbers_on_card[row][cols_index] = '--'


if __name__ == '__main__':
    card = Card()
    print(card)
    print(*card.numbers)
    for each in card.numbers:
        card.cross_out(each)
    print(card)

