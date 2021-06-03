# RedditScraper
**Midterm Exam: Reddit**

*Project Lead: Eduard Naldoza*

*Programmers: Eduard Naldoza, Steve Ibanez, Miguel Villanueva*

A program that lets you scrape information on the top 20+ posts in the **Hot** or **Top** categories of your favourite subreddits. Columns included are:
 - Title - Title of the subreddit post
 - User - u/username of user who posted
 - Post URL - URL of the specific post
 - Upvote Count - Number of upvotes minus downvotes. if in thousands, expressed as *X.X*k; in millions, *X.X*m
 - Time Since Posted - expressed as X hours/days/months/years ago

*and additionally, information about the subreddit:*
 - *Subreddit Name* - Title/Header of subreddit
 - *About* - Description of the subreddit
 - *Subreddit User Count* - Number of users currently in/following subreddit
 - *Date of Creation* - expressed as "Created *Month* *Day*, *Year*"

**Packages Used**
 - Selenium
 - PyInstaller

## Requirements
*(to run code from .py file)*
 - ChromeDriver
 - Python 3.9.0 or newer

## Installation
 To install, firstly download the zip file by clicking on the green *code* button and then the *Download Zip* option. Extract the zip file in any directory you wish. 
 Make sure the chromedriver.exe file is in the ChromeDriver folder located on the same directory as redditscraper.exe as shown below.
 ![ChromeDriver Directory](https://raw.githubusercontent.com//EduardNaldozaCPE/redditscraper-midterm/main/README_Images/chromedriverdir.png)

## Instructions
Before starting the program, make sure that your chromedriver.exe's directory is specified in the *ChromeDriverPath.txt* file.

To start the program, simply open *redditscraper.exe*

![Opening Screen](https://raw.githubusercontent.com//EduardNaldozaCPE/redditscraper-midterm/main/README_Images/subredditname.png?raw=true)

You will be prompted to enter the name of the subreddit you would like to collect data from
You can then choose to 

*1. Collect 20+ Posts from the Hot section* or  *2. Collect 20+ Posts from the Top section*

![Options](https://raw.githubusercontent.com//EduardNaldozaCPE/redditscraper-midterm/tree/main/README_Images/options.png?raw=true)

If you chose 1, the program will start collection data via ChromeDriver. 
If you chose 2, you will be able to choose which timeframe to collect from.

**After the program closes, you will find a .csv file containing the data, and another .csv file containing the information about the subreddit**

![CSV Files](https://raw.githubusercontent.com//EduardNaldozaCPE/redditscraper-midterm/main/README_Images/outputs.png?raw=true)

The file naming scheme is as follows:
for option 1:

    filename format: Hot_<subreddit name>_<Date Written>.csv

for option 2:

    filename format: Top_<time range>_<subreddit name>_<Date Written>.csv

About file:

    filename format: About_<subreddit name>_<Date Written>.csv
