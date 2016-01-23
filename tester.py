import os
import random
from parser import Parser


class Test:

    def __init__(self, fields):
        self.hex = fields.get('hex')
        if self.hex is None:
            return
        fields = list(fields.items())
        random.shuffle(fields)
        self.fields = dict(item for item in fields if item[0] != 'hex')

    @staticmethod
    def filter(value):
        return value.lower().strip().replace(' ', '')


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def ask_question(test, field):
    clear_screen()
    print('=' * 50)
    print('Hex:\n')
    print(test.hex)
    ans = input('Input %s:\n' % field)
    if Test.filter(ans) == Test.filter(test.fields[field]):
        print('Correct!\n')
    else:
        print('Wrong.')
        print('%s: %s' % (field, test.fields[field]))


TESTS_DIR = 'tests'

if __name__ == '__main__':
    test_files = os.listdir(TESTS_DIR)
    random.shuffle(test_files)
    while True:
        for file in test_files:
            file = open(os.path.join(TESTS_DIR, file))
            tests = Parser.parse(file)
            random.shuffle(tests)
            for test in filter(bool, map(Test, tests)):
                for field in test.fields:
                    ask_question(test, field)
                    input('Press any key')
            file.close()
        random.shuffle(test_files)
