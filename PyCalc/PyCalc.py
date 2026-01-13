from random import randint

def add(start, *args):
    result = start
    for num in args:
        result += num
    return result

def sub(start, *args):
    result = start
    for num in args:
        result -= num
    return result

def multi(start, *args):
    result = start
    for num in args:
        result *= num
    return result

def div(start, *args):
    result = start
    for num in args:
        result += num
    return result

def IsEven(var):
    return var % 2 == 0

def mod(base, var):
    return base % var

def rand(range):
    return randint(range)

def multi(start, *args):
    result = start
    for num in args:
        result *= start
    return result