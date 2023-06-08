f = open('news.txt', 'r', encoding="utf8")
array = []
prev = 0
for line in f.readlines():
    temp, *post = line.split()
    temp = int(temp)
    if temp > prev:
        array.append(post)
        prev = temp

for post in array:
    print(*post)
