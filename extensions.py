import random
import os


def rand_iter(iterable):
    iterable_copy = list(iterable)
    random.shuffle(iterable_copy)
    return iterable_copy


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


random.iter = rand_iter
os.cls = clear_screen
