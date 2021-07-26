import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class useuni(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_maps(self):

		driver=self.driver
		driver.get("https://www.google.com/maps/@15,-2.970703,3z?hl=es")
		time.sleep(4)


		indica=driver.find_element_by_xpath("//*[@id='searchbox-directions']/img")
		indica.click()
		time.sleep(4)

		origen=driver.find_element_by_xpath("//*[@id='sb_ifc51']/input")
		origen.send_keys("Simón Bolivar")
		origen.send_keys(Keys.ENTER)
		time.sleep(3)

		destino=driver.find_element_by_xpath("//*[@id='sb_ifc52']/input")

		destino.send_keys("Minuto de Dios")
		destino.send_keys(Keys.ENTER)
		time.sleep(2)


		ruta=driver.find_element_by_xpath("//*[@id='omnibox-directions']/div/div[2]/div/div/div[1]/div[2]/button/img")
		ruta.click()
		time.sleep(3)

		acceso=driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[6]/div[1]/div[2]/button")
		acceso.click()
		time.sleep(4)

		acceder=driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[6]/div[1]/div[2]/div/div/button")
		acceder.click()
		time.sleep(4)

		user = driver.find_element_by_id("identifierId")
		user.send_keys("pp252525252585@gmail.com")
		user.send_keys(Keys.ENTER)
		time.sleep(2)

		password =driver.find_element_by_name("password")
		password.send_keys("zaqwe456")
		password.send_keys(Keys.ENTER)
		time.sleep(10)

		handles = self.driver.window_handles
		for handle in handles:
			driver.switch_to.window(handle)

		correo=driver.find_element_by_xpath("//*[@id='hoNUob-Sx9Kwc-m5SR9c']/div[2]/div/div[3]/div/div/div[2]/div/div/div[1]/span[3]")
		correo.click()
		time.sleep(4)

		cerrar=driver.find_element_by_xpath("//*[@id='gb']/div/div/div[1]/div[2]/div[1]/a/img")
		cerrar.click()
		time.sleep(3)

		singout=driver.find_element_by_xpath("//*[@id='gb_71']")
		singout.click()
		time.sleep(5)


if __name__ == '__main__':
	unittest.main()