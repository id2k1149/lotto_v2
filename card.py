import random


def get_random_numbers():
    rows, cols = (3, 9)
    random_numbers = []
    numbers_on_card = [['  ' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        counter = 0
        while counter < 5:
            number = random.randint(1, 90)
            if number not in random_numbers:
                cols_index = 8 if int(number) == 90 else int(number) // 10
                if numbers_on_card[i][cols_index] == '  ':
                    if i == 2:
                        if (numbers_on_card[i - 1][cols_index] != '  ') and (
                                numbers_on_card[i - 2][cols_index] != '  '):
                            continue
                    random_numbers.append(number)
                    if number < 10:
                        number_on_card = ' ' + str(number)
                    else:
                        number_on_card = str(number)
                    numbers_on_card[i][cols_index] = number_on_card
                    counter += 1
            else:
                continue

    return random_numbers, numbers_on_card


class Card:

    def __init__(self):
        random_numbers, numbers_on_card = get_random_numbers()
        self.numbers = random_numbers
        self.numbers_on_card = numbers_on_card

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

