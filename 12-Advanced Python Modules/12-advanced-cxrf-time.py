import time
import timeit

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str,range(n)))

print(func1(10))
print(func2(10))
#########################################################################

# current time
start_time = time.time()
# run code
result1 = func1(1000000)
# current time after
end_time = time.time()
# elapsed time
elapsed_time = end_time-start_time
print(elapsed_time)

# current time
start_time = time.time()
# run code
result1 = func2(1000000)
# current time after
end_time = time.time()
# elapsed time
elapsed_time = end_time-start_time
print(elapsed_time)
#########################################################################

stmt='''
func1(100)
'''

setup='''
def func1(n):
    return [str(num) for num in range(n)]
'''
t1=timeit.timeit(stmt,setup,number=1000000)
print(t1)

stmt='''
func2(100)
'''

setup='''
def func2(n):
    return list(map(str,range(n)))
'''
t2=timeit.timeit(stmt,setup,number=1000000)
print(t2)

#########################################################################
# use %%timeit
# func_one(100)
# this will run in jpter notebooks
# then %%timeit
#func_two(100)  in the next cell


