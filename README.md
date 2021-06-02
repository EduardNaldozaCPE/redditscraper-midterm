# RedditScraper
**Midterm Exam: Reddit**

*Project Lead: Eduard Naldoza*

*Programmers: Eduard Naldoza, Steve Ibanez, Miguel Villanueva*

A program that lets you scrape information on the top 20+ posts in the **Hot** or **Top** categories of your favourite subreddits. Columns included are:
 - Title
 - User
 - Post URL
 - Upvote Count
 - Time Since Posted

*and additionally, information about the subreddit:*
 - *Subreddit Name*
 - *About*
 - *Subreddit User Count*
 - *Date of Creation*

**Packages Used**
 - Selenium
 - PyInstaller
## Requirements

 - ChromeDriver
 - Python 3.9.0 or newer (optional)

## Installation
 To install, firstly download the zip file by clicking on the green *code* button and then the *Download Zip* option. Extract the zip file in any directory you wish. Make sure the chromedriver.exe file is accessible or that chromedriver.exe has an entry in the PATH environment variables.  

## Instructions
Before starting the program, make sure that your chromedriver.exe's directory is specified in the *ChromeDriverPath.txt* file.

To start the program, simply open *redditscraper.exe*

You will be prompted to enter the name of the subreddit you would like to collect data from
You can then choose to 
*1. Collect 20+ Posts from the Hot section* or  *2. Collect 20+ Posts from the Top section*

If you chose 1, the program will start collection data via ChromeDriver. 
If you chose 2, you will be able to choose which timeframe to collect from.

**After the program closes, you will find a .csv file containing the data, and another .csv file containing the information about the subreddit**

for option 1:

    filename format: Hot_<subreddit name>_<Date Written>.csv

for option 2:

    filename format: Top_<time range>_<subreddit name>_<Date Written>.csv

About file:

    filename format: About_<subreddit name>_<Date Written>.csv
