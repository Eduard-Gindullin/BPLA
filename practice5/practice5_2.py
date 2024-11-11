# Подсчитать количество строк
#  Подсчитать количество слов
# Подсчитать количество символов
# Вывести топ 3 самых часто слова

from collections import Counter

def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())
    
def count_words(filename):
    with open(filename, "r") as file:
        return len(file.read().split())
    
def count_characters(filename):
    with open(filename, "r") as file:
        return len(file.read())
    
def count_top_words(filename, top_n=3):
    with open(filename, "r") as file:
        words = file.read().split()
    words_count = Counter(words)
    return words_count.most_common(top_n)

def analize_file(filename):
    lines = count_lines(filename)
    words = count_words(filename)
    characters = count_characters(filename)
    top_words = count_top_words(filename)
    return {
        "Строки" : lines,
        "Слова"  : words,
        "Символы" : characters,
        "Топ 3"   : top_words
    }

print(analize_file("dataset_home.txt"))