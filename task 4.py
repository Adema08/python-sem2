n = int(input())
massa_1 = int(input('massa_1: '))
max = massa_1
min = massa_1

for _ in range(n - 1):
    massa = int(input('massa: '))
    if massa_1 > massa:
        max = massa
    if massa_1 < massa:
        min = massa
print(min, max)