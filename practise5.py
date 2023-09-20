# dict comprehension
'''
d = {'t1':-40,'t2':-20}
c = {k.replace('t','c'):(5/9)*v-32 for (k,v) in d.items()}
print(c)
'''
'''
c2 = list(map(lambda x:(5/9)*x-32,d.values()))
#result = dict(zip(d.keys(),list(map(lambda x:(5/9)*x-32,d.values()))))
result = dict(zip(d.keys(),c2))
print(result)
'''






# decorator
'''
import time
import math

def calc_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'THE Total Time is {end-start}')
        return result
    return inner

@calc_time
def mysum(x):
    print(math.factorial(x))
print(mysum(1000))
'''





# type hint

def mysum(x:int,y:int) -> int: # it makes a validation to the code
    for n in range(x):
        y += n
    return y
print(mysum(5,1.5))# not gonna get error but if we use another interpreter(mypy) it gonna makes error 
# cuz i said above that the output of def and the 2 parameters must be intger not float


''''it could be something bigger like class or somethig
for instance -> class Calc:

                c:Calc = Calc()

'''



















