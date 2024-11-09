def ex6_2():
    alphabet = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Щ': 10, 'Ъ': 10, 'Ф': 10
    }
    value = 0
    word = input("Введите слово: ")
    word = word.upper()
    splitted = list(word)
    for i in range(len(splitted)):
        if splitted[i] in alphabet:
            value += alphabet.get(splitted[i])
    print(value)
ex6_2()