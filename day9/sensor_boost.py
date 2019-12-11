def extend(data, n):
    if n >= len(data):
        data += [0] * (n - len(data) + 1)

f = open("input.txt", "r")
data = list(map(int, f.read().split(",")))

relative_base = 0
i = 0
while i < len(data):
    instr = str(data[i])
    if instr[-1:] == '3':
        if instr[0] == '2':
            extend(data, relative_base + data[i + 1])
            data[relative_base + data[i + 1]] = 2
        else:
            extend(data, data[i + 1])
            data[data[i + 1]] = 2
        i += 2
    elif instr[-1:] == '4':
        if instr[0] == '1':
            print("output", data[i + 1])
            # if data[i + 1] != 0:
            #     raise ValueError('A test failed')
        elif instr[0] == '2':
            extend(data, relative_base + data[i + 1])
            print("output", data[relative_base + data[i + 1]])
            # if data[relative_base] != 0:
            #     raise ValueError('A test failed')
        else:
            extend(data, data[i + 1])
            print("output", data[data[i + 1]])
            # if data[data[i + 1]] != 0:
            #     raise ValueError('A test failed')
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