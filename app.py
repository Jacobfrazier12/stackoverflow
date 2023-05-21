from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric
import matplotlib as plt
from numpy import nan

path = path.join(getcwd(), "Data.csv")

data = read_csv(filepath_or_buffer=path)
data["Languages"] = data["Languages"].str.split(";").explode(True)
data["Databases"] = data["Databases"].str.split(";").explode(True)
data["Gender"] = data["Gender"].str.split(";").explode(True)
#data = data.loc[data.isna().mean() < 0.80]
print(data["Country"].value_counts().head(300))
#print(data.groupby("Year")["Gender"].value_counts())