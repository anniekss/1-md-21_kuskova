def checkseat(seat_number):
    compartment = [1, 2, 3, 4, 5, 6]
    side = [19, 20, 21, 22, 23, 24]

    if seat_number in compartment:
        if seat_number % 2 == 0:
            print("Верхнее место в купе")
        else:
            print("Нижнее место в купе")
    elif seat_number in side:
        if seat_number % 2 == 0:
            print("Верхнее боковое место")
        else:
            print("Нижнее боковое место")
    else:
        print("Номер не определен")
seat_number = int(input("Введите номер места: "))
checkseat(seat_number)