def runProg(prog, swap = False):
    seen = set()
    acc = op_ptr = 0
    
    while op_ptr < len(prog):
        line = prog[op_ptr].rstrip().split(' ')
        op, arg = line[0], int(line[1])
        if op_ptr in seen:
            return None if swap else acc
        seen.add(op_ptr)
        if op == 'acc':
            acc += arg
            op_ptr += 1
        elif op == 'jmp':
            op_ptr += arg
        elif op == 'nop':
            op_ptr += 1
    return acc

def tryRun(code_b, i):
    code = code_b.copy()
    if code[i].startswith('jmp'):
        code[i] = code[i].replace('jmp', 'nop')
    elif code[i].startswith('nop'):
        code[i] = code[i].replace('nop', 'jmp')
    return runProg(code, True)
    

with open('.\\Inputs\\day08input.txt', 'r') as f:
    code = f.readlines()
    # Part A:
    print(runProg(code))
    # Part B:
    for i in range(0, len(code)):
        ret = tryRun(code, i)
        if ret:
            print(ret)

