# pylint: disable=invalid-name
'''docstring'''
import random
from acme import Product

# Useful to use with random.sample or random.choice to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''docstring'''
    products = []
    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)
    return products


def inventory_report(products):
    '''docstring'''
    names = []
    prices = []
    weights = []
    flammabilities = []

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    num_unique_names = len(set(names))
    avg_price = sum(prices) / len(prices)
    avg_weight = sum(weights) / len(weights)
    avg_flammability = sum(flammabilities) / len(flammabilities)
    return num_unique_names, avg_price, avg_weight, avg_flammability


if __name__ == '__main__':
    print(inventory_report(generate_products()))
