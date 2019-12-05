count = 0
for i in range(256310, 732736):
    s = str(i)
    valid = False
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            valid = False
            break
        if s[j] == s[j + 1]:
            valid = True
    if valid:
        count += 1
print(count)