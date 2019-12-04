f = open("input.txt", "r")
wire1 = f.readline().split(",")
wire2 = f.readline().split(",")
f.close()

x = y = 0
coordinates1 = []
for path in wire1:
    for i in range(int(path[1:])):
        if path[0] == 'R':
            x += 1
        elif path[0] == 'U':
            y += 1
        elif path[0] == 'L':
            x -= 1
        else:
            y -= 1
        coordinates1.append((x, y))

x = y = 0
coordinates2 = []
for path in wire2:
    for i in range(int(path[1:])):
        if path[0] == 'R':
            x += 1
        elif path[0] == 'U':
            y += 1
        elif path[0] == 'L':
            x -= 1
        else:
            y -= 1
        coordinates2.append((x, y))

intersections = list(set(coordinates1) & set(coordinates2))
sorted_intersections = sorted(intersections, key=lambda tup: abs(tup[0]) + abs(tup[1]))
if sorted_intersections:
    print(abs(sorted_intersections[0][0]) + abs(sorted_intersections[0][1]))