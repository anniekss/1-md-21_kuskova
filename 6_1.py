def ex6_1():
    slovar = {"USA": "WASHINGTONE", "RUSSIA": "MOSCOW", "FRANCE": "PARIS", "ITALY": "ROME"}

    for key, value in slovar.items():
        print("{}: {}".format(key, value))
    country = input("Введите название страны: ").upper()
    print("Столица", country, "-", slovar.get(country))
    sorted_slovar = sorted(slovar.items(), key=lambda f: f[1])
    print(sorted_slovar)
    sorted_slovar = dict(sorted_slovar)
    for key, value in sorted_slovar.items():
        print("{}: {}".format(key, value))
ex6_1()