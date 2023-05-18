from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna
import matplotlib as plt

from numpy import nan
for year in range(2011, 2023):
    
   

    
    def clean_2013_os(row):
        if "Windows" in str(row):
            return "Windows"
        elif "Mac" in str(row):
            return "MacOS"
        elif str(row) == "Response":
            return nan
        else: return row
   
    if year == 2013:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [0,2, 81]]
        data["Which desktop operating system do you use the most?"] = data["Which desktop operating system do you use the most?"].apply(lambda row: clean_2013_os(row))
       
        for column, index in zip(data.columns, data.index.tolist()):
            pass
           # print(index, column)
    
    def clean_2014_os(row):
        linux_list = ["Linux", "Ubuntu", "Debian", "Mint", "Fedora"]
        if "Windows" in str(row):
            return "Windows"
        elif "Mac" in str(row):
            return "MacOS"
        elif str(row) in linux_list:
            return "Linux"
        elif str(row) == "Response":
            return nan
        else: return row 
    
    if year == 2014:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [0, 67]]
        data["Which desktop operating system do you use the most?"] = data["Which desktop operating system do you use the most?"].apply(lambda row: clean_2014_os(row))
        #print(data.iloc[:, 1].value_counts())
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    def combine_languages(row):
        languages = []
        for col in range(5, 48):
            value = data.iloc[row.name, col]
            if not isna(value):
                languages.append(value)
            return ";".join(languages)

   
    
    def clean_2015_2016_os(row):
        linux_list = ["Other Linux", "Ubuntu", "Debian", "Mint", "Fedora"]
        if "Windows" in str(row):
            return "Windows"
        elif str(row) in linux_list:
            return "Linux"
        elif "Mac" in str(row):
            return "MacOS"
        elif str(row) == "Response":
            return nan
        else: return row    
    
    if year == 2015:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [0, 1, 2, 6, 7, *[col for col in range(8,51)]]]
        data["Languages"] = data.apply(lambda row: combine_languages(row), axis=1)
        data["Desktop Operating System"] = data["Desktop Operating System"].apply(lambda row: clean_2015_2016_os(row))
        data = data.iloc[:, [0, 2, 3, 48]]
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    if year == 2016:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [1, 6, 18, 31]]
        data["desktop_os"] = data["desktop_os"].apply(lambda row: clean_2015_2016_os(row))
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    def clean_2017_os(row):
        
        cleaned_list_of_os = []
        if "Windows" in str(row):
            cleaned_list_of_os.append("Windows")
        elif "Mac OS" in str(row):
            cleaned_list_of_os.append("MacOS")
        elif "Linux" in str(row):
            cleaned_list_of_os.append("Linux")
        if cleaned_list_of_os:
         return ";".join(cleaned_list_of_os)
        else: return nan
            




    if year == 2017:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [3, 145,88, 94]]
        data["HaveWorkedPlatform"] = data["HaveWorkedPlatform"].apply(lambda row: clean_2017_os(row))
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
   
    def clean_2018_languages(row):
        languages = str(row)
        return languages.split(";")

   
    if year == 2018:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [3, 65,74,120, 124]]
        #data["LanguageWorkedWith"] = data["LanguageWorkedWith"].apply(lambda row: clean_2018_languages(row))
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    if year == 2019:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [6, 43, 54, 78]]
        data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
        #print(data.iloc[:, 2].value_counts())
       
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    if year == 2020:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [ 8, 17, 22, 41]]
        data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
        #print(data["OpSys"].value_counts())
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    if year == 2021:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [3, 16, 18, 30, 39]]
        data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
        #print(data["OpSys"].value_counts())
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)
    
    if year == 2022:
        data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
        data = data.iloc[:, [15, 19,21, 33, 34, 50]]
        #print(data.iloc[:, 4].value_counts())
        for column, index in zip(data.columns, data.index.tolist()):
            pass
            #print(index, column)