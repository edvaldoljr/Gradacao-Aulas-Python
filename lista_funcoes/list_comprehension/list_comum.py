#modelo tradicional para criar uma lista com 10 elementos

list1 = []
for i in range(3):
    list1.append(i)
print(list1)

#com a list comprehension ficaria assim:

list2 = [i for i in range(10)]
print(list2)