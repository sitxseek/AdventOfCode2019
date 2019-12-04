def main():
    f = open("input.txt", "r")
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")
    f.close()

    coordinates1 = collect_coordinates(wire1)
    coordinates2 = collect_coordinates(wire2)
    intersections = list(set(coordinates1) & set(coordinates2))
    steps = [0] * len(intersections)

    collect_steps(wire1, intersections, steps)
    collect_steps(wire2, intersections, steps)
    print("Min steps:", min(steps))

def collect_coordinates(wire):
    x = y = 0
    coordinates = []
    for path in wire:
        for _ in range(int(path[1:])):
            if path[0] == 'R':
                x += 1
            elif path[0] == 'U':
                y += 1
            elif path[0] == 'L':
                x -= 1
            else:
                y -= 1
            coordinates.append((x, y))
    return coordinates

def collect_steps(wire, intersections, steps):
    x = y = step = 0
    for path in wire:
        for _ in range(int(path[1:])):
            if path[0] == 'R':
                x += 1
            elif path[0] == 'U':
                y += 1
            elif path[0] == 'L':
                x -= 1
            else:
                y -= 1
            step += 1
            if (x, y) in intersections:
                index = intersections.index((x, y))
                steps[index] += step

if __name__ == '__main__':
    main()