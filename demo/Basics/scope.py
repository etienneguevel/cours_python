from copy import copy

list_valeurs = list(range(10))
def add_and_sum(l, a, b):
    temp = l
    temp.append(a)
    temp.append(b)
    return sum(temp)

print(list_valeurs)
print(add_and_sum(list_valeurs, 2, 3))
print(list_valeurs)