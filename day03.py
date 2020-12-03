def trace(x, y):
    pos = 0
    trees = 0
    with open('.\\Inputs\\day03input.txt', 'r') as f:
        map = [line.rstrip() for line in f]
        for a, b in enumerate(map):
            if a % y == 0:
                if b[pos] == '#':
                    trees += 1
                pos += x
                if pos >= len(b):
                    pos = abs(pos - len(b))
        return trees

# Previous method, slightly less intuitive
def trace_alternative(step_right, step_down):
    with open('.\\Inputs\\day03input.txt', 'r') as f:
        pos_x = step_right
        trees = 0
        tiles = [l.rstrip() for l in f.readlines()]
        for i in range(step_down, len(tiles), step_down):
            if tiles[i][pos_x] == '#':
                trees += 1
            if len(tiles[i][pos_x+1::]) >= step_right:
                pos_x += step_right
            else:
                pos_x = (step_right-1) - len(tiles[i][pos_x+1::])      
        return trees

print(f"Part 1: {trace(3, 1)}")
print(f"Part 2: {trace(1, 1) * trace(3, 1) * trace(5, 1) * trace(7, 1) * trace(1, 2)}")
