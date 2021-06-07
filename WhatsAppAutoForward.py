#Implementation of Selenium WebDriver with Python using PyTest
 
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import argparse
driver = webdriver.Chrome("chromedriver")
from time import time, sleep
driver.get("https://web.whatsapp.com")
 
# Initialize parser
parser = argparse.ArgumentParser(description='Message Forward arguments')
parser.add_argument('--source', dest='source', type=str, help='Name of the source from which copy the message')
parser.add_argument('--sourceIsGroup', dest='sourceIsGroup', type=bool,default=False, help='If the source is group or contact?')
parser.add_argument('--target', dest='target', type=str, help='Name of the target to which forward message')
parser.add_argument('--alert', dest='alert', type=bool,default=False, help='Set the alert if you want notification on laptop')

args = parser.parse_args()
print(args.source)
print(args.target)
print(args.alert)
 

input("Please scan QR code to login to whatsapp: ")
 

while True:
    sleep(1)
    sourceTitle='span[title="' + args.source + '"]'
    sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../div[2]/div[2]/div[2]/span[1]'
    if args.sourceIsGroup == False : 
        sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../../div[2]/div[2]/div[2]/span[1]'

    bulishGroup = driver.find_element_by_css_selector(sourceTitle) 
    unReadMessages=driver.find_element_by_xpath(sourceUnreasMessage)
    print(unReadMessages.get_attribute('innerHTML'))
    

    if len(unReadMessages.get_attribute('innerHTML')) > 0 :
        noOfMessageElement = unReadMessages.find_element_by_tag_name('span')
        if len(noOfMessageElement.get_attribute('innerHTML')) > 0 :
            print(noOfMessageElement.get_attribute('innerHTML'))
            noOfMessage = noOfMessageElement.text
            bulishGroup.click()

            groupTexts = driver.find_elements_by_xpath('//div[contains(@class, "message-in") and position()>(last()-'+noOfMessage+')]//span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span')
          
            messageList = [];
            for item in range(len(groupTexts)) :
                messageList.append(groupTexts[item].get_attribute('innerHTML'))
            
            humPanchGroup = driver.find_element_by_css_selector('span[title="' + args.target + '"]') 
            humPanchGroup.click()    
            testInput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        
            for message in messageList :
                print(message)
                testInput.send_keys(message);
                testInput.send_keys(Keys.RETURN);
            
                # message= groupTexts[item].find_element_by_xpath('')
                # print(message.text)

#
# while True:
#     
   
        
    

   





#todaysMessages= driver.find_element_by_xpath("//div[contains(@role,'region')]/div[contains(@class, 'focusable-list-item') and not(contains(@class, 'message-out')  or (@class='message-in'))]/following-sibling::div")
# driver.findElements(by.xpath("//*[text()='Today']/following::div[class='message-in']//span[class='selectable-text copyable-text']/span"))[1];

#print(unReadMessages.get_attribute('innerHTML'))



# sendButton = driver.find_element_by_css_selector('span[data-icon="send"]')

# sendButton.click()
