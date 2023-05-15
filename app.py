from time import time
from os import getcwd, path
from zipfile import ZipFile
from pandas import DataFrame
from requests import get, exceptions
import matplotlib as plt

#This section downloads all the StackOverflow survey results.



for year in range(2011, 2023):
    try:
        url = f"https://stackoverflow.com/survey/{year}"
        file_path = path.join(getcwd(), f"results_{year}.zip")
        if not path.exists(file_path):
            data = get(url, timeout=60)
            data.raise_for_status()
            with open(file_path,"wb" ) as f:
                for data in data.content:
                    f.write(data)
            time.sleep(10)
        
    except exceptions.RequestException as e:
        raise SystemExit(e)
   
    