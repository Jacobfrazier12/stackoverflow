from os import getcwd, path, remove, mkdir, listdir, walk
from pandas import DataFrame, read_csv, concat, isna, to_numeric, Series
import matplotlib as plt
from numpy import nan
import pycountry 


file_path = path.join(getcwd(), "Data.csv")
file_path2 = path.join(getcwd(), "Data2.csv")
data = read_csv(filepath_or_buffer=file_path, low_memory=False)
#data = data[(data["Year"]==2021)]
languages_path = path.join(getcwd(), "Languages.csv")
gender_path = path.join(getcwd(), "Gender.csv")
database_path = path.join(getcwd(), "Databases.csv")
country_path = path.join(getcwd(), "Country.csv")
opsys_path = path.join(getcwd(), "OpSys.csv")
cols = ["Languages", "Databases", "Country", "Gender", "OpSys"]
paths = [languages_path, database_path, country_path, gender_path, opsys_path]
      
   

        
         