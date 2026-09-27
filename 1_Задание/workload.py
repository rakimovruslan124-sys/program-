# Запрос названий двух предметов
subject1 = input("Введите название первого предмета: ")
subject2 = input("Введите название второго предмета: ")
# Запрос и валидация количества занятий и их длительности
while True:
    try:
        count1 = int(input(f"Количество занятий по {subject1} за неделю: "))
        duration1 = int(input(f"Длительность одного занятия по {subject1} (в минутах): "))
        if count1 < 0:
            raise ValueError("Количество занятий не может быть отрицательным.")
        if duration1 <= 0:
            raise ValueError("Длительность занятия должна быть положительным числом.")
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Попробуйте снова.")

while True:
    try:
        count2 = int(input(f"Количество занятий по {subject2} за неделю: "))
        duration2 = int(input(f"Длительность одного занятия по {subject2} (в минутах): "))
        if count2 < 0:
            raise ValueError("Количество занятий не может быть отрицательным.")
        if duration2 <= 0:
            raise ValueError("Длительность занятия должна быть положительным числом.")
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Попробуйте снова.")
# Запрос доступного времени на неделю в часах
while True:
    try:
        available_hours = float(input("Доступное время на неделю (в часах): "))
        if available_hours < (count1 * duration1 + count2 * duration2) / 60:
            raise ValueError("Доступное время не может быть меньше суммарной нагрузки.")
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Введите число.")
# Расчёты
total_minutes = count1 * duration1 + count2 * duration2
total_hours = total_minutes / 60
four_weeks_hours = total_hours * 4
# Вывод результатов
print("\n--- Результаты ---")
print(f"Время по {subject1}: {count1 * duration1} минут")
print(f"Время по {subject2}: {count2 * duration2} минут")
print(f"Общая нагрузка: {total_minutes} минут ({total_hours:.2f} часов)")
print(f"Остаток свободного времени: {four_weeks_hours - total_hours:.2f} часов")