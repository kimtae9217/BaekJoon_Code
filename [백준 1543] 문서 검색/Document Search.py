doc = input()
word = input()
 
index = 0
cnt = 0
 
while len(doc) - index >= len(word):
    if doc[index:index+len(word)] == word:
        cnt += 1
        index += len(word)
    else:
        index += 1
 
print(cnt)