s = input()

normalized = " ".join(s.split())

print("Исходная длина:", len(s))
print("Новая длина:", len(normalized))
print("Нормализованный текст:", normalized)
print("Количество слов:", len(normalized.split()))