def sum_digits(number):
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    return [x for x in numbers if x % 2 == 0 and x > threshold]