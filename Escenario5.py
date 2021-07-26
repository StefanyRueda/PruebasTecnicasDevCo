import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class useuni(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_language(self):
		driver=self.driver

		driver.get("https:\\www.gmail.com")
		time.sleep(1)
		
		user = driver.find_element_by_id("identifierId")
		user.send_keys("pp252525252585@gmail.com")
		user.send_keys(Keys.ENTER)
		time.sleep(2)

		password =driver.find_element_by_name("password")
		password.send_keys("zaqwe456")
		password.send_keys(Keys.ENTER)
		time.sleep(10)

		perfil=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img")
		perfil.click()
		time.sleep(3)

		cuenta=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[4]/div[1]/div[2]/a")
		cuenta.click()
		time.sleep(3)

		driver.switch_to.window(driver.window_handles[1])
		datos=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]")
		datos.send_keys("IDIOMA")
		time.sleep(3)
		datos.send_keys(Keys.ENTER)
		time.sleep(3)


		editar=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[2]/div/div[3]/c-wiz/div[1]/div[2]/div/div/div[1]/ul/li/div[1]/div[2]/div/button")
		editar.click()
		time.sleep(7)

		seleccion = driver.find_element_by_xpath("//*[@id='c6']")
		seleccion.send_keys("English")
		seleccion.send_keys(Keys.ENTER)
		time.sleep(3)
		english= driver.find_element_by_xpath("//*[@id='yDmH0d']/div[12]/div/div[2]/span/div/div/div[2]/div/span[22]/div[2]/div/div/div/span/span")
		english.click()
		time.sleep(5)

		country=driver.find_element_by_xpath("//*[@id='yDmH0d']/div[12]/div/div[2]/span/div/div/div[3]/div/span[1]/div[2]/div/div/div/span")
		country.click()
		time.sleep(3)

		ok =driver.find_element_by_xpath("//*[@id='yDmH0d']/div[12]/div/div[2]/div[3]/div[2]/button/span")
		ok.click()
		time.sleep(4)

		cerrar=driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img")
		cerrar.click()
		time.sleep(3)

		singout=driver.find_element_by_xpath("//*[@id='gb_71']")
		singout.click()
		time.sleep(4)


if __name__ == '__main__':
	unittest.main()