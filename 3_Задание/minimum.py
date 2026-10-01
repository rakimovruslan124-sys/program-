a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c
print(f"Минимальное число: {minimum}")