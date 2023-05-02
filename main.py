text = open('files/24_7824.txt').read().rstrip('\n').lower()
maxx = 0
for i in 'abc':
    for j in 'abc':
        for l in 'abc':
            text = text.replace(i + j + l, ' ')
maxx = max(map(len, text.split()[1:-1])) + 4
maxx = max(maxx, 2 + len(text.split()[0]))
maxx = max(maxx, 2 + len(text.split()[-1]))

print(maxx)
