from time import time
from os import getcwd, path, remove, mkdir, listdir, walk
from shutil import rmtree
from zipfile import ZipFile
from pandas import DataFrame, read_csv, concat
from requests import get, exceptions
import matplotlib as plt
import re
import chardet
from fake_useragent import UserAgent
#This section downloads all the StackOverflow survey results.
user_agent = UserAgent()



for year in range(2011, 2023):
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
                            encoding = chardet.detect(f.readline())["encoding"]
                           
                            if int(dir) == 2011:
                                data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                print(dir)
                            if int(dir) == 2012:
                                #data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                print(dir)    
                            if int(dir) == 2013:
                                #data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                print(dir)
                            if int(dir) == 2014:
                                #data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                print(dir)
                            if int(dir) == 2015:
                                #data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                                print(dir)
                                
                        if int(dir) == 2016:
                            data = read_csv(path.join(root, file), encoding=encoding, low_memory = False)
                            data.insert(0, "id", data["Unnamed: 0"].values)
                            data = data.drop(["Unnamed: 0"], axis=1)
                               
                    except UnicodeDecodeError as e:
                        pass
                    #data = concat(temp_df_list)
                    #data.to_csv(path_or_buf = save_path, encoding = "utf-8")
                    #data.insert(0, column="Survey_year,", value=[int(dir) for _ in range(len(data))])
            
    
            
            
   

        