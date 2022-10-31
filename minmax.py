
from random import *
print("Пошук min і max")
lst = [randint(-100, 100) for _ in range(10)]
print([lst[i] for i in range(10)])
print("index min =", lst.index(min(lst)), "min =", min(lst), "count min =", lst.count(min(lst)))
print("index max =", lst.index(max(lst)), "max =", max(lst), "count max =", lst.count(max(lst)))
