import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class useuni(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_pdf(self):

		driver=self.driver
		driver.get("https://drive.google.com/drive/my-drive")
		time.sleep(4)

		user = driver.find_element_by_id("identifierId")
		user.send_keys("pp252525252585@gmail.com")
		user.send_keys(Keys.ENTER)
		time.sleep(2)

		password =driver.find_element_by_name("password")
		password.send_keys("zaqwe456")
		password.send_keys(Keys.ENTER)
		time.sleep(8)

		search=driver.find_element_by_xpath("//*[@id='gs_lc50']/input[1]")
		search.send_keys("pdf")
		time.sleep(3)
		search.send_keys(Keys.ENTER)

		time.sleep(4)
		singout=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a")
		singout.click()
		time.sleep(5)
		cerrar=driver.find_element_by_xpath("//*[@id='gb_71']")
		cerrar.click()
		time.sleep(4)


if __name__ == '__main__':
	unittest.main()