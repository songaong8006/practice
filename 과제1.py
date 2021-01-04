import math
import time

start = time.time()

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
# Add up numbers until the sum becomes greater than 10

data = [1, [-2, [[[4]]], [0, 5], [], 3], [4], 2, 7]
a = flatten(data)
for e in a:
    print(e)


print("걸린 시간은 :", time.time() - start) 

 
