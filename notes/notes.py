from datetime import datetime

def create_note():
    manufacturer = input("Введите производителя дрона: ")
    model = input("Введите модель дрона: ")
    mass = input('Введите массу дрона (кг): ')
    payload = input("Полезная нагрузка (кг): ")
    flight_distance = input("Максимальная дальность полёта (км): ")
    speed = input("Максимальная скорость (км/ч): ")
    battery_life = input("Время работы от батареи (мин): ")

    current_time = datetime.now()
    creation_time_str = current_time.strftime("%Y-%m-%d %H:%M")

    with open("notes.txt", "a", encoding='utf-8') as file:
        file.write(manufacturer + ';' + model + ';' + mass + ';' + payload + ';' + flight_distance + ';' + speed + ';' + battery_life + ';' + creation_time_str + '\n')
        file.close()

    print("Данные успешно сохранены!")
    print(f"Время создания записи: {creation_time_str}")

def view_notes():
    try:
        with open("notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет")
            else:
                print("Список заметок")
                display_notes(notes)
    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новую заметку")


def display_notes(notes):
    for idx in range(1, len(notes)+1):
        data = notes[idx - 1].strip().split(';')
        manufacturer = data[0]
        model = data[1]
        mass = data[2]
        payload = data[3]
        flight_distance = data[4]
        speed = data[5]
        battery_life = data[6]
        creation_time = data[7]
        print(creation_time)

        print(f"№: {idx}, Производитель: {manufacturer}, Модель: {model}, Масса дрона: {mass}, Полезная нагрузка: {payload}, Максимальная дальность полёта: {flight_distance}, Максимальная скорость: {speed}, Время работы от батареи: {battery_life}, Время создания: {creation_time} ")


def delete_note():
    try:
        with open("notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет")
                return
            
            print("Список заметок для удаления")
            display_notes(notes)

            note_number = int(input("Введите номер заметки для удаления: "))
            if 1 <= note_number <= len(notes):
                del notes[note_number - 1]
                with open("notes.txt", "w", encoding='utf-8') as file:
                    file.writelines(notes)
                print("Заметка успешно удалена")
            else:
                print("Некорректный номер заметки")
    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новую заметку")
    except ValueError:
        print("Введите корректное число")


def main_menu():
    while True:
        print("\n=== Меню ===")
        print("1. Ввести нового дрона в каталог")
        print("2. Вывести на экран список дронов")
        print("3. Удалить записи дрона из каталога")
        print("0. Выход")

        choice = input("Выберите опцию (0 - 3):")

        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '0':
            print("Программа завершена")
            break
        else:
            print("Некорректный ввод. Пожалуйста выведите опцию от 0 до 3")

main_menu()