a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ").strip()
if op == "+":
    result = a + b
    print(f"{result:.2f}")
elif op == "-":
    result = a - b
    print(f"{result:.2f}")
elif op == "*":
    result = a * b
    print(f"{result:.2f}")
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"{result:.2f}")

else:
    print("Неизвестная операция")