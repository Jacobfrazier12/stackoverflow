from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric
import matplotlib as plt
from numpy import nan
import pycountry 


path = path.join(getcwd(), "Data.csv")

data = read_csv(filepath_or_buffer=path, low_memory=False)
data["Languages"] = data["Languages"].str.split("\t").explode(True)
print(data.groupby("Year").filter(lambda x: (x["Year"]==2017).all())["Languages"].value_counts())
	
