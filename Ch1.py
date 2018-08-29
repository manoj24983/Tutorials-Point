#Data Operations in Numpy
# more than one dimensions
import numpy as np
import pandas as pd
a = np.array([[1, 2], [3, 4]])
print (a)
# minimum dimensions
a = np.array([1, 2, 3,4,5], ndmin = 2)
print (a)

# dtype parameter
a = np.array([1, 2, 3], dtype = complex)
print (a)

#Data Operations in Pandas
#import the pandas library and aliasing as pd
print("Series data")
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

#list creation and methods of lists
a=list(range(10))
for item in a:
    print(item)
a.append("manisha")
a.append("manoj")
a.append(8765)
for item in a:
    print(item)


