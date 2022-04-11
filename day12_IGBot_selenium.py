##!/usr/bin/env python
#day12 use selenium to create a IGBot

import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
driver = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe')

def login(username, password):
    driver.get('https://www.instagram.com/')

    # accepting the cookies
    try:
        cookies_accept = driver.find_element_by_xpath('//button[text()="Accept"]')
        cookies_accept.click()
        time.sleep(2)
    except:
        pass

    time.sleep(2)
    Username = driver.find_element_by_name('username')
    Password = driver.find_element_by_name('password')

    Username.click()
    Username.send_keys(username)
    time.sleep(1)
    Password.click()
    Password.send_keys(password)
    time.sleep(1)

    log_in = driver.find_element_by_xpath('//div[text()="登入"]')
    log_in.click()
    time.sleep(5)

    # credential storage
    try:
        credentials = driver.find_element_by_xpath('//button[text()="稍後再說"]')
        credentials.click()
        time.sleep(3)
    except:
        pass

    # notification
    try:
        notification = driver.find_element_by_xpath('//button[text()="稍後再說"]')
        notification.click()
        time.sleep(3)
    except:
        pass

def presslike():
    time.sleep(3)
    pic = driver.find_element_by_class_name('_9AhH0')
    pic.click()

    for i in range(0,3):
        #if i % 10 == 1:
        #    time.sleep(random.randint(5,20))

        # check Like button
        if len(driver.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(driver.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
            print('按過了')
            scroll = 'window.scrollBy(0,500)'
            driver.execute_script(scroll)
            time.sleep(1)
        else:
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//*[@aria-label="讚"]').click()
            except:
                try:
                    driver.find_elements_by_xpath('//*[@aria-label="讚"]')[1].click()
                except:
                    print('圖片沒跑出來，直接下一頁')
        #driver.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
        scroll = 'window.scrollBy(0,500)'
        driver.execute_script(scroll)
        time.sleep(1)

    print(' 按完了')

username = str(input('Username: '))
password = str(input('Password: '))

login(username,password)
presslike()