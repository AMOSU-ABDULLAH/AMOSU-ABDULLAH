# ade  = "jhdjhsdkjhsf"
# print(ade)

import pandas as pd


# df = pd.DataFrame([[1,1,2],[2,34,3],[1,3,4]], columns = ["A", "B", "C"], index = ["x","y","z"])

df = pd.DataFrame([[1,1,2],[2,34,3],[1,3,4]], columns = ["A", "B", "C"], index = ["x","y","z"])

print(df.columns)
print(df.info())
print(df.describe())
print(df.tail(3))

coffee = pd.read_csv('../DATAS/music.csv')