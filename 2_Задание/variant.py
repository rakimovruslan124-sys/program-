total = int(input("Общий объём бутылок: "))
capacity = int(input("Вместимость одной бутылки в ящик : "))
full = total // capacity
remainder = total % capacity
units_needed = (total + capacity - 1) // capacity
print(f"Полностью заполненных ящиков: {full}")
print(f"Остаток буытлок: {remainder}")
print(f"Минимальное число ящиков: {units_needed}")