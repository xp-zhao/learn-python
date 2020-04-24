from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 5, 6, -7])
print(obj)
print(obj.index)
print(obj.values)

obj2 = Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
print(obj2)
obj2['c'] = -6
print(obj2)

data = {"a": 1, "b": 2, "c": 3}
obj3 = Series(data)
print(obj3)

data_frame = {"city": ["cd", "sh", "bj"],
              "year": [2016, 2017, 2018],
              "pop": [1.5, 1.6, 1.7]}
frame = DataFrame(data_frame)
frame2 = DataFrame(data_frame, columns=("year", "city", "pop"))
# print(frame)
# print(frame2)
# print(frame2["city"])
# print(frame2.year)

# frame2['new'] = 100
# print(frame2)
# 
# frame2['cap'] = frame2.city == 'cd'
# print(frame2)
# 
# pop = {"bj": {2008: 1.5, 2020: 2.0},
#        "sh": {2008: 2.0, 2020: 1.5}}
# frame3 = DataFrame(pop)
# print(frame3)
# print(frame3.T)
# 
# obj4 = Series([1, 2, 3, 4], index=['d', 'c', 'b', 'a'])
# obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# print(obj5)
# 
# obj6 = Series(['blue', 'origin', 'yellow'], index=[0, 2, 4])
# print(obj6.reindex(range(6), method="ffill"))
# print(obj6.reindex(range(6), method="bfill"))

import numpy as np

data3 = Series(np.random.random(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data3)
print(data3['b':'c'])
