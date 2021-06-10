print("D09-HW","---"*20,sep="\n")
"""
1. 請建立類似提供結果的 DataFrame：
2. 請問如果現在有一個 DataFrame 如下，請問資料在 Python 中可能長怎樣？
        city  visitor weekday
    0  Austin      139     Sun
    1  Dallas      237     Sun
    2  Austin      326     Mon
    3  Dallas      456     Mon
3. 假設你想知道每個 weekday 的平均 visitor 數量，可以怎麼做？
"""
# 1. 
import pandas as pd
from pandas.core.indexes.base import Index
a = pd.DataFrame({
    "apple":[30]
    ,"banana":[21]
})
print("結果如下：", a, sep="\n")
b = pd.DataFrame({
    "Apples":[35,41]
    ,"Bananas":[21,34]
}, index=["2017 Sales","2018 Sales"])
print("結果如下：", b, sep="\n")
print("==="*20)
# 2. 
c = pd.DataFrame({
    "City":["Austin","Dallas","Austin","Dallas"]
    ,"visitor":[139,237,326,456]
    ,"weekday":["Sun","Sun","Mon","Mon"]
}, index=None)
print("結果如下：", c, sep="\n")
print("==="*20)
# 3. 
SunData = c.loc[c["weekday"]=="Sun"]
print("Sun的資料：",SunData,sep="\n") # 篩選出 Sun 資料
SunMean = SunData["visitor"].mean()
print("Sun 的平均 visitor：", SunMean)
Mondata = c.loc[c["weekday"]=="Mon"]
print("Mon的資料：", Mondata, sep="\n")
MonMean = Mondata["visitor"].mean()
print("Mon 的平均 visitor：", MonMean)