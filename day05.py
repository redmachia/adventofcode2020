with open('.\\Inputs\\day05input.txt', 'r') as f:
    # New version
    trans = str.maketrans('FBRL', '0110')
    seats = [int(line.strip('\n').translate(trans), base=2) for line in f]
    my_seat = set(range(min(seats), max(seats))).difference(set(seats)).pop()
    print(f"Solution to part 1: {max(seats)}")
    print(f"Solution to part 2: {my_seat}")
