result = ""

while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word == "stop":
        break
    result += word + " "

print("Результат:", result)