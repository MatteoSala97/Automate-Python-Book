import time
import sys


x = time.time()
print(x)

sys.set_int_max_str_digits(1000000000)
#calcola quanto tempo impiega un determinato task

def calcProd():
    product  = 1
    for i in range(1, 10000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print("the result is %s digits long," % (len(str(prod))))
print("it took %s seconds to calculate" % (endTime - startTime))


