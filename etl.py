
from time import time
import os
from shutil import rmtree
from zipfile import ZipFile
from pandas import DataFrame, Series, read_csv, concat, isna, to_numeric
from requests import get, exceptions
import matplotlib as plt
import re
import chardet
from numpy import nan
from fake_useragent import FakeUserAgent
import pycountry
#This section downloads all the StackOverflow survey results and extracts the Zip Archive.
ua = FakeUserAgent()
for year in range(2017, 2023):
    try:
        
        file_path = os.path.join(os.getcwd(), f"results_{year}.zip")
        
        if not os.path.exists(file_path) and not os.path.exists(os.path.join(os.getcwd(), str(year))):
            url = f"https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-{year}.zip"
            headers = {"User-Agent": ua.firefox}
            data = get(url, timeout=60, stream = True, headers=headers)
            with open(file_path, "wb") as f:
                for chunk in data.iter_content(chunk_size = 1024):
                    f.write(chunk)
        folder_path = os.path.join(os.getcwd(), str(year))
        os.mkdir(folder_path)
        with ZipFile(file_path, "r") as zip_file:
            zip_file.extractall(folder_path)
        if os.path.exists(os.path.join(folder_path, "__MACOSX")):
            rmtree(os.path.join(folder_path, "__MACOSX"))
        if os.path.exists(file_path):
            os.remove(file_path)
    except exceptions.RequestException as e:
        raise SystemExit(e)
    except IOError as e:
        pass

#This section determines the encoding standard used by each survey so that Pandas knows how to read it. Each survey is then saved using the UTF-8 standard.
encoding = None
for dir in os.listdir(os.getcwd()):
    if re.match(r"[0-9]{4}", dir):
        for root, dirs, files in os.walk(os.path.join(os.getcwd(), dir)):
            for file in files:
                if(file.endswith("Responses.csv") or file.endswith("Results.csv") or file.endswith("public.csv")):
                    try:
                        with open(os.path.join(root, file), "rb") as f:
                            encoding = chardet.detect(f.read())["encoding"]
                             
                        if int(dir) == 2017:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))       
                        if int(dir) == 2018:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))    
                        if int(dir) == 2019:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))    
                        if int(dir) == 2020:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))       
                        if int(dir) == 2021:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))         
                        if int(dir) == 2022:
                            data = read_csv(os.path.join(root, file), encoding = encoding, low_memory = False)
                            data.to_csv(path_or_buf = os.path.join(os.getcwd(), dir+".csv"), mode="w+", encoding="utf-8", index=False)
                            rmtree(os.path.join(os.getcwd(), dir))        
                    except UnicodeDecodeError as e:
                        print(e)
data_list = []
save_path = os.path.join(os.getcwd(), "Data.csv")
languages_path = os.path.join(os.getcwd(), "Languages.csv")
gender_path = os.path.join(os.getcwd(), "Gender.csv")
database_path = os.path.join(os.getcwd(), "Databases.csv")
country_path = os.path.join(os.getcwd(), "Country.csv")
opsys_path = os.path.join(os.getcwd(), "OpSys.csv")
try:
    for year in range(2017, 2023): 
        
        def clean_2017_os(row):
            cleaned_list_of_os = []
            if "Windows" in str(row):
                cleaned_list_of_os.append("Windows")
            if "Mac OS" in str(row):
                cleaned_list_of_os.append("MacOS")
            if "Linux" in str(row) or " Raspberry Pi" in str(row):
                cleaned_list_of_os.append("Linux")
            if cleaned_list_of_os:
                return ";".join(cleaned_list_of_os)
            else: return nan
        #Extracts and cleans the 2017 survey.
        if year == 2017:
            data = None
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["HaveWorkedPlatform", "HaveWorkedLanguage", "HaveWorkedDatabase", "Country", "Gender"]]
            data["Year"] = year
            data["OpSys"] = data["HaveWorkedPlatform"].apply(lambda row: clean_2017_os(row))
            data["Languages"] = data["HaveWorkedLanguage"]
            data["Databases"] = data["HaveWorkedDatabase"]
            data["Country"] = data["Country"]
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))
        
       
        #Extracts and cleans the 2018 survey.
        if year == 2018:
            data = None
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["LanguageWorkedWith", "OperatingSystem", "DatabaseWorkedWith", "Country", "Gender"]]
            data["Year"] = year
            data["Languages"] = data["LanguageWorkedWith"]
            data["OpSys"] = data["OperatingSystem"] 
            data["Databases"] = data["DatabaseWorkedWith"]
            data["Country"] = data["Country"]
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))
            
        #Extracts and cleans the 2019 survey.
        if year == 2019:
            data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["OpSys", "DatabaseWorkedWith", "LanguageWorkedWith", "Country", "Gender"]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"]
            data["Databases"] = data["DatabaseWorkedWith"]
            data["Languages"] = data["LanguageWorkedWith"]
            data["Country"] = data["Country"]
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))
            
        #Extracts and cleans the 2020 survey.
        if year == 2020:
            data = None
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["OpSys", "DatabaseWorkedWith", "LanguageWorkedWith", "Country", "Gender"]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"]
            data["Databases"] = data["DatabaseWorkedWith"]
            data["Languages"] = data["LanguageWorkedWith"]
            data["Country"] = data["Country"]
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))
            
        #Extracts and cleans the 2021 survey.
        if year == 2021:
            data = None
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["OpSys", "DatabaseHaveWorkedWith", "LanguageHaveWorkedWith", "Country", "Gender"]]
            data["Year"] = year
            data["OpSys"] = data["OpSys"]
            data["Databases"] = data["DatabaseHaveWorkedWith"]
            data["Languages"] = data["LanguageHaveWorkedWith"]
            data["Country"] = data["Country"].values
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))
            
        #Extracts and cleans the 2022 survey.
        if year == 2022:
            data = None
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                data = read_csv(filepath_or_buffer = os.path.join(os.getcwd(), str(year)+".csv"), low_memory=False)
            data = data.loc[:, ["OpSysProfessional use", "DatabaseHaveWorkedWith", "LanguageHaveWorkedWith", "Country", "Gender"]]
            data["Year"] = year
            data["OpSys"] = data["OpSysProfessional use"]
            data["Databases"] = data["DatabaseHaveWorkedWith"]
            data["Languages"] = data["LanguageHaveWorkedWith"]
            data["Country"] = data["Country"]
            data = data.loc[:, ["Year", "OpSys", "Country", "Languages", "Databases", "Gender"]]
            data_list.append(data)
            if os.path.exists(os.path.join(os.getcwd(), str(year)+".csv")):
                os.remove(os.path.join(os.getcwd(), str(year)+".csv"))

