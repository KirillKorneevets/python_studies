a: tuple = 'дед', 'дерево', 'шалаш', 'кабак'
res = tuple(filter(lambda x: x == x[::-1], a))
print(res)