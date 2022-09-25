import random


def get_random_numbers():
    rows, cols = (3, 9)
    random_numbers = []
    numbers_on_card = [['__' for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        counter = 0
        while counter < 5:
            number = random.randint(1, 90)
            if number not in random_numbers:
                column_index = 8 if int(number) == 90 else int(number) // 10
                if numbers_on_card[i][column_index] == '__':
                    if i == 2:
                        if (numbers_on_card[i - 1][column_index] != '__') and (
                                numbers_on_card[i - 2][column_index] != '__'):
                            continue
                    random_numbers.append(number)
                    if number < 10:
                        number_on_card = '_' + str(number)
                    else:
                        number_on_card = str(number)
                    numbers_on_card[i][column_index] = number_on_card
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
-----card numbers-------
{self.numbers_on_card[0]}
{self.numbers_on_card[1]}
{self.numbers_on_card[2]}
------------------------
                """
        return result


if __name__ == '__main__':
    card = Card()
    print(card)
