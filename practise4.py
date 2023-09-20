
names = ['megzz','sayed','saad','roll','ali']
'''
result = []

for n in names:
    result.append(len(n))
print(result)

#list comprehension
result_2 = [len(n) if len(n)>3 else '-' for n in names]
print(result_2)

#generator the fastest method of get data back
result_3 = (len(n) for n in names)
print(result_3)

'''

'''
# map func
def mylen(n):
    return len(n)
result_5 = map(mylen,names)
print(list(result_5))


print('-----------------------------------------------')

#filter func
numbers = list(range(1,101))
def get_even_nums(n):
    if n % 2 == 0:
        return n
resultt = filter(get_even_nums,numbers)
print(list(resultt))

'''

#reduce func
from functools import reduce

numbers = list(range(1,101))

def number_sum(x,y):
    return x + y

sum_1 = reduce(number_sum,numbers)
print(sum_1)



















