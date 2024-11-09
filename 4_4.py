def luckyticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False
    half_length = len(ticket_number) // 2
    first_half = ticket_number[:half_length]
    second_half = ticket_number[half_length:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

user_ticket = input("Введите номер билета: ")
if luckyticket(user_ticket):
    print("Этот билет - счастливый!")
else:
    print("Этот билет не является счастливым.")