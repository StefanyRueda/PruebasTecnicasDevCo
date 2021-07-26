import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class useunittest(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
		
	def test_meetnew(self):
		driver=self.driver
		driver.get("https:\\www.gmail.com")
		time.sleep(1)

		
		user = driver.find_element_by_id("identifierId")
		user.send_keys("pp252525252585@gmail.com")
		user.send_keys(Keys.ENTER)
		time.sleep(3)

		password =driver.find_element_by_name("password")
		password.send_keys("zaqwe456")
		password.send_keys(Keys.ENTER)
		time.sleep(5)

		meet=driver.find_element_by_xpath("//*[@id=':4f']/div/div[2]/span/a")
		meet.send_keys(Keys.ENTER)
		

		time.sleep(3)

		handles = self.driver.window_handles
		for handle in handles:
			driver.switch_to.window(handle)
			

		newmeet=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[3]/div/button/span")
		newmeet.click()
		time.sleep(5)
		
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)
		cerrar=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img")
		cerrar.click()
		time.sleep(3)

		singout=driver.find_element_by_xpath("//*[@id='gb_71']")
		singout.click()
		time.sleep(5)


if __name__ == '__main__':
	unittest.main()

