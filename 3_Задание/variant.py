n = int(input("Введите целое число от 0 до 100: "))
if n < 0 or n > 100:
    print("Ошибка диапазона")
elif n <= 4:
    print("Начало")
elif n <= 94:
    print("Загрузка")
elif n <= 99:
    print("Завершение")
else:
    print("Завершено")