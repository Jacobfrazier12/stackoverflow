# Overview  

- This is a project that downloads and extracts every StackOverflow Developer survey from 2017-2022. To view the results, please see the following dashboard: [Insights Dashboard](https://public.tableau.com/app/profile/jacob5151/viz/StackOverflowDeveloperSurveyResults2017-2022/StackOverflowDashboard)

- I've been wondering what the most popular tools are that respondents use. I was also curious about the gender makeup of survey respondents and where they live. I already had preconceived answers that were right, but I wanted quantifiable data that backed up my answers. The StackOverflow Annual Developer survey provided data that I was able to use. 

# License

**You are free to distribute, copy, or modify this software, with or without credit towards the author; however, the author bares no responsibility for any damages sustained while using this software. Also, the software is offered "as is."**

# Approach 
- I wanted to fully automate the retrieval, extraction, cleaning, and loading processes. I discovered that each CSV file could be retrieved with a URL with the year appended to it; which downloaded a Zip Archive, which itself contained the survey results. 

- After extracting the survey results, I began working on combining the data from each survey. This proved difficult because the surveys have evolved over the years. Some CSV files required more cleaning and transformation than others.

1. My first challenge was actually reading the CSV files. Not all files were encoded with UTF-8, so I had to determine which encoding standard each file was using. After that, I then encoded the data using UTF-8 and saved it to a new CSV file which was titled {year}.csv, with "year" being the year the survey was conducted.

2. My second challenge was analyzing each survey to prepare my strategy for cleaning and transforming the data. Over the years, StackOverflow has been refining the survey.





# Running the software
1. Ensure you have Python 3, Pip 3, and GNU Make installed.

2. Run `make init` && `make run`

- `make init` will install dependencies and `make run` will run the ETL script.


# Results at a glance
- The most popular Language year-over-year is JavaScript.

- The most popular database software year-over-year is MySQL

- The country with the most respondents year-over-year is the United States.

- Majority of respondents are male.

- Majority of respondents use Windows or various forms of Linux, including Windows Subsystems for Linux(WSL) 

