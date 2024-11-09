def check3(number):
    if number % 3 == 0:
        return True
    else:
        return False

number = int(input("Введите число: "))
if check3(number):
    print("Число", number, "делится на 3")
else:
    print("Число", number, "не делится на 3")9