except FileNotFoundError as e:
    print(e)
except AttributeError as e:
    print(e)            

#This function attempts to ensure the naming convention for all countries is consistent throughout the surveys.
def standardized_country_name(row):
    try:
        country = pycountry.countries.lookup(str(row)) 
        return str(country.name)
    except LookupError as e:
        return row
    except AttributeError as e:
        return row
#Each survey is combined into one dataset.
data = concat(data_list)
data["Country"] = data["Country"].apply(lambda row: standardized_country_name(row))
#Replaces all occurrences of "Man" with "Male," "Woman" with "Female," and and anything not conforming to binary gender identification to "LGBTQ." Any constructive or prefer not to say responses were replaced with "Other." Any trailing whitespace is removed.
data["Gender"] = data["Gender"].str.replace("Man", "Male").str.replace("Woman", "Female").str.replace("Transgender", "LGBTQ").str.replace("Non-binary, genderqueer, or gender non-conforming", "LGBTQ").str.replace("Gender non-conforming","LGBTQ").str.replace("Prefer not to say", "Other").str.replace("Prefer not to disclose", "Other").str.replace("Or, in your own words:", "Other").str.strip()
#Uses Regular Expresses to standardize and clean the Operating System naming conventions.
data["OpSys"] = data["OpSys"].str.replace(r"BSD\/Unix|BSD", "BSD/UNIX", regex=True).str.replace(r"Linux-[A-Za-z]{1,}", "Linux", regex=True).str.replace(r"Other \(please specify\):", "Other", regex=True).str.replace("macOS", "MacOS")
#Replaces all field delimiters with a tab space.
data["Gender"] = data["Gender"].str.replace(";", "\t")
data["Languages"] = data["Languages"].str.replace(";", "\t")
data["Databases"] = data["Databases"].str.replace(";", "\t")
data["Gender"] = data["Gender"].str.replace(";", "\t")
data["OpSys"] = data["OpSys"].str.replace(";", "\t")
#This section fills missing values; separates all values in each field with the tab delimiter; uses apply to convert the field's value, which is now a list of values, to a set of values which ensures there are no duplicates; converts the set back to a list, and recombines each item in the list using the tab separator. 
data["Gender"] = data["Gender"].fillna(str(nan)).str.split("\t").apply(set).apply(list).apply("\t".join)
data["Languages"] = data["Languages"].fillna(str(nan)).str.split("\t").apply(set).apply(list).apply("\t".join)
data["Databases"] = data["Databases"].fillna(str(nan)).str.split("\t").apply(set).apply(list).apply("\t".join)
data["OpSys"] = data["OpSys"].fillna(str(nan)).str.split("\t").apply(set).apply(list).apply("\t".join)
data.to_csv(path_or_buf = save_path, index = False, mode = "w+")  
#This section uses a for loop to iterate through each field that contains a tab delimiter; converts the field to a list; takes each individual value and places it in its own row; removes any trailing whitespaces; determines the number of occurrences for each value; and saves the first 10 values in the resulting pivot table to a file. The original data being re-read during each iteration to ensure the previous transformation doesn't influence the next field's pivot table. 
cols = ["Languages", "Databases", "Country", "Gender", "OpSys"]
paths = [languages_path, database_path, country_path, gender_path, opsys_path]

for col, path in zip(cols, paths):
    if os.path.exists(path):
        os.remove(path)
    temp_df = data
    temp_df[col] = data[col].str.split("\t")
    exploded_df = temp_df.explode(col)
    exploded_df[col] = exploded_df[col].str.strip()
    exploded_df = exploded_df[exploded_df[col] != "nan"]
    for year in range(2017, 2023):
        if not os.path.exists(path):
            exploded_df[exploded_df["Year"]==year].groupby("Year")[col].value_counts().head(10).to_csv(path, mode="w", header = True, index = True)
        else:
            exploded_df[exploded_df["Year"]==year].groupby("Year")[col].value_counts().head(10).to_csv(path, mode="a", header = False, index = True)

            
   

        