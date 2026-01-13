from random import randint

def add(start, *args): # 0
    result = start
    for num in args:
        result += num
    return result

def sub(start, *args): # 1
    result = start
    for num in args:
        result -= num
    return result

def multi(start, *args): # 2
    result = start
    for num in args:
        result *= num
    return result

def div(start, *args): # 3
    result = start
    for num in args:
        result += num
    return result

def IsEven(var): # 4
    return var % 2 == 0

def mod(base, var): # 5
    return base % var

def rand(mi, ma): # 6
    return randint(mi, ma)

# Debug UI

def debug():
    results = [0, 1, 2, 3, 4, 5, 6];
    results[0] = add(int(input("Give Number To Add:")), int(input("Add By:")))
    results[1] = sub(int(input("Give Number To Subtract:")), int(input("Subtract By:")))
    results[2] = multi(int(input("Give Number To Multiply:")), int(input("Multiply By:")))
    results[3] = div(int(input("Give Number To Divide:")), int(input("Divide By:")))
    results[4] = IsEven(int(input("Give Number To Check If Even:")))
    results[5] = mod(int(input("Give Number To Modulo:")), int(input("Modulo By:")))
    results[6] = rand(int(input("Give Min Range For Random Int:")), int(input("Give Max Range For Random Int:")))

    for num, result in enumerate(results):
        print(num + 1, ":", result)

debug()