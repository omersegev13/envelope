import random

class Envelope:
    # constructor
    def __init__(self):
        self.used = False
        self.money = random.randint(1, 10001)

    def Open(self):
        """
        returns the amount of money in the envelope
        """
        self.used = True
        return self.money
