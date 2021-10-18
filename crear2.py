from selenium import webdriver
import time

nombre = "nombre"
mail = "tareauno@pebih.com"
contrasena = "123456"

driver = webdriver.Chrome()
driver.get('https://www.pccomponentes.com/signup')
time.sleep(30)

box = driver.find_element_by_xpath('//*[@id="name"]')
box.send_keys(nombre)
box = driver.find_element_by_xpath('//*[@id="email"]')
box.send_keys(mail)
box = driver.find_element_by_xpath('//*[@id="password"]')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="repeatPassword"]')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="policy"]').click()

time.sleep(10)
box = driver.find_element_by_xpath('//*[@id="root"]/main/section[2]/form/button[2]').click()
time.sleep(10)