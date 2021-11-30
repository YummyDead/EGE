z = set()
for i in range(10, 1001):
    N = bin(i)[3:]
    N = int(N, 2)
    z.add(i - N)
print(len(z))
            