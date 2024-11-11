import datetime
import time
# 1 вывести текущую дату
# current_date = datetime.datetime.now().date()
# print(current_date)

# 2 Использование time для задержек в управлении полетом
# speeds = [10, 20, 30, 40, 50]

# for speed in speeds:
#     print (f"Текущая скорость {speed}")
#     time.sleep(2)


# 3 Использование datetime для временных меток
start_time = datetime.datetime.now()
print(f"Время начала полета {start_time}")
time.sleep(2)

end_time = datetime.datetime.now()
print(f"Время окончания полета {end_time}")

flight_duration = end_time - start_time
print(f"Продолжительность полета {flight_duration}")

