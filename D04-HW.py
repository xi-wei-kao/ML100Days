print("hellow world","---"*20, sep="\n")
"""
1. [簡答題] 請問下列程式碼，運算結果分別為何？
a = np.array( [20,30,40,50] )
b = np.array( [1,2,3,4] ) 
c = 1
d = np.array( [1] )
e = np.array( [1,2] ) 
2. 如何在不用迴圈的情況下計算 (A+B)*(-A/2) ？那用迴圈怎麼做？
3. 請問如何計算「1x6 的單位矩陣」和「6x1 的單位矩陣」的內積和外積？
"""
from os import sep
import numpy as np
from numpy.core.numeric import ones
# 1.
a = np.array( [20,30,40,50] ) #建立 1*4 陣列 a
b = np.array( [1,2,3,4] ) # 建立 1*4 陣列 b
c = 1 # 宣告變數 c
d = np.array( [1] ) # 建立 1*1 陣列 d
e = np.array( [1,2] ) # 建立 1*2 陣列 e
print("---"*20)

# 2.
result1=(a+b)*((a*-1)/2)
print(result1) # 不用迴圈
print("---"*20)
result2=np.zeros(4)
for i in np.arange(4).tolist():
    result2[i]=(a[i]+b[i])*((a[i]*-1)/2)
print(result2) # 用迴圈
print("---"*20)
# 3.
arr1=np.ones(6)
arr2=np.ones(6).reshape(6,1)
print(arr1,arr2,sep="\n")
result3=arr1@arr2 # 內積→(6*1)@(1*6)=(1*1)
print("內積：", result3,"---"*20,sep="\n")
result4=np.outer(arr1,arr2)
print("外積：", result4 ,sep="\n") # 外積→(6*1)outer(1*6)=(6*6)
