import time
from functools import wraps

def timeit(func):
    '''
    this is the decorator function
    :param func: the test function
    :return: return the function to be executed
    '''
    @wraps(func)
    def myfunc(a,b):
        start = time.perf_counter_ns()
        func(a,b)
        end = time.perf_counter_ns()
        print('the time is {}'.format(end - start))
    return myfunc



@timeit
def sum1(a,b):
    '''
    this is the sum func
    :param a: the sum param
    :param b: the sum param
    :return: the result
    '''
    sum = a + b
    print(sum)


sum1(2,4)

print(sum1.__doc__)
print(timeit.__doc__)
