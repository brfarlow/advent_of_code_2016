with open('input.txt') as f:
    valid = 0
    for line in f.readlines():
        line = sorted([int(x) for x in line.split()])
        print(line)
        if line[0] + line[1] > line[2]:
            valid += 1

    print(valid)
