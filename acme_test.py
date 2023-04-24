import pytest

from acme import Product


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_stealability():
    '''Test stealability'''
