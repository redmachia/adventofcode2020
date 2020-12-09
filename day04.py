def parse():
    with open('.\\Inputs\\day04input.txt', 'r') as f:
        tmp = ''
        d = dict()
        passports = list()
        for line in f:
            if line != '\n':
                tmp += line.strip() + " "
            else:
                pids = [(id.split(':')[0], id.split(':')[1]) for id in tmp[:len(tmp) - 1].split(' ')]
                for key, val in pids:
                    d |= {key : val}
                passports.append(d)
                d = dict()
                tmp = ''
        return passports


def part_01(passports):
    correct = 0
    pids = ['ecl', 'pid', 'eyr', 'hcl',
            'byr', 'iyr', 'cid', 'hgt']
    for passport in passports:
        pkeys = list(passport.keys())
        if 'cid' in pkeys:
            if len(pkeys) == len(pids):
                correct += 1
        else:
            if (len(pkeys) + 1) == len(pids):
                correct += 1
    return correct

def part_02(passports):
    correct = 0
    final_correct = 0
    for passport in passports:
        try:
            if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
                correct += 1
            if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['byr']) <= 2020:
                correct += 1
            if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                correct += 1
            if passport['hgt'].endswith('cm'):
                if int(passport['hgt'][:len(passport['hgt'])-2]) >= 150 and int(passport['hgt'][:len(passport['hgt'])-2]) <= 193:
                    correct += 1
            elif passport['hgt'].endswith('in'):
                if int(passport['hgt'][:len(passport['hgt'])-2]) >= 59 and int(passport['hgt'][:len(passport['hgt'])-2]) <= 76:
                    correct += 1
            if passport['hcl'].startswith('#'):
                if len(passport['hcl'][1:]) == 6 and int(passport['hcl'][1:], base=16):
                    correct += 1
            if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                correct += 1
            if len(passport['pid']) == 9:
                correct += 1
            if correct == 7:
                final_correct += 1
            correct = 0
        except:
            correct = 0
    return final_correct
passports = parse()
print(part_01(passports))
print(part_02(passports))
            