# Создание текстового документа
# with open("example.txt", "w", encoding=UTF8) as file:
#     file.write("Привет, мир")

# # Чтение
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Создание файла с числами
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
                   file.write(str(i)+"\n")