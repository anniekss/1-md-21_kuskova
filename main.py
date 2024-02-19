# a=input()
# b=input()
# if a==b:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
#
#
# a=int(input())
# if a%3 and a%100!=0 or a%400:
#     print("Год", a, "- високосный")
# else:
#     print("Это год не високосный")


a = input()
b = input()
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif a == 'красный' and b == 'красный':
    print('красный')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif a == 'желтый' and b == 'желтый':
    print('желтый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print('зеленый')
elif a == 'синий' and b == 'синий':
    print('синий')
else:
    print('ошибка цвета')


# a=input()
# b=input()
# if a==1:
#     print("купейный вагон")
# elif a==2:
#     print("плацкартный вагон")
# elif a<1 or a>2:
#     print("ошибка")
# elif b%2==0:
#     print("Вернее место")
# elif b%2!=0:
#     print("Нижнее место")