s = input().strip()

nums = list(map(int, s.split())) if s else []

new_nums = [abs(x) for x in nums]

print("Исходный список:", nums)
print("Новый список:", new_nums)