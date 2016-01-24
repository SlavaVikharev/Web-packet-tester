import os
import random
import extensions
import glob
import colors
from parser import Parser
from operator import truth


class Test:
    def __init__(self, fields):
        self.hex = fields.get('hex')
        if self.hex is None:
            return
        fields = list(fields.items())
        random.shuffle(fields)
        self.fields = dict(item for item in fields
                           if item[0] != 'hex')

    @staticmethod
    def filter(value):
        return value.lower().strip().replace(' ', '')


TESTS_FOLD = 'tests'
TEST_FILE = '*.anq'
TESTS_DIR = os.path.join(TESTS_FOLD, TEST_FILE)


class Tester:
    def __init__(self, file):
        tests = Parser.parse(file)
        tests = random.iter(tests)
        tests = map(Test, tests)
        self.tests = filter(truth, tests)

    def ask_tests(self):
        for test in self.tests:
            self.ask_fields(test)

    def ask_fields(self, test):
        for field in test.fields:
            self.ask_field(test, field)

    def ask_field(self, test, field):
        os.cls()
        print('=' * 50)
        print(colors.bold('Hex:\n'))
        print(test.hex)
        ans = input(colors.bold('Input %s:\n' % field))
        if Test.filter(ans) == Test.filter(test.fields[field]):
            print(colors.ok_green('Correct'))
        else:
            print(colors.fail('Wrong'))
            print('%s: %s' % (colors.header(field),
                              colors.ok_blue(test.fields[field])))
        input(colors.bold('Press Enter...'))


if __name__ == '__main__':
    while True:
        test_files = glob.glob(TESTS_DIR)
        for file_dir in random.iter(test_files):
            with open(file_dir) as file:
                tester = Tester(file)
                tester.ask_tests()
