from collectAbout import getAbout


def getHot(subreddit_name, driverPath):
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import csv
    import os
    import datetime

    #DECLARE/INIT VARIABLES
    csvBody = [['Title','User','Post URL', 'Upvote Count', 'Time Since Posted']]
    rowData = []
    writeDate = str(datetime.datetime.now().year) +'-'+ str(datetime.datetime.now().month) +'-'+ str(datetime.datetime.now().day)
    #filename format: "Hot_<subreddit name>_<Date Written>.csv"
    fileName = 'Hot_'+subreddit_name+"_"+writeDate+'.csv'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(driverPath)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--Reddit Scraper--\nProgrammed by: E. Naldoza, S. Ibanez, M. Villanueva [CPE32]")
    print("A Selenium Program designed to obtain data from your favourite subreddits. Refer to README.md for more information\n")
    print("Please wait until the program closes...")

    driver.maximize_window()
    driver.get("https://www.reddit.com/")


    search_box = driver.find_element_by_class_name('_2xQx4j6lBnDGQ8QsRnJEJa')
    search_box.send_keys(subreddit_name)
    sleep(3)
    search_box.send_keys(Keys.ENTER)
    sleep(3)
    try: #Checks if any subreddits fit the name given by user, if no subreddit is found, return 1. If there is, proceed.
        sorry = driver.find_element_by_class_name('_1tEoY-vmgG3yWH6hCdgy3p').is_displayed()
        if(sorry):
            #DEBUG print("sorry")
            driver.close()
            driver.quit()
            return 1
    except:
        pass
        #DEBUG print("no sorry")
    
    subredditURL = driver.find_element_by_xpath('//div[@class="_2mO8vClBdPxiJ30y_C6od2"]/div[2]/div[1]/div[1]/a')
    print(subredditURL.get_attribute("href"))
    sleep(1)
    driver.get(str(subredditURL.get_attribute("href")))
    sleep(5)
    items = driver.find_elements_by_xpath('//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div')
    #DEBUG print(items)

    #CREATE CSV FILE
    if (os.path.exists(fileName) == False):
        open(fileName, mode='x')

    for item in items:
        try:
            title = item.find_element_by_xpath('.//h3[contains(@class, "_eYtD2XCVieq6emjKBH3m")]').get_attribute('innerHTML')
            username = item.find_element_by_xpath('.//a[@class="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE"]').get_attribute('innerHTML')
            postURL = item.find_element_by_xpath('.//a[@class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"]').get_attribute("href")
            upCount = item.find_element_by_xpath('.//div[@class="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"]').get_attribute('innerHTML')
            timeSince = item.find_element_by_xpath('.//a[@class="_3jOxDPIQ0KaOWpzvSQo-1s"]').get_attribute('innerHTML')

            #DEBUG print(title, username, postURL, upCount, timeSince)

            rowData = [title,username,postURL,upCount,timeSince]
            csvBody.append(rowData)
        except:
            pass
            #DEBUG print('error')

    if (getAbout(subreddit_name, driver)==0):
        driver.close()
        driver.quit()
    else:
        print('ERROR GETTING ABOUT FILE')

    #DEBUG print(csvBody)

    #Write data to csv file
    with open(fileName, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator = '\n')
        writer.writerows(csvBody)

    return 0