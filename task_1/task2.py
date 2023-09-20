import numpy as np

array = np.random.randint(-1000,1001, 1024)
array.sort()
array = array[array >= 0]

print(array)