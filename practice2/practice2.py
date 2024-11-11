# 2 проверка положительности числа

# # 3 Проверка числа на кратность 5
# num = int(input("Введите число \n"))
# if num % 5 == 0:
#     print (f"{num} кратно 5")
# else:
#     print(f"{num} не кратно 5")

# 4 Проверка какое больше
# num1 = int(input("Введите число1: \n"))
# num2 = int(input("Введите число2: \n"))
# if num1 > num2:
#     print (f"Наибольшее число{num1}")
# else :
#     print (f"Наибольшее число {num2}")

# 5 Сравнение 3х чисел
# num1 = int(input("Введите число1: \n"))
# num2 = int(input("Введите число2: \n"))
# num3 = int(input("Введите число3: \n"))
# if num1 > num2 and num1 > num3:
#     print(f"Наибольшее число {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"Наибольшее число {num2}")
# else:
#     print(f"Наибольшее число {num3}")

# 6 Проверка диапазона от 10 до 20
# num = int(input("Введите число \n"))
# if 10 <= num <= 20:
#     print ("Число находится в диапазоне")
# else:
#     print ("Число находится вне диапазона")

# 7 Проверка скрости (50 км/ч допустима)
# speed = float(input("Введите скорость БПЛА:"))
# max_speed = 50
# if speed > max_speed:
#     print ("Скорость превышена")
# else: 
#     print ("Скорость превышена")

# 8 Проверка высоты (от 100 до 500)
# alt = float(input("Введите высоту"))
# if 100 <= alt <= 500:
#     print("Высота в допустимом значении")
# else: 
#     print("Высота вне допустимых значении")

# 9 выбор направления движения
# direction = input("Введите направления движения \n")
# if direction == "север":
#     print(f"Двигаемся на {direction}")
# elif direction == "юг":
#     print(f"Двигаемся на {direction}")
# elif direction == "запад":
#     print(f"Двигаемся на {direction}")
# elif direction == "восток":
#     print(f"Двигаемся на {direction}")
# else:
#     print("Двигаемся в никуда")

#10. Опредение времени полета
# speed = float(input("Введите скорость БПЛА:"))
# distance = float(input("Введите растояние /n"))
# time = distance/speed
# print ("Время полета", time)
# if time > 3:
#     print("Полет отменен")
# else:
#     print("Полет разрешен")

# 11 Определение времени работы аккума
# battery_percent = float(input("Введите процент заряда аккума \n"))
# max_flight_time = 2
# flight_time = (battery_percent / 100) * max_flight_time
# print (f"Предполагаемое время полета {flight_time} часов")

#12  Вывод чисел от 1 до 10
# for i in range(1,11):
#     print(i)

# 13 сумма чисел от 1 до 100
# total = 0
# for i in range(1,101):
#     total += i
#     print("сумма чисел от 1 до 100", total)

# 14 Вывод четных чисел от 1 до 20
# for i in range(2,21,2):
#     print(i)

#15 Обратный отсчет 
# for i in range(10,-1,-1):
#     print(i)

# 16 Подсчет количество положительных чисел из 5
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число: \n"))
#     if num > 0:
#         positive_count += 1
# print(f"Количество положительных чисел: {positive_count}")


# 17 Таблица умножения на 5
# for i in range(1, 11):
#     print(f"5 * {i} = {5 * i}")

# 18 Вывод всех цифр числа
# num = input("Введите число: \n")
# for digit in num:
#     print (digit)

# 19 Сумма всех цифр числа
# num = input("Введите число: \n")
# total = 0
# for digit in num:
#     total += int(digit)
# print ("Сумма цифр равна", total)

#20 поиск минимального числа
# min_num = float("inf")
# for i in range(5):
#     num = int(input("Введите число \n"))
#     if num < min_num:
#         min_num = num
# print(f"Минимальное число {min_num}") 


#21 Количество положительных и отрицательных чисел из 5
# negative_count = 0
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число \n"))
#     if num > 0:
#         positive_count += 1
#     else:
#         negative_count += 1
# print(f"Количество положительных {positive_count}. Отрицательных {negative_count}")

# 22 Проверка наличия цифры 7
# number = input("Введите число \n")
# if "7" in number:
#     print("число содержит 7")
# else:
#      print("число не содержит 7")

#23 проверка диапазона значений (50 до 300)
# alts = []
# out_of_range = []
# while True:
#     alt = int(input("Введите высоту: (или -1 для завершения)\n"))
#     if alt == -1:
#         break
#     alts.append(alt)

#     if alt < 50 or alt > 300:
#         out_of_range.append(alt)

