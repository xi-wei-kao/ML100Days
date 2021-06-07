print("hellow HW5","---"*20,sep="\n")
"""
    1. 產生一個 1-11 的一維陣列，並且把 3-6 由正數變成負數。
    2. 試著從一個隨機陣列中，找出比 0.5 大的數有幾個？
"""
# 1.
import numpy as np
a=np.arange(11)+1
print("產生1~11 的一維陣列：", a, sep="\n")
for i in np.arange(10):
    if (i>=3-1) & (i<=6-1):
        a[i]=a[i]*-1
    else:
        a[i]=a[i]
print("把 3~6 正數換成負數：", a, sep="\n")
print("--"*20,"分隔線","--"*20)
# 2.
rng=np.random.rand(10+1)
print("一個隨機陣列：", rng, sep="\n")
condition=rng>0.5
result=np.size(rng[condition])
print("比 0.5 大的值「%1.0f」個"%(result))