attempts = 0
x = int(input())
while x <= 0:
    attempts += 1
    x = int(input())
print(x * x)
print(attempts)