with open('input.txt') as f:
    valid = 0
    lines = [[int(x) for x in lines.split()] for lines in f.readlines()]
    for x, y, z in zip(lines[0::3], lines[1::3], lines[2::3]):
        for i, j, k in zip(x, y, z):
            sides = [i, j, k]
            if sum(sides) > 2 * max(sides):
                valid += 1

    print(valid)
