with open('.\\Inputs\\day12input.txt') as f:
    moves = [(line[:1], int(line[1:])) for line in f]

directions = {'N': (0,  1),
            'S': (0, -1),
            'W': (-1, 0), 
            'E': (1,  0)}

def solve(dx: int, dy: int, part: int) -> float:
    x = y = 0
    for move, val in moves:
        if move == 'L' or move == 'R':
            if move == 'R':
                val = 360 - val
            while val:
                dx, dy = -dy, dx
                val -= 90
        elif move == 'F':
            x += val * dx
            y += val * dy
        else:
            ddx, ddy = [val * i for i in directions[move]]
            if part == 1:
                x += ddx
                y += ddy
            else:
                dx += ddx
                dy += ddy
    return abs(x) + abs(y)

print(f"Part 1 solution: {solve(*directions['E'], part=1)}")
print(f"Part 2 solution: {solve(10, 1, part=2)}")
