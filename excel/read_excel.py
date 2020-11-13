import pandas as pd

data = pd.read_excel("xxx.xlsx")
columns = data.columns.values.tolist()
for idx, row in data.iterrows():
    set_name = set()
    code = row['xx']
    name1 = row['xxx']
    name2 = row['xxx.1']
    name3 = row['xxx.2']
print(columns)

