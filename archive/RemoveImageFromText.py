# coding=utf8
from base64 import encode
import re
clean = re.compile('<.*?>')
text = '<div class="xkqQM copyable-text" data-pre-plain-text="[2:10 PM, 6/8/2021] Mehul Patel: "><div class="_3lWN8"><div class="_2w_1z"><div class="_3Ppzm" role="button"><span class="bg-color-1 _3eu_9"></span><div class="_2mGGI"><div class="_3Xmdf"><div class="_26iqs color-1" role="button"><span dir="auto" class="_1Lc2C _3-8er">Mehul Patel</span></div><div class="_31DtU" dir="ltr" role="button"><span dir="auto" class="quoted-mention _3-8er">3 DAYS CALL : Buy.....HFCL @ CMP.........TARGET...........55-56 SL....48.30.</span></div></div></div></div></div></div><div class="_3ExzF"><span dir="ltr" class="_3-8er selectable-text copyable-text"><span>Sitting NEAR DAYS High......WILL Trigger HUGE Buying AGAIN , Once this Cross.....TODAYS Days HIGH....JAI HO.</span></span><span class="_1Bd9o"></span></div></div>'
print( re.sub(clean, '', text))

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# #set chromodriver.exe path
# driver = webdriver.Chrome("chromedriver")
# driver.implicitly_wait(0.5)
# #launch URL
# driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
# #object of ActionChains
# a = ActionChains(driver)
# #identify element
# m = driver.find_element_by_link_text("Enabled")
# #hover over element
# a.move_to_element(m).perform()
# #identify sub menu element
# n = driver.find_element_by_link_text("Back to JQuery UI")
# # hover over element and click
# a.move_to_element(n).click().perform()
# print("Page title: " + driver.title)
# #close browser
# driver.close()

#Implementation of Selenium WebDriver with Python using PyTest
 
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

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
print(args.sourceIsGroup)

input("Please scan QR code to login to whatsapp: ")

text='<div class="_3ExzF"><span dir="ltr" class="_3-8er selectable-text copyable-text"><span>This is with emogi<img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🐱" draggable="false" class="b35 emoji wa _3-8er selectable-text copyable-text" data-plain-text="🐱" style="background-position: -40px -20px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🐱" draggable="false" class="b35 emoji wa _3-8er selectable-text copyable-text" data-plain-text="🐱" style="background-position: -40px -20px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🐱" draggable="false" class="b35 emoji wa _3-8er selectable-text copyable-text" data-plain-text="🐱" style="background-position: -40px -20px;"></span></span><span class="_1Bd9o"></span></div>'
soup = BeautifulSoup(text, 'html.parser') 

listOfImages=soup.find_all('img')
emogiList = [];
for i in range(len(listOfImages)) :
    #print (listOfImages[i])
    #print(listOfImages[i]["alt"])
    #print(str(listOfImages[i]))
    #newTag = soup.new_tag("data")
    #newTag.string=listOfImages[i]["alt"]
    #emogiList.append(listOfImages[i]["alt"])
    listOfImages[i].replace_with(listOfImages[i]["alt"])
    #text = text.replace(str(listOfImages[i]),"tes")

msg = re.sub(clean, '', str(soup))
print(msg)
#for i in range(len(emogiList)) :
    #msg = msg.replace("#emogi-"+str(i),emogiList[i])

print(msg)


# #while True:
# sleep(1)
sourceTitle='span[title="' + args.source + '"]'
sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../div[2]/div[2]/div[2]/span[1]'
if args.sourceIsGroup == False: 
    sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../../div[2]/div[2]/div[2]/span[1]'
print(sourceUnreasMessage)
bulishGroup = driver.find_element_by_css_selector(sourceTitle) 
unReadMessages=driver.find_element_by_xpath(sourceUnreasMessage)
print(unReadMessages.get_attribute('innerHTML'))
bulishGroup.click()
testInput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")

# ActionChains(driver).send_keys(args.target).perform()
driver.execute_script("arguments[0].innerHTML = '{}'".format(msg),testInput)
testInput.send_keys('.')
testInput.send_keys(Keys.BACKSPACE)
# testInput.send_keys();        
             
input("Please wait: ")

WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id("main"))
# hoverItem = driver.find_elements_by_xpath('//div[contains(@class,"message-in") and contains(@class,"focusable-list-item") and position() >= (last()-5)]//div[contains(@class,"copyable-text")]')

# print(range(len(hoverItem)))
# if len(hoverItem)>0 :
#     for item in range(len(hoverItem)) :
     
#         finalMessage="⏩ : \n";
#         replyText="";
#         messageText="";
#         replyItem = hoverItem[item].find_elements_by_xpath('.//span[contains(@class,"quoted-mention")]')
       
#         if len(replyItem)>0:
#             replyText =" *REPLY OF* : " + re.sub(clean, '', replyItem[0].get_attribute('innerHTML')) +" \n" +" *MESSAGE* :  " ;
#         messageIn = hoverItem[item].find_elements_by_xpath('.//span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span')
#         if len(messageIn)>0:
#             messageText = re.sub(clean, '', messageIn[0].get_attribute('innerHTML')) +" \n"
#         finalMessage +=replyText + messageText
#         print(finalMessage)

    


    #object of ActionChains
    # hoverAction = ActionChains(driver)

    # print( re.sub(clean, '', hoverItem.get_attribute('innerHTML')))
    # #identify element
    # hoverAction.move_to_element(hoverItem).perform()

    # if len(unReadMessages.get_attribute('innerHTML')) > 0 :
    #     noOfMessageElement = unReadMessages.find_element_by_tag_name('span')
    #     if len(noOfMessageElement.get_attribute('innerHTML')) > 0 :
    #         print(noOfMessageElement.get_attribute('innerHTML'))
    #         noOfMessage = noOfMessageElement.text
    #         bulishGroup.click()

    #         hoverItem = driver.find_element_by_xpath('//div[contains(@class,message-in) and contains(@class,focusable-list-item) and position() = last()]/div')
    #         #object of ActionChains
    #         hoverAction = ActionChains(driver)
    #         #identify element
    #         hoverAction.move_to_element(hoverItem).perform()
            # groupTexts = driver.find_elements_by_xpath('//div[contains(@class, "message-in") and position()>(last()-'+noOfMessage+')]//span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span')
          
            # messageList = [];
            # for item in range(len(groupTexts)) :
            #     messageList.append(groupTexts[item].get_attribute('innerHTML'))
            
            # humPanchGroup = driver.find_element_by_css_selector('span[title="' + args.target + '"]') 
            # humPanchGroup.click()    
            # testInput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        
            # for message in messageList :
            #     print(message)
            #     testInput.send_keys(message);
            #     testInput.send_keys(Keys.RETURN);
            
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
