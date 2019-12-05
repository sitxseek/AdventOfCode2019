def check(n):
    return list(n) == sorted(n) and 2 in map(n.count, n)

print(sum(check(str(n)) for n in range(256310, 732737)))