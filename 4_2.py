def divide100():
    try:
        number = float(input("Введите число: "))
        result = 100 / number
        print("Результат деления 100 на", number, " =", result)
    except ValueError:
        print("Ошибка! Введите число, а не строку.")
    except ZeroDivisionError:
        print("Ошибка! Нельзя делить на ноль.")
divide100()