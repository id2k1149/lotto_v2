from numbers_generator import NumbersGenerator


class Card:

    def __init__(self):
        total_numbers = 90
        rows = 3
        cols = 9
        generator = NumbersGenerator(total_numbers, rows, cols)
        self.numbers = generator.random_numbers
        self.numbers_after_cross_out = self.numbers.copy()
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
            index_to_delete = self.numbers_after_cross_out.index(item)
            self.numbers_after_cross_out.pop(index_to_delete)
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

    def is_empty(self):
        if len(self.numbers_after_cross_out) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    card = Card()
    print(card)
    print(*card.numbers)
    # number = card.numbers[0]
    # card.cross_out(number)
    # for each in card.numbers:
    #     card.cross_out(each)
    print(card)
    print(card.is_empty())

