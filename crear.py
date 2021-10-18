from selenium import webdriver
import time

nombre = "nombre"
apellidos = "apellido"
mail = "tareauno@pebih.com"
contrasena = "123456"

driver = webdriver.Chrome()
driver.get('https://gameshark.cl/iniciar-sesion?create_account=1')
time.sleep(5)

box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[2]/div[1]/input')
box.send_keys(nombre)
box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[3]/div[1]/input')
box.send_keys(apellidos)
box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[4]/div[1]/input')
box.send_keys(mail)
box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div[1]/div/input')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="ff_customer_privacy"]').click()
box = driver.find_element_by_xpath('//*[@id="ff_psgdpr"]').click()
time.sleep(10)
box = driver.find_element_by_xpath('//*[@id="customer-form"]/footer/button').click()
time.sleep(10)