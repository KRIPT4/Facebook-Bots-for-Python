#!/usr/bin/env python
"""
FBot-AutoLogin.py - Facebook Bots for Python
Copyright 2017, KRIPT4

More info:
 * KRIPT4: https://github.com/KRIPT4/Facebook-Bots-for-Python
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

start_time = time.time()		# TIME EXECUTION TEST

#https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/chrome/options.py

chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--no-referrers')
chrome_options.add_argument('--window-size=800,800')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://m.facebook.com/home.php')

time.sleep(5)

varUSER = '==USERNAME=='
varPASS = '==PASSWORD=='

## LOGIN
driver.find_element_by_xpath('//*[@id="u_0_1"]/div[1]/div/input').send_keys(varUSER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="u_0_2"]').send_keys(varPASS)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="u_0_6"]').click()
## END LOGIN

elapsed_time = time.time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)