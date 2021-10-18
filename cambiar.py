from selenium import webdriver
import time
mail = "tareauno@pebih.com"
contrasena = "123456"

driver = webdriver.Chrome()
driver.get('https://gameshark.cl/datos-personales')


box = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
box.send_keys(mail)

box = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="submit-login"]').click()
time.sleep(5)

box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div[1]/div/input')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[6]/div[1]/div/input')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="ff_customer_privacy"]').click()
box = driver.find_element_by_xpath('//*[@id="ff_psgdpr"]').click()


box = driver.find_element_by_xpath('//*[@id="customer-form"]/footer/button').click()
time.sleep(5)

