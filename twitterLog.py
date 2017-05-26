from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.errorhandler import ErrorHandler
import selenium.webdriver.support.ui as ui
import unittest
import os
import sys
import time


def __init__():
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--ignore-ssl-errors')
		dir_path = os.path.dirname(os.path.realpath(__file__))
		chromedriver = dir_path + "/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		driver = webdriver.Chrome(chrome_options=options, executable_path= chromedriver)

class MyHandler(ErrorHandler):
    def check_response(self, response):
        try:
            super(MyHandler, self).check_response(response)
        except NoSuchElementException as e:
            e.stacktrace = None
            # PhantomJS specific line:
            e.msg = json.loads(e.msg)['errorMessage']
            raise
            
class TestLifeLabsLogin(unittest.TestCase):
	
	def life_login():
		browser=webdriver.Chrome()
		browser.get('http://www.twitter.com/')
	
		#user credentials
		login = browser.find_element_by_css_selector('a.Button.StreamsLogin.js-login').click()
		user = browser.find_element_by_name('session[username_or_email]')
		user.send_keys('')
		password = browser.find_element_by_name('session[password]')
		password.send_keys('')
		login_two = browser.find_element_by_css_selector('input.submit.btn.primary-btn.js-submit').click()
		browser.implicitly_wait(3)
		#menuEnter = browser.find_element_by_css_selector('dropdown-toggle-no-caret right middle').click()
		#menuPlayer = browser.find_element_by_css_selector('div:nth-child(4)').click()
		search = browser.find_element_by_id('search-query').send_keys('overwatch').click()
		browser.implicitly_wait(5)
		
	life_login()

	def tearDown(self):
		browser.implicitly_wait(5)
		self.driver.close()

if __name__ == '__main__':
	sys.tracebacklimit = 0
	
	
	

