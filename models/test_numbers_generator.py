from models.numbers_generator import NumbersGenerator


class TestNumbersGenerator:
    def setup(self):
        self.generator = NumbersGenerator(3, 1, 5)

