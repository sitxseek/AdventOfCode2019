
import numpy as np
import matplotlib.pyplot as plt

class Robot:
    def __init__(self):
        self.direction = 0
        self.x = 0
        self.y = 0

def extend(data, n):
    if n >= len(data):
        data += [0] * (n - len(data) + 1)

f = open("input.txt", "r")
data = list(map(int, f.read().split(",")))

relative_base = 0
i = 0
location_to_color = {(0, 0): 1}
direction_to_movement = {
    0: [(-1, 0), (1, 0)],
    1: [(0, -1), (0, 1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)]
}
new_direction = {
    0: [1, 3],
    1: [2, 0],
    2: [3, 1],
    3: [0, 2]
}
paint_count = 0
curr_color = None
robot = Robot()
minX = minY = maxX = maxY = 0
while i < len(data):
    instr = str(data[i])
    if instr[-1:] == '3':
        color = 0 if (robot.x, robot.y) not in location_to_color else location_to_color[(robot.x, robot.y)]
        if instr[0] == '2':
            extend(data, relative_base + data[i + 1])
            data[relative_base + data[i + 1]] = color
        else:
            extend(data, data[i + 1])
            data[data[i + 1]] = color
        i += 2
    elif instr[-1:] == '4':
        val = None
        if instr[0] == '1':
            val = data[i + 1]
            # if data[i + 1] != 0:
            #     raise ValueError('A test failed')
        elif instr[0] == '2':
            extend(data, relative_base + data[i + 1])
            val = data[relative_base + data[i + 1]]
            # if data[relative_base] != 0:
            #     raise ValueError('A test failed')
        else:
            extend(data, data[i + 1])
            val = data[data[i + 1]]
            # if data[data[i + 1]] != 0:
            #     raise ValueError('A test failed')
        if curr_color == None:
            curr_color = val
        else:
            direction = val
            if (robot.x, robot.y) not in location_to_color:
                paint_count += 1

            location_to_color[(robot.x, robot.y)] = curr_color
            robot.x += direction_to_movement[robot.direction][direction][0]
            robot.y += direction_to_movement[robot.direction][direction][1]
            robot.direction = new_direction[robot.direction][direction]
            curr_color = None
        i += 2
    elif instr == '99':
        break
    elif instr[-1:] == '9':
        if instr[0] == '1':
            relative_base += data[i + 1]
        elif instr[0] == '2':
            extend(data, relative_base + data[i + 1])
            relative_base += data[relative_base + data[i + 1]]
        else:
            extend(data, data[i + 1])
            relative_base += data[data[i + 1]]
        i += 2
    else:
        count = 4
        first = second = 0
        extend(data, data[i + 3])
        third = data[i + 3]
        if len(instr) == 1:
            extend(data, data[i + 1])
            extend(data, data[i + 2])
            first = data[data[i + 1]]
            second = data[data[i + 2]]
        elif len(instr) == 3:
            if instr[0] == '1':
                first = data[i + 1]
            else:
                extend(data, relative_base + data[i + 1])
                first = data[relative_base + data[i + 1]]
            extend(data, data[i + 2])
            second = data[data[i + 2]]
        else:
            if instr[-4] == '1': second = data[i + 2]
            else:
                extend(data, relative_base + data[i + 2]) 
                second = data[relative_base + data[i + 2]]
            if instr[-3] == '0': 
                extend(data, data[i + 1])
                first = data[data[i + 1]]
            elif instr[-3] == '1': first = data[i + 1]
            else: 
                extend(data, relative_base + data[i + 1])
                first = data[relative_base + data[i + 1]]
            if (len(instr) == 5):
                extend(data, relative_base + data[i + 3])
                third = relative_base + data[i + 3]

        if instr[-1:] == '1': 
            data[third] = first + second
        elif instr[-1:] == '2': 
            data[third] = first * second
        elif instr[-1:] == '5': 
            if first != 0:
                i = second
                count = 0
            else:
                count = 3
        elif instr[-1:] == '6': 
            if first == 0:
                i = second
                count = 0
            else:
                count = 3
        elif instr[-1:] == '7':
            data[third] = 1 if first < second else 0
        elif instr[-1:] == '8':
            data[third] = 1 if first == second else 0
        i += count

print(paint_count)

for location in location_to_color:
    if (location_to_color[location] == 1):
        plt.scatter(location[0], location[1])

plt.show()