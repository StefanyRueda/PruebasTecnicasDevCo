import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class useuni(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_calendar(self):

		driver=self.driver
		driver.get("https://accounts.google.com/signin/v2/identifier?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
		time.sleep(2)

		user = driver.find_element_by_id("identifierId")
		user.send_keys("pp252525252585@gmail.com")
		user.send_keys(Keys.ENTER)
		time.sleep(2)

		password =driver.find_element_by_name("password")
		password.send_keys("zaqwe456")
		password.send_keys(Keys.ENTER)
		time.sleep(5)

		crear=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/button/span[2]/div[2]")
		crear.click()
		time.sleep(4)

		name=driver.find_element_by_xpath("//*[@id='yDmH0d']/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input")

		name.send_keys("Evaluation")
		time.sleep(3)

		type_event= driver.find_element_by_xpath("//*[@id='yDmH0d']/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/span")
		type_event.click()
		
		time.sleep(3)
				
		save=driver.find_element_by_xpath("//*[@id='yDmH0d']/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[4]/span/span")
		save.click()
		time.sleep(3)

		singout=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a")
		singout.click()
		time.sleep(5)
		cerrar=driver.find_element_by_xpath("//*[@id='gb_71']")
		cerrar.click()
		
		time.sleep(4)
	
if __name__ == '__main__':
	unittest.main()