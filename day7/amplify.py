from itertools import permutations

f = open("input.txt", "r")
data = list(map(int, f.read().split(",")))

def run_on_amplifier(data, phase, val, state, amp):
    i = state[amp]
    if state[amp] == 0:
        data[data[i + 1]] = phase
        i += 2
    while i < len(data):
        instr = str(data[i])
        if instr[-1:] == '3':
            data[data[i + 1]] = val
            i += 2
        elif instr[-1:] == '4':
            if len(instr) > 1:
                state[amp] = i + 2
                return data[i + 1]
                # if data[i + 1] != 0:
                #     raise ValueError('A test failed')
            else:
                state[amp] = i + 2
                return data[data[i + 1]]
                # raise ValueError('A test failed')
            break
        elif instr == '99':
            state[amp] = -1
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

# process
max_amplication = 0
permutations = list(permutations(range(5, 10)))

for p in permutations:
    state = [0, 0, 0, 0, 0]
    signal = 0
    signal_from_e = 0
    a = data[:]
    b = data[:]
    c = data[:]
    d = data[:]
    e = data[:]

    while True:
        signal = run_on_amplifier(a, p[0], signal, state, 0)
        if signal == None: break
        signal = run_on_amplifier(b, p[1], signal, state, 1)
        if signal == None: break
        signal = run_on_amplifier(c, p[2], signal, state, 2)
        if signal == None: break
        signal = run_on_amplifier(d, p[3], signal, state, 3)
        if signal == None: break
        signal = run_on_amplifier(e, p[4], signal, state, 4)
        if signal == None: break
        signal_from_e = signal

    max_amplication = max(max_amplication, signal_from_e)
    
print("Amplification:", max_amplication)