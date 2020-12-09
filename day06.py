with open('.\\Inputs\\day06input.txt', 'r') as f:
    tmp = ""
    k = sum_s = 0
    groups = list()
    for line in f:
        if line != '\n':
            tmp += line.strip()
            k += 1
        else:
            groups.append(set([l for l in tmp]))
            for i in range(0, len(tmp)):
                if tmp.count(tmp[i]) == k and tmp[i] != '-':
                    sum_s += 1
                    tmp = tmp.replace(tmp[i], '-')
            tmp = ""
            k = 0
    size = sum([len(s) for s in groups])

    print(f"Part 1 solution: {size}")
    print(f"Part 2 solution: {sum_s}")