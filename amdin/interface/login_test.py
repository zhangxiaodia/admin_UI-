from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


class loginTest(unittest.TestCase):
	'''用户登陆测试'''
	def setUp(self):
		url='http://admin.muggle-inc.com'
		self.driver=webdriver.Firefox()
		self.driver.get(url)
		self.driver.implicitly_wait(10)
#		self.username="test"
#		self.password="qq123456"

	#数据驱动
		
#			print(username,password)


	def tearDown(self):
		self.driver.quit()

	def test_login1(self):
		'''普通用户密码'''
		
		username='test'
		password='qq123456'
		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
#			time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()
		time.sleep(3)
		now_url=self.driver.current_url
		self.assertEqual(now_url,"http://admin.muggle-inc.com/desktop")
	def test_login2(self):
		'''管理员用户密码'''
		#读取txt文件
		username='Sanit'
		password='Fansclub321'
		
		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
#		time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()
		time.sleep(3)
		now_url=self.driver.current_url
		self.assertEqual(now_url,"http://admin.muggle-inc.com/desktop")
	def test_login3(self):
		'''用户名&密码均为空'''
		#读取txt文件
		username=''
		password=''
		
		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
#		time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()
		time.sleep(3)
		now_url=self.driver.current_url
		self.assertNotEqual(now_url,"http://admin.muggle-inc.com/desktop")
	def test_login4(self):
		'''用户名/密码均为空'''
		#读取txt文件
		username='test'
		password=''
		
		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
#		time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()
		time.sleep(3)
		now_url=self.driver.current_url
		self.assertNotEqual(now_url,"http://admin.muggle-inc.com/desktop")
	def test_login5(self):
		'''密码错误'''
		#读取txt文件
		username='test'
		password='qq12345678'
		
		self.driver.find_element_by_name('username').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(password)
#		time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()
		time.sleep(3)
		now_url=self.driver.current_url
		self.assertNotEqual(now_url,"http://admin.muggle-inc.com/desktop")


'''	def test_login(self):
		
		
		self.driver.find_element_by_name('username').send_keys(self.username)
		self.driver.find_element_by_name('password').send_keys(self.password)
		time.sleep(3)
		self.driver.find_element_by_tag_name('button').click()'''
if __name__ == '__main__':
#	testunit=unittest.TestSuite()
#	testunit.addTest(loginTest("test_login"))
#	now_time=time.strftime("%Y-%m-%d %H-%M-%S")
#	file_name='../report/'+now_time+'result.html'
#	fp=open(file_name,'wb')
#	runnner=HTMLTestRunner(stream=fp,title='后台管理测试报告',description='用例执行情况：')
#	runnner.run(testunit)
#	fp.close()
	unittest.main()
