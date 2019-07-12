from selenium import webdriver
import unittest
import time
import sys
from user_manage import Login
class party(unittest.TestCase):
	'''聚会测试'''
	def setUp(self):
		url='http://admin.muggle-inc.com'
		self.driver=webdriver.Firefox()
		self.driver.get(url)
		time.sleep(3)
	def tearDown(self):
		self.driver.quit()
	def test_party1(self):
		print(1)
		Login().user_login(self.driver)
		self.driver.find_element_by_xpath("//li/div").click()
		time.sleep(3)
		Login().user_logout(self.driver)
		time.sleep(3)
if __name__ == '__main__':
	unittest.main()