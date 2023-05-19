from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric
import matplotlib as plt
from numpy import nan

path = path.join(getcwd(), "Data.csv")

data = read_csv(filepath_or_buffer=path)
data["Languages"] = data["Languages"].str.split(";").explode(True).str.strip()
data["Databases"] = data["Databases"].str.split(";").explode(True)
data["Gender"] = data["Gender"].str.split(";").explode(True).str.strip()
print(data["Gender"].unique())

data = data[~data["Languages"].isna()]
data = data[~data["Languages"].str.isnumeric()]
print(data["Languages"].value_counts().head(15))
#print(data.groupby("Year")["Gender"].value_counts())