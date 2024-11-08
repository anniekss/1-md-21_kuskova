def mixcolors(color1, color2):
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("фиолетовый")
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("оранжевый")
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("зеленый")
    else:
        print("Ошибка! Введите только 'красный', 'синий' или 'желтый'")
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")
mixcolors(color1, color2)