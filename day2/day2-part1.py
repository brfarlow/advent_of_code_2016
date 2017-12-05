with open('input.txt') as f:
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    pos = (1, 1)

    for line in f.readlines():
        for direction in line.strip():
            pos = (
                max(0, min(pos[0] + directions[direction][0], 2)),
                max(0, min(pos[1] + directions[direction][1], 2)))
        print(keypad[pos[1]][pos[0]])
