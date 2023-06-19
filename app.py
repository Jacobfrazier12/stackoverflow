from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric
import matplotlib as plt
from numpy import nan
import pycountry 


path = path.join(getcwd(), "Data.csv")

data = read_csv(filepath_or_buffer=path, low_memory=False)
#data = data.str.split("\t").explode(True)
for col in data.columns:
    try:
        data[col] = data[col].str.split("\t").explode(True)
    except AttributeError as e:
        pass

data.to_csv("temp.csv", mode="w+", index=True)
temp = read_csv("temp.csv")
print(data["Languages"].value_counts())
#print(data.groupby("Year").filter(lambda x: (x["Year"]==2018).all())["Languages"].value_counts())
	
