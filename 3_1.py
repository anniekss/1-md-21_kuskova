n = int(input("Введите количество слов: "))
result = ""

for i in range(n):
    word = input("Введите слово: ")
    result += word + " "

print("Результат: ", result)