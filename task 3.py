n = int(input())
count = 0
max_day = 0

for _ in range (n):
    temp = int(input('temp: '))
    if temp > 0:
        count += 1
    if count > max_day:
        max_day = count
    if temp < 0:
        count = 0
    # else:
    #     if count > max_day:
    #         max_day = count
    #     max_day = count
    #     count = 0
print(max_day)