print("hellow D08-HW", "---"*20,sep="\n")
"""
1. [簡答題] 請問 Pandas 套件最主要的貢獻是什麼？
2. 根據提供的資料集，印出他們的屬性分別為何？
（屬性：shape、size、values、index、columns、dtypes、len）
"""
from os import sep
import pandas as pd
# 1. 
#   (1) 提供 DataFrame 結構，使用字典方式管理每個 key 的 list-value 使用 C 之
# 核心運算速度快。
#   (2) 提供許多方便函數尤其在管理科學、統計、應用等等領域廣泛使用
#   (3) 對於檔案讀寫非常方便：如 csv 、 excel 、 sql 等等。 

# 2. 
a = pd.DataFrame({
    "names":["csv","json","xlsx"]
    ,"work":[100,200,150]
})
print("---"*20)
print("1. 形狀：", pd.DataFrame(a).shape,sep="\n")
print("2. 大小：", pd.DataFrame(a).size,sep="\n")
print("3. 資料值：", pd.DataFrame(a).values,sep="\n")
print("4. 索引：", pd.DataFrame(a).index,sep="\n")
print("5. 欄位名稱(key names)：", pd.DataFrame(a).columns,sep="\n")
print("6. 資料型態(每個值串列的)：", pd.DataFrame(a).dtypes,sep="\n")
print("7. 資料長度：", pd.DataFrame(a).__len__(),sep="\n")

