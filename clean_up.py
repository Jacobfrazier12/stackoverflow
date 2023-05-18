from time import time
from os import getcwd, path, remove, mkdir, listdir, walk
from shutil import rmtree
from zipfile import ZipFile
from pandas import DataFrame, read_csv, concat, isna
from requests import get, exceptions
import matplotlib as plt
import re
import chardet
from fake_useragent import UserAgent
from numpy import nan
#This section downloads all the StackOverflow survey results.
user_agent = UserAgent()

for year in range(2013, 2023):
    try:
        headers={"User-Agent": user_agent.firefox}
        file_path = path.join(getcwd(), f"results_{year}.zip")
        
        if not path.exists(file_path) and not path.exists(path.join(getcwd(), str(year))):
            url = f"https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-{year}.zip"
            data = get(url, timeout=60, stream = True)
            with open(file_path, "wb") as f:
                for chunk in data.iter_content(chunk_size = 1024):
                    f.write(chunk)
        folder_path = path.join(getcwd(), str(year))
        mkdir(folder_path)
        with ZipFile(file_path, "r") as zip_file:
            zip_file.extractall(folder_path)
        if path.exists(path.join(folder_path, "__MACOSX")):
            rmtree(path.join(folder_path, "__MACOSX"))
        if path.exists(file_path):
            remove(file_path)
    except exceptions.RequestException as e:
        raise SystemExit(e)
    except IOError as e:
        pass

legacy_df_list = []
modern_df_list = []
for dir in listdir(getcwd()):
    if re.match(r"[0-9]{4}", dir):
        for root, dirs, files in walk(path.join(getcwd(), dir)):
            for file in files:
                legacy_save_path = path.join(getcwd(), "legacy.csv")
                if(file.endswith("Responses.csv") or file.endswith("Results.csv") or file.endswith("public.csv")):
                    try:
                        with open(path.join(root, file), "rb") as f:
                            encoding = chardet.detect(f.read())["encoding"]
                           
                            if int(dir) == 2011:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2012:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2013:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2014:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2015:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False, skiprows=1)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2016:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data = data.drop(["Unnamed: 0"], axis=1)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2017:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))       
                            if int(dir) == 2018:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2019:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))    
                            if int(dir) == 2020:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))       
                            if int(dir) == 2021:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))         
                            if int(dir) == 2022:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                data.to_csv(path_or_buf = path.join(getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                                rmtree(path.join(getcwd(), dir))        
                    except UnicodeDecodeError as e:
                        print(e)
data_list = []
save_path = path.join(getcwd(), "Data.csv")
try:
    for year in range(2013, 2023):
        
        def clean_2013_os(row):
            if "Windows" in str(row):
                return "Windows"
            elif "Mac" in str(row):
                return "MacOS"
            elif str(row) == "Response":
                return nan
            else: return row
    
        if year == 2013:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [0, 81]]
            data["Year"] = year
            data["OpSys"] = data.iloc[:, 1].apply(lambda row: clean_2013_os(row))
            data["Country"] = data.iloc[:, 0].values
            data["Languages"] = nan
            data["Databases"] = nan
            data["Gender"] = nan
            data = data.iloc[:, [*range(2, 6)]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
        
        
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
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [0, 67]]
            data["Year"] = year
            data["OpSys"] = data.iloc[:, 1].apply(lambda row: clean_2014_os(row))
            data["Country"] = data.iloc[:, 0].values
            data["Languages"] = nan
            data["Databases"] = nan
            data["Gender"] = nan
            data = data.iloc[:, [*range(2, 6)]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
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
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [0, 1, 2, 6, 7, *[col for col in range(8,51)]]]
            data["Year"] = year
            data["Languages"] = data.apply(lambda row: combine_languages(row), axis=1)
            data["OpSys"] = data["Desktop Operating System"].apply(lambda row: clean_2015_2016_os(row))
            data["Databases"] = nan
            data = data.iloc[:, [0, 2, 48,49, 50]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        if year == 2016:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [1, 6, 18, 31]]
            data["Year"] = year
            data["OpSys"] = data["desktop_os"].apply(lambda row: clean_2015_2016_os(row))
            data["Databases"] = nan
            data["Languages"] = data["programming_ability"]
            data["Gender"] = data["gender"]
            data = data.iloc[:, [0, 4, 5, 6, 7]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        def clean_2017_os(row):
            
            cleaned_list_of_os = []
            if "Windows" in str(row):
                cleaned_list_of_os.append("Windows")
            elif "MacOS" in str(row):
                cleaned_list_of_os.append("MacOS")
            elif "Linux" in str(row):
                cleaned_list_of_os.append("Linux")
            if cleaned_list_of_os:
                return ";".join(cleaned_list_of_os)
            else: return nan
                




        if year == 2017:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [3, 145,88, 94]]
            data["Year"] = year
            data["OpSys"] = data["HaveWorkedPlatform"].apply(lambda row: clean_2017_os(row))
            data["Languages"] = data["HaveWorkedLanguage"]
            data["Databases"] = nan
            data = data.iloc[:, [0, 1, 4, 5, 6]]
            data["Year"] = year
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
        
    
        def clean_2018_languages(row):
            languages = str(row)
            return languages.split(";")

    
        if year == 2018:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [3, 65,74,120]]
            data["Year"] = year
            data["Languages"] = data["LanguageWorkedWith"]
            data["OpSys"] = data["OperatingSystem"] 
            data["Databases"] = nan
            data = data.iloc[:, [0, 3, 4, 5, 6]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        if year == 2019:
            data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [6, 43, 54, 78]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
            data["Databases"] = nan
            data["Languages"] = data["LanguageWorkedWith"].values
            data = data.iloc[:, [0, 2, 3, 4, 5]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        if year == 2020:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [8, 17, 22, 41]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
            data["Databases"] = nan
            data["Languages"] = data["LanguageWorkedWith"].values
            data = data.iloc[:, [0, 1, 3, 4, 5]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        if year == 2021:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [3, 16, 18, 30, 39]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"].replace("Linux-based", "Linux")
            data["Databases"] = data["DatabaseHaveWorkedWith"].values
            data["Languages"] = data["LanguageHaveWorkedWith"].values
            data = data.iloc[:, [0, 3, 4, 5, 6]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))
            
        
        if year == 2022:
            data = None
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = path.join(getcwd(), str(year)+".csv"), low_memory=False)
            data = data.iloc[:, [15, 19,21, 33, 34, 50]]
            data["Year"] = year
            data["OpSysPersonal use"] = data["OpSysPersonal use"].str.split(";").explode(True).replace("Linux-based", "Linux").replace("macOS", "MacOS")
            data["OpSys"] = data["OpSysPersonal use"]
            data["Databases"] = data["DatabaseHaveWorkedWith"].values
            data["Languages"] = data["LanguageHaveWorkedWith"].values
           
            data = data.iloc[:, [0, *range(5,9)]]
            data_list.append(data)
            if path.exists(path.join(getcwd(), str(year)+".csv")):
                remove(path.join(getcwd(), str(year)+".csv"))

except FileNotFoundError as e:
    print(e)
except AttributeError as e:
    print(e)            
concat(data_list).to_csv(path_or_buf = save_path, index = False, mode = "w+")                   
            
    
            
            
   

        