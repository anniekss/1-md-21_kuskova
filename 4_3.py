def magicdate(date):
    try:
        day, month, year = map(int, date.split("."))
        if day * month == int(str(year) [-2:]):
            return True
        else:
            return False
    except ValueError:
        return False
user_date = input("Введите дату в формате dd.mm.yyyy: ")
if magicdate(user_date):
    print("Эта дата - магическая!")
else:
    print("Эта дата не является магической.")