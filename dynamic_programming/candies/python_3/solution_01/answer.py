n = int(input().strip())

a = []
for i in range(n):
    a.append(int(input().strip()))

b = [1 for x in range(n)]

# check left to right
for i in range(1, n):
    b[i] = b[i - 1] + 1 if a[i] > a[i - 1] else 1

# check right to left
for i in range(n - 2, -1, -1):
    if a[i] > a[i + 1]:
        if b[i] <= b[i + 1]:
            b[i] = b[i] + 1

print(sum(b))