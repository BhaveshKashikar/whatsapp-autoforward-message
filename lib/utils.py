# coding=utf8
from logging import debug
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import re
clean = re.compile('<.*?>') 

def sendMessages(driver,messageList):
    testInput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
    for messageObject in messageList :
        print(messageObject)
        driver.execute_script("arguments[0].innerHTML = '{}'".format(messageObject['message']),testInput)
        testInput.send_keys('.')
        testInput.send_keys(Keys.BACKSPACE)
        testInput.send_keys(Keys.RETURN); 
        messageObject["isSent"] = True;

def readIncomingMessage(groupText, xPath, preFix):
    messageText = "";
    messageIn = groupText.find_elements_by_xpath(xPath)
    if len(messageIn)>0:
        innerHtml = messageIn[0].get_attribute('innerHTML')
        debug("Message In has been found {}", innerHtml)
        soup = replaceImgTagWithAlt(innerHtml)
        messageText = preFix + re.sub(clean, '', str(soup)) +" <br />"
    return messageText

def replaceImgTagWithAlt(innerHtml):
    soup = BeautifulSoup(innerHtml, 'html.parser')
    listOfImages = soup.find_all('img')
    for i in range(len(listOfImages)) :
        listOfImages[i].replace_with(listOfImages[i]["alt"])
    return soup