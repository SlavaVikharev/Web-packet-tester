import json
import random


class Test:

    def __init__(self, fields):
        self.hex = fields.get('hex')
        fields = list(fields.items())
        random.shuffle(fields)
        self.fields = dict(item for item in fields
                           if item[0] != 'hex')

    @staticmethod
    def filter(value):
        return value.lower().strip().replace(' ', '')

if __name__ == '__main__':
    with open('tests.json', 'r') as f:
        tests = json.load(f)
        random.shuffle(tests)

    while True:
        for test in map(Test, tests):
            print('=' * 50)
            print('Hex:\n')
            print(test.hex)
            for field in test.fields:
                ans = input('Input %s:\n' % field)
                if Test.filter(ans) == Test.filter(test.fields[field]):
                    print('You are my hero ^_^\n')
                else:
                    print('Are you stupid or something?')
                    print('%s: %s' % (field.upper(), test.fields[field]))
        random.shuffle(tests)
