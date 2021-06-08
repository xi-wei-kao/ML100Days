print("hellow D06-HW", "---"*20, sep="\n")
"""
    1. [簡答題] 請問下列這三種方法有什麼不同？
        1-1. print(a.sum())
        1-2. print(np.sum(a))
        1-3. print(sum(a)) 
    2. 請對一個 5x5 的隨機矩陣作正規化的操作。
    3. 請建立一個長度等於 10 的正整數向量，並且將其中的最大值改成 -1。
"""
#1. 
#   print(a.sum()) → 物件方法的寫法
#   print(np.sum(a)) → 套件函式寫法
#   print(sum(a)) → 內建總和函數寫法

#2. 正規化[將最大值轉為1；最小值轉為0的過程?]
import numpy as np
from numpy.core.fromnumeric import size
a = np.random.rand(25).reshape((5,5))
print("原來的矩陣：", a, sep="\n")
print("==="*20)
a = (a-np.min(a))/(np.max(a)-np.min(a))
print("正規化的矩陣：", a, sep="\n")
print("---"*20)
# 3.
a = np.random.randint(10,100, size=(10))
print("原來矩陣：", a, sep="\n")
a[np.argmax(a)] = a[np.argmax(a)]*(-1)
print("最大值轉負數矩陣：", a, sep="\n")

