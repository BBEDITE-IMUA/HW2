a = int(input())
d = 1
result = 1
for i in range(1, a + 1):
    #  Вычисляем факториал числа в переменной d:
    d = d * i
    # К переменной result пребовляем факториал в минус 1 степени:
    result += 1 / d
print(result)