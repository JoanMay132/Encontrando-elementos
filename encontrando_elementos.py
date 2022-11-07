
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class usando_unittest(unittest.TestCase): #heredando de la clase unittest.TestCase
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") 

    def test_buscar(self): #nombre del test
        driver=self.driver #llamando al driver
        driver.get("https://es.wikipedia.org/wiki/Programaci%C3%B3n") #abriendo la pagina
        time.sleep(3) #esperando 3 segundos
        self.assertIn("Programación",driver.title) #verificando que la palabra Programación este en el titulo de la pagina  
        elemento= driver.find_element(By.NAME,"search") #buscando el elemento con el nombre search
        elemento.send_keys("Selenium") #enviando la palabra Selenium
        elemento.send_keys(Keys.RETURN) #enviando la tecla enter
        time.sleep(5)   #esperando 5 segundos
        time.sleep(3) #esperando 3 segundos
        assert "No se encontró el elemento" not in driver.page_source #verificando que la palabra Selenium este en el codigo fuente de la pagina

    def tearDown(self): 
        self.driver.close() #cerrando el driver

if __name__=='__main__': #si el archivo se ejecuta directamente
    unittest.main() #ejecutar el test