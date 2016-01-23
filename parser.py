class Parser:
    @staticmethod
    def parse(file):
        field = ''
        tests = [{}]
        current = tests[-1]
        for line in file:
            striped = line.strip()

            if striped.startswith('#'):
                continue

            if not striped:
                if current:
                    tests.append({})
                    current = tests[-1]
                continue

            if line.startswith(' '):
                if not field:
                    continue
                current[field] += striped + '\n'
            else:
                field = striped
                current[field] = ''
        print(tests)
        return tests
