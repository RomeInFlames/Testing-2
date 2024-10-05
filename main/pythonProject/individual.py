print("Введите по порядку стоимость монитора, блока, клавиатуры, мыши и количество их наборов")
monitor = int(input())
block = int(input())
klaviatura = int(input())
mish = int(input())
N = int(input())
a = monitor + block + klaviatura + mish
print(a*3, a*N)