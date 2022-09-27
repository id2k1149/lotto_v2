from card import Card


class CrossOutError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"The card doesn/'t  contain number {self.number}"
