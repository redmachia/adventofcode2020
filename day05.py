from math import ceil, floor
"""
# OLD VERSION
def part01(passess):
    max = 127
    min = 0
    max_c = 7
    min_c = 0
    
    for letter in passess:
        if letter == 'F':
            max = floor((max - min)/2) + min
        elif letter == 'B':
            min = ceil((max-min) / 2) + min
        elif letter == 'L':
            max_c = floor((max_c - min_c) / 2) + min_c
        else:
            min_c = ceil((max_c-min_c) / 2) + min_c
    return (min * 8) + max_c

def part02(seats):
    for seat in range(min(seats), max(seats)):
        if ((seat - 1) in seats) and ((seat not in seats)) and ((seat + 1) in seats):
            return seat

with open('.\\Inputs\\day05input.txt', 'r') as f:
    seats = list()
    for line in f:
        seats.append(part01(line.strip('\n')))
    print(f"Solution to part 1: {max(seats)}")
    my_seat = part02(seats)
    print(f"Solution to part 2: {my_seat}")

"""
with open('.\\Inputs\\day05input.txt', 'r') as f:
    # New version
    trans = str.maketrans('FBRL', '0110')
    seats = [int(line.strip('\n').translate(trans), base=2) for line in f]
    my_seat = set(range(min(seats), max(seats))).difference(set(seats)).pop()
    print(f"Solution to part 1: {max(seats)}")
    print(f"Solution to part 2: {my_seat}")