#REDDIT SCRAPER
#PROGRAMMED BY: EDUARD NALDOZA, STEVE IBANEZ, MIGUEL VILLANUEVA

from collectHot import getHot
from collectTop import getTop
import os

#NOTE: Lines Tagged [OLD] is kept for when a custom chromedriver path is required.
#NOTE: Lines Tagged [DEBUG] are kept for debugging purposes.

#Declare/Init Variables
userInput = 0 #User input String
#[OLD] driverPath = ''

#Get chromedriver.exe from 'ChromeDriver' folder in directory
driverDir = os.getcwd() + '\\ChromeDriver'
print(driverDir)

#[OLD] Create ChromeDriverPath file if missing
#if (os.path.exists('ChromeDriverPath.txt') == False):
#    open('ChromeDriverPath.txt', mode='x')
#    with open('ChromeDriverPath.txt', 'w') as driverPathFile:
#        driverPathFile.writelines(['Enter chromedriver.exe Directory Folder','\n[NOTE: single backslash; same as Windows file explorer address bar,','\nLeave blank if ChromeDriver is in PATH environment variables]','\nEXAMPLE: C:\\Users\\admin\\Documents\\CPE32\\BIG DATA\\ChromeDriver','\n','\nEnter Below (7th line):','\nPATH'])

#[OLD] Obtain chromedriver.exe file directory from ChromeDriverPath.txt file
#with open('ChromeDriverPath.txt', 'r') as driverPathFile:
#    driverPath = driverPathFile.readlines()[6]

driverDir = driverDir.replace("\\", "\\\\")
driverDir += '\\\\chromedriver.exe'
#DEBUG print(driverDir)

#[OLD]
#if driverPath != 'PATH': #Replace '\' with '\\' and add '\'chromedriver.exe to directory
#    driverPath = driverPath.replace("\\", "\\\\")
#    driverPath += '\\\\chromedriver.exe'
#else:
#    driverPath = ''

#INTRODUCTORY MESSAGES
print("--Reddit Scraper--\nProgrammed by: E. Naldoza, S. Ibanez, M. Villanueva [CPE32]")
print("A Selenium Program designed to obtain data from your favourite subreddits. Refer to README.md for more information\n")

#[OLD]
#if driverDir == "": #Show chromedriver.exe directory
#    print("chromedriver path: empty (must be in PATH environment variables)")
#else:
#    print("chromedriver path: "+driverDir)

#USER PROMPTS
subredditName = input("\nEnter Subreddit Name: r/")

userInput = input('\n1. Scrape Top 20+ posts in Hot\n2. Scrape Top 20+ posts in Top\t')
userInput = int(userInput)
while(userInput != 1 and userInput != 2):
    print(type(userInput))
    print("\nTry again")
    userInput = input('1. Scrape posts in Hot\n2. Scrape posts in Top\n(Hint: Enter the number)\t')

#DEPENDING ON USER INPUT, EXECUTE getHot() OR getTop() FUNCTIONS
if (userInput == 1):
    getHot_Ouptut = getHot(subredditName, driverDir)
    while(getHot_Ouptut == 1):
        subredditName = input("\nr/" + subredditName + " does not exist re-enter subreddit name: r/")
        getHot_Ouptut = getHot(subredditName, driverDir)
    print("DONE")

elif (userInput == 2): #Prompt the user to choose the time range of top posts
    topOption = int(input('\n1. Top of Today\n2. Top of This Week\n3. Top of This Month\n4. Top of This Year\n5. Top of All Time\t'))
    #[DEBUG] print(topOption, type(topOption))

    if(topOption == 1):
        timeRange = "/?t=day"
    elif(topOption == 2):
        timeRange = "/?t=week"
    elif(topOption == 3):
        timeRange = "/?t=month"
    elif(topOption == 4):
        timeRange = "/?t=year"
    elif(topOption == 5):
        timeRange = "/?t=all"
    else:
        timeRange = "/?t=all"

    getTop_Ouptut = getTop(subredditName, timeRange, driverDir)
    while(getTop_Ouptut == 1):
        subredditName = input("\nr/" + subredditName + " does not exist re-enter subreddit name: r/")
        getTop_Ouptut = getTop(subredditName, timeRange, driverDir)
    print("DONE")