# if len(out_of_range) == 0:
#     print("Все высоты были в допустимом диапазоне") 
# else:
#     print("не всевысоты были в допустимом диапазоне", out_of_range)


# 24 Таблица умножения
# for i in range(1, 11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i * j}")
#     print()


# 25 Посчитать количество гласных и согласных букв в строке
# vowels = "аеёиоуыэюя"
# vowels_count = 0
# consanant_count = 0
# text = input("Введите строку текста:").lower()
# for char in text:
#     if char .isalpha():
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consanant_count += 1
# print (f"Колличество гласных {vowels_count}, согласных {consanant_count}")


# 26 создание списка четных чисел
# even_numbers = []
# for num in range(1,101):
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# 27 количество четных чисел в списке
# numbers = input("Введите числа через пробел: \n").split()
# even_count = 0
# for num in numbers:
#     if int(num) % 2 == 0:
#         even_count +=1
# print (f"четные {even_count}")

# 28 Удаление дубликатов из списка
# numbers = input("Введите числа через пробел: \n").split()
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print ("Список без дубликатов", unique_numbers)

# 29 тоже самое
# numbers = input("Введите числа через пробел: \n").split()
# unique_number = list(set(numbers))
# print(unique_number)

# 30 Содержит ли строка числа
# input_string = input("Введите строку \n")
# contains_digit = False
# for char in input_string:
#     if char.isdigit():
#         contains_digit = True
#         break
# if contains_digit:
#     print("строка содежит цифры!")
# else:
#     print("все ок")

# 31 брать все цифры из строки
# input_string = input("Введите строку \n")
# output_string = ""
# for char in input_string:
#     if not char.isdigit():
#         output_string += char
# print(f"Строка без чисел {output_string}")

# 32 разделение строки на слова
# input_string = input("Введите строку \n")
# words = input_string.split()
# for word in words:
#     print(word)

# 33 Подсчет количества положительных чисел в списке
# input_list = input("Введите числа через пробел \n")
# numbers = []
# possitive_count = 0
# for num in input_list.split():
#     numbers.append(int(num))

# for num in numbers :
#     if num > 0:
#         possitive_count +=1
# print(f"Количество положительных чисел {possitive_count}")


#34 Нахождение разности между мин и мак числом


# 35 проверить что все числа списка положительные
# input_list = input("Введите числа через пробел \n")
# numbers =[]
# all_possitive = True
# negative_numbers = []
# for num in input_list.split():
#      negative_numbers.append(int(num))
# for num in numbers:
#      if num <= 0:
#           all_possitive = False
#           negative_numbers.append(num)
# if all_possitive:
#      print("Все числа положительные") 
# else:
#      print ("Отрицательные", negative_numbers)   


# 36 Подсчет заряда
# initial_charge = float(input("Введите заряд\n"))
# distance = float(input("введите дистанцию в км \n"))
# consumption_rate = float(input("Введите расход на 1 км\n"))
# remaining_charge = initial_charge - (distance * consumption_rate)
# if remaining_charge < 0:
#     remaining_charge = 0
# print(f"Осталось заряда {remaining_charge}")


# 37 Поис минимальной скорости
# num_speeds = float(input("Введите количество показателей скорости \n"))
# speeds = []

# for i in range(num_speeds):
#     speed = float(input("Введите скорость полета\n"))
#     speeds.append(speed)
# min_speed = min(speeds)
# print(f"Минимальная скорость среди {num_speeds} : {min_speed}")


# 38 Определение высоты полета через n минут (Пусть каждые 1 минуту подъем 10 метров)
# n = int(input("Введите количество минут\n"))
# alt = 0
# for i in range(n):
#     alt += 10
# print (f"Высота чкркз {n} минут равна {alt} м")


# 39 Отслеживание уровня заряда (в минуту теряет 1%)
# battery = 100
# minutes = 0
# while battery > 20:
#     battery -= 1
#     minutes += 1
# print(f"Заряд достиг 20% через {minutes} мин")


# 40 Расчет времени на полный круг полета
# pi = 3.14
# diametr = 500
# speed = 10
# circumference = pi * diametr
# time = circumference / speed
# print(f"Время на полный круг {int(time)} c")


# 42 Подсчет полетов с перегрузом
# weights_input = input("Введите массы грузов через пробел \n")
# weights = []
# overload_flaights = 0
# for i in weights_input.split():
#     weights.append(int(i))

# for weight in weights:
#     if weight > 30:
#         overload_flaights += 1

# print(f"Колличество полетов с перегрузкой {overload_flaights}")