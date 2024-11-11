# 
def get_numbers():
    user_input = input("Введите числа через пробел \n")
    numer_strings = user_input.split()
    numbers = []
    for num in numer_strings:
        num = float(num)
        numbers.append(num)
    return numbers

def save_numbers(numbers):
    with open("numbers2.txt", "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

def calculate(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = get_numbers
    save_numbers(numbers)
    average = calculate(numbers)
    print(f"Среднее аврифметическое {average}")

main()