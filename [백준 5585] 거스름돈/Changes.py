money = int(input())
change = 1000 - money
cnt = 0

for i in [500, 100, 50, 10, 5, 1]:
    cnt += change // i
    change %= i

print(cnt)