'''docstring'''
import random


class Product:
    '''class docstring'''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        '''function docstring'''
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        '''function docstring'''
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."
        elif product >= 10 and product < 50:
            return "...boom!"
        else:
            return "...BABOOM!"

    def __repr__(self):
        return f'<Product:{self.name}>'


class BoxingGlove(Product):
    '''class docstring'''

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        '''class docstring'''
        if self.weight < 5:
            return "That tickles."

        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
