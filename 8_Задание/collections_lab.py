from collections import Counter, defaultdict

def word_counts(text: str) -> dict:
    """Словарь {слово: количество}.

    - нижний регистр;
    - разбиение по пробельным символам;
    - удаление .,!?;: с краёв каждого слова;
    - пропуск пустых результатов.

    Пустой текст даёт {}.
    """
    if not text:
        return {}
    strip_chars = ".,!?;:"
    words = (token.strip(strip_chars) for token in text.lower().split())
    return dict(Counter(w for w in words if w))


def sorted_pairs(counts: dict) -> list:
    """Пары (слово, количество), отсортированные по алфавиту."""
    return sorted(counts.items(), key=lambda kv: kv[0])



def common_topics(first: list, second: list) -> list:
    """Общие темы — отсортированный список уникальных строк."""
    return sorted(set(first) & set(second))


def all_topics(first: list, second: list) -> list:
    """Все уникальные темы — отсортированный список."""
    return sorted(set(first) | set(second))



def make_record() -> dict:
    """Создаёт запись, меняет hours и добавляет completed."""
    record = {"title": "Python", "hours": 20}
    record["hours"] = 30
    record["completed"] = False
    return record


def title_hours_pair(record: dict) -> tuple:
    """Кортеж (title, hours) из записи."""
    return (record["title"], record["hours"])



def totals_by_category(records: list) -> dict:
    """Суммы amount по категориям: {category: сумма}."""
    totals = defaultdict(int)
    for rec in records:
        totals[rec["category"]] += rec["amount"]
    return dict(totals)


def titles_in_category(records: list, category: str) -> list:
    """Названия (title) записей указанной категории в исходном порядке."""
    return [rec["title"] for rec in records if rec["category"] == category]

if __name__ == "__main__":
    print("=== 1. Частоты слов ===")
    text = "Привет, мир! Привет... Мир? КАК дела; как: дела!"
    counts = word_counts(text)
    print(counts)
    for word, n in sorted_pairs(counts):
        print(f"  {word}: {n}")
    print("  пустой текст ->", word_counts(""))

    print("\n=== 2. Учебные интересы ===")
    a = ["python", "sql", "алгоритмы", "sql"]
    b = ["sql", "ml", "python", "python"]
    print("  общие:      ", common_topics(a, b))
    print("  все:        ", all_topics(a, b))

    print("\n=== 3. Запись и пара ===")
    record = make_record()
    print("  запись:     ", record)
    pair = title_hours_pair(record)
    print("  пара:       ", pair)
    title, hours = pair
    print(f"  распаковка: title={title!r}, hours={hours}")

    print("\n=== 4. Записи: сводка и поиск (вариант 1: учебные занятия, часы) ===")
    base_records = [
        {"title": "A", "category": "основное",       "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное",       "amount": 3},
    ]
    print("  totals (набор):", totals_by_category(base_records))
    print("  titles 'основное':", titles_in_category(base_records, "основное"))
    print("  titles 'нет':     ", titles_in_category(base_records, "нет"))

    my_records = [
        {"title": "Python: основы",        "category": "программирование", "amount": 12},
        {"title": "Алгоритмы",             "category": "программирование", "amount": 18},
        {"title": "Базы данных",           "category": "программирование", "amount": 10},
        {"title": "Английский язык",       "category": "языки",            "amount": 8},
        {"title": "Математический анализ", "category": "математика",       "amount": 16},
    ]

    totals = totals_by_category(my_records)
    print("  Сводка по категориям:")
    for category in sorted(totals):
        print(f"    {category}: {totals[category]} ч.")

    query = input("  Введите категорию: ").strip()
    found = titles_in_category(my_records, query)
    if found:
        print(f"  Найдено в «{query}»:")
        for t in found:
            print(f"    - {t}")
    else:
        print(f"  Категория «{query}» не найдена: {found}")