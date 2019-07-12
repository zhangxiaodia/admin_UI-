from selenium import webdriver
import time
class Login():
	def user_login(self,driver):
		username='test'
		password='qq123456'
		driver.find_element_by_name('username').send_keys(username)
		driver.find_element_by_name('password').send_keys(password)
		driver.find_element_by_tag_name('button').click()
		time.sleep(3)

	def user_logout(self,driver):
		driver.find_element_by_css_selector(".el-icon-caret-bottom").click()
		time.sleep(2)
		driver.find_element_by_css_selector(".el-dropdown-menu__item > span").click()
		