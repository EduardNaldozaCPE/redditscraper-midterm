def getAbout(subreddit_name, driverInstance):
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import csv
    import os
    import datetime

    #DECLARE/INIT VARIABLES
    csvBody = [['Subreddit Name','About','Subreddit User Count','Date of Creation']]
    rowData = []
    writeDate = str(datetime.datetime.now().year) +'-'+ str(datetime.datetime.now().month) +'-'+ str(datetime.datetime.now().day)
    #filename format: "About_<subreddit name>_<Date Written>.csv"
    fileName = 'About_'+subreddit_name+"_"+writeDate+'.csv'

    #CREATE CSV FILE
    if (os.path.exists(fileName) == False):
        open(fileName, mode='x')

    try:
        subredditName = driverInstance.find_element_by_xpath('//h1[@class="_2yYPPW47QxD4lFQTKpfpLQ"]').text
        about = driverInstance.find_element_by_xpath('//div[@class="_1zPvgKHteTOub9dKkvrOl4"]').text
        userCount = driverInstance.find_element_by_xpath('//div[@class="nEdqRRzLEN43xauwtgTmj"]/div').text
        dateofCreation = driverInstance.find_element_by_xpath('//div[@class="_2QZ7T4uAFMs_N83BZcN-Em"]').text

        #DEBUG print(title, about, userCount, dateofCreation)

        rowData = [subredditName,about,userCount,dateofCreation]
        #DEBUG print(rowData)
        csvBody.append(rowData)
    except:
        pass
        #print('ERROR APPENDING "ABOUT" DATA')

    #DEBUG print(csvBody)

    #Write data to csv file
    with open(fileName, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator = '\n')
        writer.writerows(csvBody)

    return 0