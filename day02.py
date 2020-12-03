def parse(filename):
    with open(filename, 'r') as f:
        lines = [l.rstrip('\n').split(' ') for l in f.readlines()]
        d = list()
        for line in lines:
            nums = [int(i) for i in line[0].split('-')]
            d.append({'min': nums[0], 'max': nums[1], 'l': line[1][0],
                 'pw': line[2]})
        return d

correct = 0
data = parse('.\\Inputs\\day02input.txt')
"""
# Day 1
for d in data:
    n = d['pw'].count(d['l'])
    if n <= d['max'] and n >= d['min']:
        correct += 1
"""
# Day 2
for d in data:
    if d['pw'][d['min'] - 1] == d['l'] and d['pw'][d['max'] - 1] != d['l']:
        correct += 1
    elif d['pw'][d['min'] - 1] != d['l'] and d['pw'][d['max'] - 1] == d['l']:
        correct += 1
    
print(correct)
