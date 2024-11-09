numbers = [1, 2, 3, 4, 5]
user_number = int(input("Введите число: "))
if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
print("Исходный список: ", numbers)