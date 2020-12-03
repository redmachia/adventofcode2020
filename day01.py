import operator, functools, itertools

def day01both(data, n):
    for comb in itertools.combinations(lines, n):
        if sum(comb) == 2020:
            return functools.reduce(operator.mul, comb, 1)

with open('.\\Inputs\\day01input.txt', 'r') as f:
    lines = [*map(int, f.readlines())]
    print(day01both(lines, 2))
    print(day01both(lines, 3))