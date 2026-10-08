n = int(input())
x = int(input())

total = x
positive = 1 if x > 0 else 0
maximum = x

for i in range(n - 1):
    x = int(input())
    total += x
    if x > 0:
        positive += 1
    if x > maximum:
        maximum = x

print(total)
print(positive)
print(maximum)