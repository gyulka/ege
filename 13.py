from collections import defaultdict


def obhod(start, end, path):
    if start == end and path: # если ищем циклы в графе то чтобы не искали циклы 0 длины
        return end
    if start in path: # если мы в этой вершине уже были то выходим из этой ветки
        return 0
    ans = 0
    for i in dict1[start]:
        ans += obhod(i, end, path + i)
    return ans


n = 10 # количество рёбер
dict1 = defaultdict(list)
for i in range(n):# вводим граф, да долго, но без ошибок сработает
    a, b = input().split()
    dict1[a].append(b)
print(obhod('','',''))