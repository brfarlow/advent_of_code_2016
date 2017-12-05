with open('input.txt') as f:
    keypad = [[None, None, 1, None, None],
              [None, 2, 3, 4, None],
              [5, 6, 7, 8, 9],
              [None, 'A', 'B', 'C', None],
              [None, None, 'D', None, None]]
    directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    pos = (0, 2)

    for line in f.readlines():
        for direction in line.strip():
            new_pos = (
                max(0, min(pos[0] + directions[direction][0], 4)),
                max(0, min(pos[1] + directions[direction][1], 4)))
            if keypad[new_pos[1]][new_pos[0]] is not None:
                pos = new_pos

        print(keypad[pos[1]][pos[0]])
