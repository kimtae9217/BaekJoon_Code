def make_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

star = ["***", "* *", "***"]
n = int(input())
e = 0 # (n의 지수)
while n != 3:
    n = int(n/3)
    e += 1

for i in range(e):
    star = make_stars(star)
for i in star:
    print(i)


