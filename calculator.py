import math

'''a'''


def power(a, b):
    return a ** b


'''b'''


def sqrt(a):
    return math.sqrt(a)


'''c'''


def factorial(a):
    try:
        return math.factorial(a)
    except ValueError:
        print('factorial() not defined for negative values')
