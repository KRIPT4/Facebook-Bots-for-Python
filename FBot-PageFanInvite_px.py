#!/usr/bin/env python
"""
FBot-PageFanInvite_px.py - Facebook Bots for Python
Copyright 2017, KRIPT4

More info:
 * KRIPT4: https://github.com/KRIPT4/Facebook-Bots-for-Python
"""

# Import unittest module for creating unit tests
import unittest

# Import time module to implement 
import time

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

# For automating data input
from selenium.webdriver.common.keys import Keys

# For Proxy
from selenium.webdriver.common.proxy import *

# For providing custom configurations for Chrome to run
from selenium.webdriver.chrome.options import Options

NewProxy = "PROXYIPADDRESS:PORT"

start_time = time.time()		# TIME EXECUTION TEST

# Select which device you want to emulate by uncommenting it
# More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
mobile_emulation = { "deviceName": "Google Nexus 5"}
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--enable-precise-memory-info')
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--no-referrers')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-ssl-errors=true --debug=true')
chrome_options.add_argument('--window-size=375,733')
chrome_options.add_argument('--proxy-server=%s' % NewProxy)
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
global driver

def mainExe():
	global driver
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get('https://m.facebook.com/home.php')

	varUSER = '==USERNAME=='
	varPASS = '==PASSWORD=='
	i = 1 #START
	c = 5 #END

	## LOGIN
	retryElement('//*[@id="u_0_1"]/div[1]/div/input').send_keys(varUSER)
	retryElement('//*[@id="u_0_2"]').send_keys(varPASS)
	retryElement('//*[@id="u_0_6"]').click()
	## END LOGIN

	## SEND FAN PAGE INVITE
	driver.get('https://m.facebook.com/send_page_invite/?pageid=262588213843476')
	time.sleep(5)

	while (i < c):
		valuef = '//*[@id="m_invitee_list"]/div[' + str(i) + ']/div[3]/div/div/button'
		retryElement(valuef).click()
		time.sleep(2) #OPTIONAL
		i += 1
	print("END SEND LIKE")
	## END SEN FAN PAGE INVITE

	driver.quit()

	elapsed_time = time.time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error XPATH: %s" % xpath))

def brikear(msg):
	print(msg)
	closeDriver()
	sys.exit(1)

def closeDriver():
	global driver
	driver.quit()

try:
	mainExe()
except Exception as e:
	print(e)
	closeDriver()