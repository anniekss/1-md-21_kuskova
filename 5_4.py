import random
StudentsMD = ['Алексеев', 'Тянутова', 'Керган', 'Головченко', 'Иванов', 'Здобнов', 'Куськова', 'Маценко', 'Уланова', 'Лашкова']
StudentsDD = ['Аузяк', 'Ахмедов', 'Васильев', 'Жарко', 'Лыткин', 'Рахимов', 'Сидорова', 'Мухин', 'Иванов', 'Обрывалина']
team = tuple(random.sample(StudentsMD, 10)[:5] + random.sample(StudentsDD, 10)[:5])
print(StudentsMD)
print(StudentsDD)
print(team)
team = tuple(sorted(list(team)))
if "Иванов" in team:
    print (list(team).count("Иванов"))
else:
    print("No ")