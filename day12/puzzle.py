from fractions import gcd
from functools import reduce
import numpy as np

position = [[-1, -4, 0], [4, 7, -1], [-14, -10, 9], [1, 2, 17]]
velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(1000):
    for j in range(len(position)):
        for k in range(j + 1, len(position)):
            for l in range(3):
                if position[j][l] < position[k][l]:
                    velocity[j][l] += 1
                    velocity[k][l] -= 1
                elif position[j][l] > position[k][l]:
                    velocity[j][l] -= 1
                    velocity[k][l] += 1
    position = [[sum(i) for i in zip(position[j], velocity[j])] for j in range(len(position))]

energy = 0
for i in range(len(position)):
    energy += sum([abs(x) for x in position[i]]) * sum([abs(x) for x in velocity[i]])

print(energy)

# part 2
position = [[-1, -4, 0], [4, 7, -1], [-14, -10, 9], [1, 2, 17]]
velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
cycle_points = [None for x in range(3)]
initial_state = [tuple((position[i][j], velocity[i][j]) for i in range(len(position))) for j in range(len(position[0]))]
iteration = 1
while True:
    for j in range(len(position)):
        for k in range(j + 1, len(position)):
            for l in range(len(position[0])):
                if position[j][l] < position[k][l]:
                    velocity[j][l] += 1
                    velocity[k][l] -= 1
                elif position[j][l] > position[k][l]:
                    velocity[j][l] -= 1
                    velocity[k][l] += 1
    position = [[sum(i) for i in zip(position[j], velocity[j])] for j in range(len(position))]
    for i in range(len(position[0])):
        t = tuple((position[j][i], velocity[j][i]) for j in range(len(position)))
        if t == initial_state[i]:
            if cycle_points[i] == None:
                cycle_points[i] = iteration
    if None not in cycle_points:
        break
    iteration += 1

print(np.lcm.reduce(cycle_points))