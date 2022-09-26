import random


class NumbersGenerator:
    def __init__(self, total_numbers, rows, cols):
        self.random_numbers = []
        self.numbers_on_card = [['  ' for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            counter = 0
            while counter < 5:
                number = random.randint(1, total_numbers)
                if number not in self.random_numbers:
                    cols_index = 8 if int(number) == 90 else int(number) // 10
                    if self.numbers_on_card[i][cols_index] == '  ':
                        if i == 2:
                            if (self.numbers_on_card[i - 1][cols_index] != '  ') and (
                                    self.numbers_on_card[i - 2][cols_index] != '  '):
                                continue
                        self.random_numbers.append(number)
                        if number < 10:
                            number_on_card = ' ' + str(number)
                        else:
                            number_on_card = str(number)
                        self.numbers_on_card[i][cols_index] = number_on_card
                        counter += 1
                else:
                    continue


if __name__ == '__main__':
    generator = NumbersGenerator(90, 3, 9)
    print(generator.random_numbers)
    print(generator.numbers_on_card)
