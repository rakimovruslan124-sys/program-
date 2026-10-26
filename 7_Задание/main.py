from functions import sum_digits, average, normalize_text, select_numbers

number = int(input("Введите целое число: "))
print("Сумма цифр:", sum_digits(number))

s = input("Введите числа через пробел: ").strip()
numbers = list(map(int, s.split())) if s else []
avg = average(numbers)
if avg is None:
    print("Среднее: Нет данных")
else:
    print("Среднее:", avg)

text = input("Введите текст: ")
print("Нормализованный текст:", normalize_text(text))

threshold = int(input("Введите порог: "))
selected = select_numbers(numbers, threshold)
print("Выборка:", selected)