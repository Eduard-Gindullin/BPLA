# Прочитать несколько текстовых файлов
# Объеденить их содержимое
# Записать результат в новый файл
# Вычеслить количество объединенных строк

def read_files(filenames):
    all_lines = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            all_lines.extend(file.readlines())
    return all_lines

def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main(output_file, input_files):
    combined_lines = read_files(input_files)
    write_file(output_file, combined_lines)
    print(f"Оъединенные строки: {len(combined_lines)}")

input_files = ['file1.txt', "file2.txt"]

main("combined.txt", input_files)