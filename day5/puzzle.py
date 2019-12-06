f = open("input.txt", "r")
data = list(map(int, f.read().split(",")))

i = 0
while i < len(data):
    instr = str(data[i])
    print(instr)
    if instr[-1:] == '3':
        data[data[i + 1]] = 5
        i += 2
    elif instr[-1:] == '4':
        if len(instr) > 1:
            print("output", data[i + 1])
            # if data[i + 1] != 0:
            #     raise ValueError('A test failed')
        if data[data[i + 1]] != 0:
            print("output", data[data[i + 1]])
            # raise ValueError('A test failed')
        break
    elif instr[-1:] == '99':
        break
    else:
        count = 4
        first = second = 0
        if (len(instr) == 1 or len(instr) == 3):
            first = data[i + 1] if len(instr) == 3 else data[data[i + 1]]
            second = data[data[i + 2]]
        elif instr[1] == '1':
            first = data[i + 1]
            second = data[i + 2]
        else:
            first = data[data[i + 1]]
            second = data[i + 2]

        if instr[-1:] == '1': data[data[i + 3]] = first + second
        elif instr[-1:] == '2': data[data[i + 3]] = first * second
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
            data[data[i + 3]] = 1 if first < second else 0
        elif instr[-1:] == '8':
            data[data[i + 3]] = 1 if first == second else 0
        i += count

# 3,3,1105,1,9,1101,0,0,12,4,12,99,1