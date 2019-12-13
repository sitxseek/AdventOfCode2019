
from math import gcd
from math import atan2
from math import degrees
from math import sqrt

class Asteroid:
    def __init__(self):
        self.detect = set()
        self.count = 0

f = open("input.txt", "r")
data = [list(line.rstrip()) for line in f]
asteroids = [[Asteroid() for _ in range(len(data[0]))] for _ in range(len(data))]
max_detect = 0
best_asteroid = None

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != '#': continue
        for x in range(j + 1, len(data[0])):
            if data[i][x] == '#':
                asteroids[i][j].count += 1
                asteroids[i][x].count += 1
                break
        for k in range(i + 1, len(data)):
            for l in range(len(data[0])):
                if data[k][l] != '#': continue
                g = gcd(k - i, l - j)
                t = ((k - i) / g, (l - j) / g)
                if t not in asteroids[i][j].detect:
                    asteroids[k][l].count += 1
                    asteroids[i][j].count += 1
                    asteroids[i][j].detect.add(t)
        if asteroids[i][j].count > max_detect:
            max_detect = asteroids[i][j].count
            best_asteroid = (j, i)

print("Best asteroid:", best_asteroid, max_detect)

# part 2
angle_to_coord = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != '#' or (i == best_asteroid[1] and j == best_asteroid[0]): continue
        angle = (degrees(atan2(j - best_asteroid[0], best_asteroid[1] - i)) + 360) % 360
        coord = angle_to_coord.get(angle, [])
        coord.append((j, i))
        angle_to_coord[angle] = coord

for angle in angle_to_coord:
    coord = angle_to_coord[angle]
    sorted_coord = sorted(coord, key=lambda tup: sqrt((tup[0] - best_asteroid[0])**2 + (best_asteroid[1] - tup[1])**2))
    angle_to_coord[angle] = sorted_coord

sorted_angles = sorted(angle_to_coord.keys())
j = 0
ans = None
for i in range(200):
    if j == len(sorted_angles):
        j = 0
    ans = angle_to_coord[sorted_angles[j]].pop(0)
    if not angle_to_coord[sorted_angles[j]]:
        del angle_to_coord[sorted_angles[j]]
        del sorted_angles[j]
        j -= 1
    j += 1

print("200th asteroid", ans)