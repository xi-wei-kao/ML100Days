print("hellow D10-HW\n","==="*20)
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd

#   1.  [簡答題] 請問下列四種不同的 DataFrame 選取結果有什麼差異？
#       請根據提供的資料，選擇出下列的要求：
data = pd.DataFrame({
    "var1":[3,2,5,4,5]
    ,"var2":[3,5,4,8,2]
    ,"var3":[5,8,7,2,6]
    ,"var4":[9,8,7,1,0]
    ,"var5":[10,5,9,1,8]
})
print("* 原資料:\n", data)
    # - select the first 3 rows.
print("* 選出首三列:\n", data[0:3])
    # - select the odd rows. (index = 1, 3, 5)
print("* 選出奇數索引列:\n", data[1: :2])
    # - select the last 2 columns.
print("* 選出最後兩欄變數:\n", data.iloc[:,[-2,-1]])
    # - select the even columns. (index = 0, 2, 4)
print("* 選出偶數資料/欄:\n", data.iloc[0: :2,0: :2])
print("---"*20)
#   2. 請根據提供的資料，選擇出下列的要求：
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print("* 原來矩陣:\n",df)
    # - 1. filtered by first column > 20?
condition = df.loc[:,0] > 20
print("* 第一欄 > 20 者:\n", df[condition].iloc[:,0])
    # - 2. filtered by first column + second column > 50
condition = df.loc[:,0]+df.loc[:,1] >50
print("* 前兩欄加起來 > 50:\n",df[condition].iloc[:,0:2])
    # - 3. filtered by first column < 30 or second column > 30
condition = (df.loc[:,0] <30) | (df.loc[:,1] > 30)
print("* 第一欄 <30 或 第二欄 >30:\n",df[condition].iloc[:,0:2])
    # - 4. filtered by total sum of row > 100
condition = df.sum(axis=1) > 100
df["sum"] = df.sum(axis=1)
print("列總和 > 100 者:\n",df[condition])

