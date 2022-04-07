##!/usr/bin/env python
#day9 Auto log in Facebook

import email
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.facebook.com'
email = input('your email: ')
password = input('your password: ')
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_id('pass').send_keys(password)
browser.find_element_by_id('loginbutton').click()