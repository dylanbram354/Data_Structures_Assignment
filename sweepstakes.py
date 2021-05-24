import random


class Sweepstakes:
    def __init__(self):
        self.contestants = {
            1: 'Bob Smith',
            2: 'Smith Bob',
            3: 'Jane Doe',
            4: 'John Doe',
            5: 'Play Doh'
        }

    def pick_winner(self):
        key = random.randint(1, 5)
        winner = self.contestants[key]
        print(winner)
