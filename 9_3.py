import csv

def task3():
    with open("C:\\Users\\annku\\Downloads\\данные.csv", 'r', encoding='utf-8') as f:
        data = DictReader(f)
        list_products = list(data)
    sum = 0
    for i in list_products:
        product = i.get(('Продукт'))
        quantity = i.get(('Количество'))
        price1 = i.get(('Цена'))
        price = int(quantity) * int(i.get(('Цена')))
        print(f'{product} - {quantity} шт. за {price1} руб.')
        sum = sum + int(price)

    print(f'Итоговая сумма: {sum} руб.')

task3()