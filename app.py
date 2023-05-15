from zipfile import ZipFile
from pandas import DataFrame
from requests import get, exceptions
import matplotlib as plt

#This section downloads all the StackOverflow survey results.
url = "https://stackoverflow.com/survey/"
for year in range(2011, 2023):
    try:
        data = get(url+str(year), stream = True, timeout = 10)
        data.raise_for_status()
        with open(f"results_{year}.zip","wb" ) as f:
            for chunk in data.iter_content(chunk_size = 1024):
                f.write(chunk)
    except exceptions.RequestException as e:
        raise SystemExit(e)
   
    