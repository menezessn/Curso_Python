def functions_sum (list1, list2):
    size = min(len(list1), len(list2))
    sum_functions = [
        list1[i]+list2[i] for i in range(size)
    ]
    return sum_functions



list1 = [1, 2, 6, 7, 10]
list2 = [3, 5, 9, 1]
try:
    sum = functions_sum(list1, list2)
    print(sum) 
except TypeError:
    print('Tipo inválido em uma das listas')


list_sum = [x+y for x, y in list(zip(list1, list2))]
print(list_sum)