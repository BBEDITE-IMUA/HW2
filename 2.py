a = int(input())
result = "NO"
#  Вводим столько значений сколько указали цифрой:
for i in range(a):
    b = int(input())
    #  Если в числах b есть 0 то выводим YES:
    if b == 0:
        result = "YES"
print(result)