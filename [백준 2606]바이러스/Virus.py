com_n = int(input())
con_n = int(input())
g = [[] for i in range(com_n+1)]
visited =[]

for i in range(con_n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

tovisit = [1]
while tovisit:
    a = tovisit.pop()
    visited.append(a)
    for i in g[a]:
        if i not in visited+tovisit:
            tovisit.append(i)

print(len(visited)-1)