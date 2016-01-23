import json


class Parser:

    def __init__(self, file):
        self.file = file
        self.tests = [{}]

    def parse(self):
        field = ''
        current = self.tests[-1]
        for line in self.file:
            striped = line.strip()

            if striped.startswith('#'):
                continue

            if not striped:
                if current:
                    self.tests.append({})
                    current = self.tests[-1]
                continue

            if line.startswith(' '):
                if not field:
                    continue
                current[field] += striped + '\n'
            else:
                field = striped
                current[field] = ''

        return self.tests


if __name__ == '__main__':
    with open('tests.anq', 'r') as file:
        parser = Parser(file)
        tests = parser.parse()
    with open('tests.json', 'w') as file:
        file.write(json.dumps(tests, indent=2, ensure_ascii=False))
    print('OK')
