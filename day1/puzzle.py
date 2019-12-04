def parse(lines):
    return list(map(int, lines))

def solvePartOne(data):
    sum = 0
    for n in data:
        sum += (n // 3 - 2)
    return sum

def solvePartTwo(data):
    sum = 0
    for n in data:
        while True:
            n = (n // 3 - 2)
            if n > 0: sum += n
            else: break
    return sum