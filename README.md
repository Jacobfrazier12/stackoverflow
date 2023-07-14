# Overview  

- This is a project that downloads and extracts every StackOverflow Developer surveys, excluding 2023 because a CSV file is unavailable with that data. To view the results, please see the following dashboard: [Insights Dashboard](https://public.tableau.com/app/profile/jacob5151/viz/StackOverflow_16887813382030/StackoverflowData)

- I've been wondering what the most popular tools are that respondents use. I was also curious about the gender makeup of survey respondents and where they live. I already had preconceived answers that were right, but I wanted quantifiable data that backed up my answers. The StackOverflow Annual Developer survey provided data that I was able to use. 

# License

**You are free to distribute, copy, or modify this software, with or without credit towards the author; however, the author bares no responsibility for any damages sustained while using this software. Also, the software is offered "as-is."**

# Approach 
- I wanted to fully automate the retrieval, extraction, cleaning, and loading processes. I discovered that each CSV file could be retrieved with a URL with the year appended to it; which downloaded a Zip Archive, which itself contained the survey results. 

- After extracting the survey results, I began working on combining the data from each survey. This proved difficult because the surveys have evolved over the years. Some CSV files required more cleaning and transformation than others.

1. My first challenge was actually reading the CSV file. Not all files were encoded with UTF-8, so I had to determine which encoding standard each file was using. After that, I then encoded the data using UTF-8 and saved the data into a new CSV file which was titled {year}.csv, with "year" being the year the survey was conducted.

2. My second challenge was analyzing each survey to prepare my strategy for cleaning and transforming the data. Over the years, StackOverflow has been refining the survey. The early years of the survey 





# Running the software
1. Ensure you have Python 3, Pip 3, and GNU Make installed.

2. Run `make init` && `make run`

- `make init` will install all required dependencies, via Pip; clone the Sparkov tool; and download the Kaggle dataset from Google Drive.

- `make run` will generate roughly half-a-gigabyte of data and train each model on said data. After each model is trained, it is tested against the second dataset. Two tests are performed: one against all non-fraudulent transactions and all fraudulent.

# Results at a glance

The results varied because the training data was randomly generated. Because of this, if you run this, you likely won't achieve the same results.


1. Model: Multinomial Naive Bayes
   all non-fraudulent: 91%
   all fraudulent: 57%

2. Model: K-nearest Neighbors 
   all non-fraudulent: 74%
   all fraudulent: 64%

3. Model: Random Forest 
   all non-fraudulent: 95%
   all fraudulent: 54%

4. Model: Logistic Regression 
   all non-fraudulent: 89%
   all fraudulent: 69%

5. Model: Logistic Regression CV 
   all non-fraudulent: 95%
   all fraudulent: 74%

6. Model: Neural Network
   all non-fraudulent: 94%
   all fraudulent: 66%