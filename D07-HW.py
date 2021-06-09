print("hellow D07-HW", "---"*20, sep="\n")
"""
1. 請比較對一個 100 x 100 * 100 的陣列，使用不同方法對每一個元素 +1 的時間比較。
2. 如何從一個陣列中，找出出現頻率最高的數值與位置？
3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
"""
from typing import Counter
import numpy as np
import time

from numpy.core.defchararray import count
from numpy.core.numeric import argwhere
from numpy.lib.shape_base import column_stack
# 1.
a = np.ones(1000000).reshape((100,100,100))
time = time.process_time()
a = a + 1 # 方法 1 [直接加, 0.437500秒]
# a[:] = a[:] + 1 # 方法 2 [寫成切片逐元加, 0.406250秒]
print(a,"\n","運行「%f」秒"%(time))
print("---"*20)
#2.
a = np.random.randint(10,20,size=[20])
print("原來矩陣：", a, sep="\n")
counters = np.bincount(a)
mode = np.argmax(counters) # 前面 0 後面顯示該索引值出現幾次
condition = a == mode
condition_index = np.where(condition)
print("1. 出現最多次：", a[condition]
, "2. 索引位置：", condition_index
, "3. 眾數為「%i」"%(mode), sep="\n")
print("---"*20)
# 3. 
a = np.arange(10)
print(a)
a_list = list(a)
a_list2 = a.tolist()
print(a_list)
print(a_list2) # 一樣意思