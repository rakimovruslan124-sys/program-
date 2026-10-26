s = input().strip()

if not s:
    print("Нет данных")
else:
    nums = list(map(int, s.split()))
    count = len(nums)
    total = sum(nums)
    minimum = min(nums)
    maximum = max(nums)
    average = total / count

    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print(f"Среднее: {average:.2f}")