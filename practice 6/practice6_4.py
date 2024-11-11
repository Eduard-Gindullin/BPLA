# Сгенерировать список случайных чисел
# Найти мин макс и меан
# Список квадратов чисел
# Подсчитать количество четных и нечетных

import random

def generate_random_numbers(count, min_val, max_val):
    numbers = []
    for i in range(count):
        number = random.randint(min_val, max_val)
        numbers.append(number)
    return numbers

def calculate(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = sum(numbers) / len(numbers)
    return min_num, max_num, avg_num

def squared(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

def count_even_odd(numbers):
    count_evens = 0
    count_odds = 0
    for num in numbers:
        if num % 2 == 0:
            count_even_odd += 1
        else:
            count_odds += 1
    return count_evens, count_odds

def main():
    numbers = generate_random_numbers(10, 1, 100)
    print (f"Список случайных чисел: {numbers}")
    min_num, max_num, avg_num = calculate(numbers)
    print(F"Мин: {min_num}, Макс: {max_num}, Среднее {avg_num} ")

    squared_numbers = squared(numbers)
    print (f" Квадраты {numbers} - {squared_numbers}")

    count_evens, count_odds = count_even_odd(numbers)

    main()