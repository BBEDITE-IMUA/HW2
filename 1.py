a = int(input())
#  Задаём последовательность от 2 т.к. делитель 1 не считается и a + 1 чтобы значение самой a тоже учитывалось:
for i in range(2, a + 1):
    #  Ищем первое число которое делит a без остатка:
    if a % i == 0:
        print(i)
        # Останавливаем цикл:
        break