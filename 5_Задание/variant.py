s = input()

words = s.split()
count = 0

for w in words:
    cleaned = w.strip(".,!?;:").lower()
    if not cleaned:
        continue
    # Вариант 10: начинается и заканчивается одной и той же буквой
    if cleaned[0] == cleaned[-1]:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
print("Количество:", count)