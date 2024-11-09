import random
def ex5_2():

    newOne = []
    spisok = [random.randint(1, 10) for x in range(0, 50)]
    for i in range(len(spisok)):
        if (spisok[i] in spisok[i+1:]) and spisok[i] not in newOne:
            newOne.append(spisok[i])
    print(newOne)
    print(spisok)
ex5_2()