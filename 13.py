from collections import defaultdict


def obhod(start, end, path):
    if start == end and path:  # если ищем циклы в графе то чтобы не искали циклы 0 длины
        return 1
    if start in path:  # если мы в этой вершине уже были то выходим из этой ветки
        return 0
    ans = 0
    for i in dict1[start]:
        ans += obhod(i, end, path + start)
    return ans


# n = 10  # количество рёбер
# dict1 = defaultdict(list)
# for i in range(n):  # вводим граф, да долго, но без ошибок сработает
#     a, b = input().split()
#     dict1[a].append(b)
# print(obhod('', '', ''))

n = 10
dict1 = defaultdict(list)
for i in range(n):
    lis = input().split()
    dict1[lis[0]] = lis[1:]
print(obhod('е', 'е', ''))
# а б г
# б д
# в а б г д
# д и л е
# и л
# е л в
# л к
# к ж
# г е ж
# ж е