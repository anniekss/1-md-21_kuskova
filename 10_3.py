with open('en-ru.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

dictionary = {}

for line in lines:
    words = line.strip().split(' - ')
    english_word = words[0]
    russian_translations = words[1].split(', ')

    for russian_word in russian_translations:
        dictionary[russian_word] = english_word

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for russian_word in sorted(dictionary.keys()):
        english_word = dictionary[russian_word]
        file.write("{} - {}\n".format(russian_word, english_word))