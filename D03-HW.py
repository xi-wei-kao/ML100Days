print("hellow world", "---"*20, sep="\n")
"""
1. [簡答題] 請比較 np.zeros 和 np.empty 產生出來的陣列有何差異？
為什麼要設計兩種方法？
2. 在不用「整數亂數方法」的限制下，如何將包含小數的轉換整數？
請將給定的 a 陣列當中的元素變成去掉小數變成整數。
    2.1 承上題，怎樣可以限制整數的範圍介於 m - n 之間？
    請將給定的 a 陣列當中的元素的範圍調整成 m - n 之間。
"""
from os import sep
import numpy as np
from numpy import random
from numpy.core.fromnumeric import shape, size
data=np.zeros([2,3])
print(data, data.dtype, sep="\n")
data=np.empty([2,3])
print(data, data.dtype,sep="\n")
""""
1.
  (1) np.zeros 的陣列為全部元素都預設為「0」的陣列。
  (2) np.empty 的陣列為全部元素都「未指定」的陣列。
  (3) 前者指定為「0」代表預設的陣列資料皆為「0」；然而後者為記憶體
      中未特定指定處，後者未指定特性，在運算速度較快。
"""
print("---"*20)

# 2.
i=5
a=np.round(np.random.rand(i)*10)
print("顯示一個小數轉換「%d」個觀察值0~10的整數陣列："%(i), a, sep="\n")
print("---"*20)
# 2.1
m=12
n=20
a=(a-a)+np.random.randint(m,n+1 ,size=a.shape)
# 把 a 陣列歸零再加回 m ~ n 之間的整數亂數矩陣值。
print("顯示「%1.0f」到「%1.0f」之間的整數陣列："%(m,n), a, sep="\n")
