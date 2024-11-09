def ex6_3():
    students_languages = {
        'Иванов': ['английский', 'французский', 'немецкий'],
        'Петров': ['английский', 'китайский'],
        'Сидоров': ['испанский', 'итальянский'],
        'Козлов': ['китайский', 'японский'],
        'Смирнов': ['французский'],
        'Алексеев': ['английский', 'немецкий', 'китайский']
    }
    allLang = set()
    for languages in students_languages.values():
        allLang.update(languages)
    print(len(allLang))
    print(sorted(allLang))
    print(students_languages.get('китайский'))
    chinese_speakers = [key for key, languages in students_languages.items() if 'китайский' in languages]
    print(chinese_speakers)
ex6_3()