# Implementation of Selenium WebDriver with Python using PyTest
# coding=utf8
import json
from selenium.webdriver.support.wait import WebDriverWait
from lib.utils import readIncomingMessage, sendMessages
from logging import debug, info
import re
from datetime import datetime

clean = re.compile("<.*?>")
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
parser = argparse.ArgumentParser(description="Message Forward arguments")
parser.add_argument(
    "--source",
    dest="source",
    type=str,
    help="Name of the source from which copy the message",
)
parser.add_argument(
    "--sourceIsGroup",
    dest="sourceIsGroup",
    type=bool,
    default=False,
    help="If the source is group or contact?",
)
parser.add_argument(
    "--target",
    dest="target",
    type=str,
    help="Name of the target to which forward message",
)
parser.add_argument(
    "--prefix",
    dest="prefix",
    type=str,
    default="Bullish",
    help="Set the prefix to set text before forwarding message",
)
parser.add_argument(
    "--alert",
    dest="alert",
    type=bool,
    default=False,
    help="Set the alert if you want notification on laptop",
)

args = parser.parse_args()
info("Source : " + str(args.source))
info("Target : " + args.target)
info("Source Is Group : {}", args.sourceIsGroup)
info("Message Prefix : " + str(args.prefix))
info(args.alert)

messageList = []
lastId = ""

input("Please scan QR code to login to whatsapp: ")

# Running the loop to check message on every second.
while True:
    sleep(1)
    try:
        now = datetime.now()

        current_time = datetime.now().strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        # Reading source title tag from the DOM
        sourceTitle = 'span[title="' + args.source + '"]'
        # Reading source un read message tag from the DOM
        # sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../div[2]/div[2]/div[2]/span[1]'

        # # If the source is individual contact then unread message tag xPath is different than the group
        # if args.sourceIsGroup == False:
        #     sourceUnreasMessage ='//span[contains(@title,"' + args.source + '")]/../../../../../div[2]/div[2]/div[2]/span[1]'

        # debug(sourceUnreasMessage)

        # Find the source group selector using css Selector
        sourceGroupSelector = driver.find_elements_by_css_selector(sourceTitle)
        if len(sourceGroupSelector) > 0:
            debug("Source Group selector found ")
            print(len(sourceGroupSelector))

            # Now open the web page for the source group chat where we found n number of messages
            sourceGroupSelector[0].click()

            WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id("main"))

            # Find last x number of messages based on the noOfMessage variable.
            if len(lastId) > 0:

                groupTexts = driver.find_elements_by_xpath(
                    '//div[contains(@class,"message-in") and contains(@class,"focusable-list-item") and @data-id="'
                    + lastId
                    + '"]/following-sibling::div[contains(@class,"message-in") and contains(@class,"focusable-list-item")]'
                )
                for item in range(len(groupTexts)):
                    dataId = groupTexts[item].get_attribute("data-id")
                    if len(lastId) > 0:
                        print("108 : " + dataId)

                        finalMessage = "*" + args.prefix + "* : <br />"
                        replyText = ""
                        replyText = readIncomingMessage(
                            groupTexts[item],
                            './/span[contains(@class,"quoted-mention")]',
                            "*REPLY OF* : ",
                        )
                        messageText = ""
                        messageText = readIncomingMessage(
                            groupTexts[item],
                            './/span[contains(@class, "selectable-text") and contains(@class,"copyable-text")]/span',
                            " <br />" + "*MESSAGE* :  ",
                        )

                        finalMessage += replyText + messageText
                        messageList.append(
                            {"dataId": dataId, "message": finalMessage, "isSent": False}
                        )

                    lastId = dataId
                print("125")
                # print(messageList)
                # messageList = list(filter(lambda x: x['isSent'] == False, messageList))
                # json.dumps(messageList)
                targetGroupSelector = driver.find_elements_by_css_selector(
                    'span[title="' + args.target + '"]'
                )
                if len(targetGroupSelector) > 0 and len(messageList) > 0:
                    targetGroupSelector[0].click()
                    WebDriverWait(driver, 10).until(
                        lambda d: d.find_element_by_id("main")
                    )
                    print("135")
                    # print(messageList)
                    sendMessages(driver, messageList)
                    messageList = []
            else:
                groupTexts = driver.find_elements_by_xpath(
                    '//div[contains(@class,"message-in") and contains(@class,"focusable-list-item")]'
                )
                if (len(groupTexts)) > 0:
                    lastId = groupTexts[0].get_attribute("data-id")
            # //div[contains(@class,"copyable-text")]
            print("144" + lastId)

        else:
            print("No element Found for the Source")
            driver.refresh()
            # print("Refresh Time =", datetime.now().strftime("%H:%M:%S"))
            # WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id("pane-side"))
            sleep(10)

    except Exception as e:
        print(e)
        print("No element Found for the Source")
        driver.refresh()
        sleep(10)
# 🖐️
# run below command to create exe file
# pyinstaller --onefile pythonScriptName.py
