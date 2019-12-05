count = 0
for i in range(256310, 732737):
    s = str(i)
    valid = True
    digits = {}
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            valid = False
            break
        digits[s[j]] = digits.get(s[j], 0) + 1
    last = s[len(s) - 1]
    digits[last] = digits.get(last, 0) + 1
    if valid and 2 in digits.values():
        count += 1
print(count)