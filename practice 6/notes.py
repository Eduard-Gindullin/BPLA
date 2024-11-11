# Заметки
# Создавать заметку
# Просматривать
# Удалять

def create_note():
    note_text = input("Введите текст заметки: \n")
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note_text + "\n")
    print("Заметка успешно сохранена")

def view_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет")
            else:
                print("Список заметок")
                display_notes(notes)

    except FileNotFoundError:
        print("Файл заметок не найден, создайте новый")

def display_notes(notes):
    for idx in range(1, len(notes)+1):
        note = notes[idx - 1]
        print(f"{idx}.{note}")

# def delete_note():
#     try:
#        with open("notes.txt", "r", encoding="utf-8") as file:
#            notes = file.readlines()
#            if not notes:
#                print("Заметок пока нет")
#            else:
#             print("Список заметок")
#             display_notes(notes)
#        note_number = int(input("Введите номер для удаления"))
#        if 1 <= note_number <= len(notes):
#            del notes[note_number - 1]
#            with open("notes.txt", "w", encoding="utf-8") as file:
#                file.writelines(notes)
#                print ("Заметка удалена")
#                break
            

def main_menu():
    while True:
        print("\n=====Меню=====")
        print("1. Создать заметку")
        print("2. Посмотреть заметку")
        print("3. Удалить заметку")
        print("0. Выход")

        choice = input("Выберите опцию (0 - 3):")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        # elif choice == "3":
        #     delete_note_notes()
        elif choice == "0":
            print("Программа завершена")
            break
        else:
            print("Некорректный ввод")