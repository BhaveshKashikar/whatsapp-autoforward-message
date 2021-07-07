#Implementation of Selenium WebDriver with Python using PyTest
# coding=utf8
import re
clean = re.compile('<.*?>') 
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import argparse
driver = webdriver.Chrome("chromedriver")
from time import time, sleep
driver.get("https://web.whatsapp.com")
from bs4 import BeautifulSoup

 
# Initialize parser
parser = argparse.ArgumentParser(description='Message Forward arguments')
parser.add_argument('--source', dest='source', type=str, help='Name of the source from which copy the message')
parser.add_argument('--sourceIsGroup', dest='sourceIsGroup', type=bool,default=False, help='If the source is group or contact?')
parser.add_argument('--target', dest='target', type=str, help='Name of the target to which forward message')
parser.add_argument('--alert', dest='alert', type=bool,default=False, help='Set the alert if you want notification on laptop')

args = parser.parse_args()
print(args.source)
#print(args.target)
print(args.alert)
print(args.sourceIsGroup)

input("Please scan QR code to login to whatsapp: ") 

while True:
    sleep(1)
    sourceTitle='span[title="' + args.source + '"]'
    sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../div[2]/div[2]/div[2]/span[1]'
    if args.sourceIsGroup == False: 
        sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../../div[2]/div[2]/div[2]/span[1]'

    print(sourceUnreasMessage)
    bulishGroup = driver.find_elements_by_css_selector(sourceTitle)
    if (len(bulishGroup)>0) :
        unReadMessages=driver.find_element_by_xpath(sourceUnreasMessage)
        print(unReadMessages.get_attribute('innerHTML'))
        
        if len(unReadMessages.get_attribute('innerHTML')) > 0 :
            noOfMessageElement = unReadMessages.find_element_by_tag_name('span')
            if len(noOfMessageElement.get_attribute('innerHTML')) > 0 :
                print(noOfMessageElement.get_attribute('innerHTML'))
                noOfMessage = noOfMessageElement.text
                bulishGroup[0].click()

                groupTexts = driver.find_elements_by_xpath('//div[contains(@class,"message-in") and contains(@class,"focusable-list-item") and position() >= (last()-'+noOfMessage+')]//div[contains(@class,"copyable-text")]')

                #driver.find_elements_by_xpath('//div[contains(@class, "message-in") and position()>(last()-'+noOfMessage+')]//span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span')
            
                messageList = [];
                for item in range(len(groupTexts)) :
                    finalMessage="*BULLISH* : <br />";
                    replyText="";
                    messageText="";
                    replyItem = groupTexts[item].find_elements_by_xpath('.//span[contains(@class,"quoted-mention")]')
                    if len(replyItem)>0:
                        innerHtml = replyItem[0].get_attribute('innerHTML')
                        soup = BeautifulSoup(innerHtml, 'html.parser')
                        listOfImages=soup.find_all('img')
                        for i in range(len(listOfImages)) :
                            listOfImages[i].replace_with(listOfImages[i]["alt"])
                        replyText ="*REPLY OF* : " + re.sub(clean, '', str(soup)) +" <br />" +"*MESSAGE* :  " ;
                    messageIn = groupTexts[item].find_elements_by_xpath('.//span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span')
                    if len(messageIn)>0:
                        innerHtml = messageIn[0].get_attribute('innerHTML')
                        soup = BeautifulSoup(innerHtml, 'html.parser')
                        listOfImages=soup.find_all('img')
                        for i in range(len(listOfImages)) :
                            listOfImages[i].replace_with(listOfImages[i]["alt"])
                        messageText = re.sub(clean, '', str(soup)) +" <br />"
                    finalMessage +=replyText + messageText
                    messageList.append(finalMessage)
                
                humPanchGroup = driver.find_element_by_css_selector('span[title="' + args.target + '"]') 
                humPanchGroup.click()    
                testInput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
            
                for message in messageList :
                    print(message)
                    driver.execute_script("arguments[0].innerHTML = '{}'".format(message),testInput)
                    testInput.send_keys('.')
                    testInput.send_keys(Keys.BACKSPACE)
                    testInput.send_keys(Keys.RETURN);                    
    else :
        print("No element Found for the Source")
#🖐️
# run below command to create exe file
# pyinstaller --onefile pythonScriptName.py