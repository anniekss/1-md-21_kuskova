def ex5_3():

    week = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    weekends = int(input("Введите количество выходных:"))
    print("Ваши выходные дни - ", list(week[-weekends:]))
    week = list(week[:-weekends])
    print("Ваши рабочие дни - ", week)
ex5_3()