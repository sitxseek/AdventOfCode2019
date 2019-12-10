image = f = open("input.txt", "r").read()

max = 0
result = 0
message = ['2'] * 150
for i in range(0, len(image), 150):
    layer = image[i:i+150]
    message = [layer[j] if message[j] == '2' else message[j] for j in range(len(layer))]
    ones = image[i:i+150].count('1')
    twos = image[i:i+150].count('2')
    if (ones + twos) > max:
        result = ones * twos
        max = ones + twos

print("Part 1:", result)
str = ''.join(message)
for i in range(0, len(str), 25):
    print(str[i:i+25].replace('0',' '))