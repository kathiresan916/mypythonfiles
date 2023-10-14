"""Roll a Dice"""

import random


class Dice:
    """Dice Function"""

    def roll(self):
        """Call Random Roll"""
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
result = dice.roll()
print(result)
