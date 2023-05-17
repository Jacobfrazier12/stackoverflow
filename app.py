from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna
import matplotlib as plt

for year in range(2011, 2023):
    if year == 2011:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        data = data.iloc[:, [0,1, 30]]
        #print(data.columns)
    if year == 2012:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        data = data.iloc[:, [0,2, 22]]
        #print(data.columns)
    if year == 2013:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        data = data.iloc[:, [0,2, 22, 56, 81]]
        for column in data.columns:
            pass
            #print(column)
    
    if year == 2014:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        data = data.iloc[:, [0, 3, 42, 67]]
        for column in data.columns:
            pass
            #print(column, "\n")
    
    def combine_languages(row):
        languages = []
        for col in range(5, 48):
            value = data.iloc[row.name, col]
            if not isna(value):
                languages.append(value)
            return ";".join(languages)
        
    if year == 2015:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        data = data.iloc[:, [0,1, 2, 6, 7, *[col for col in range(8,51)]]]
        data["Languages"] = data.apply(lambda row: combine_languages(row), axis=1)
        data = data.iloc[:, [*range(0, 5), 48]]
        for column, index in zip(data.columns, data.index.tolist()):
            pass
           #print(index, column)
    
    if year == 2016:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"))
        #data = data.iloc[:, [1, 4, 6, 18 31]]
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            print(index, column)