from functools import reduce

print(reduce(lambda x, y: x * y, [i for i in range(100, 1001)])) #написать то написал, и работает верно, но не понимаю как