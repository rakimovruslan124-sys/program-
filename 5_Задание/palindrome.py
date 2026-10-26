s = input()

cleaned = s.replace(" ", "").lower()

if not cleaned:
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")