s = input().strip()

if not s:
    print("Нет данных")
else:
    nums = list(map(int, s.split()))
    maximum = max(nums)
    positions = [i for i, x in enumerate(nums) if x == maximum]
    print(positions)