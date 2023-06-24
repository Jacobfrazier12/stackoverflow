from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric
import matplotlib as plt
from numpy import nan
import pycountry 


path = path.join(getcwd(), "Data.csv")

data = read_csv(filepath_or_buffer=path, low_memory=False)
#data["Languages"] = data["Languages"].str.split("\t").explode(True)
#data["Databases"] = data["Databases"].str.split("\t").explode(True)
#data["Gender"] = data["Languages"].str.split("\t").explode(True)
#data["Gender"] = data["Gender"].str.split("\t").explode(True)
#data = data[(data["Languages"] == "Android")]
print(data["Languages"].value_counts())
#data["Databases"] = data["Databases"].str.split("\t").explode(True)
#data.to_csv(path_or_buf = "temp.csv", index = False, mode = "w+")  