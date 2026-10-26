s = input().strip()

nums = list(map(int, s.split())) if s else []

selected = [x for x in nums if x >= 10]

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)

print("Выборка:", selected)
print("Количество:", count)
print("Сумма:", total)
print("Отсортированная копия:", sorted_copy)