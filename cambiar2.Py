from selenium import webdriver
import time
mail = "tareauno@pebih.com"
contrasena = "123asd"
contrasenanew="123asd"

driver = webdriver.Chrome()
driver.get('https://www.pccomponentes.com/usuarios/panel/mis-datos')
time.sleep(30)

box = driver.find_element_by_xpath('//*[@id="username"]')
box.send_keys(mail)
box = driver.find_element_by_xpath('//*[@id="password"]')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="login-form"]/button[2]').click()

time.sleep(5)

box = driver.find_element_by_xpath('//*[@id="userPassword_password"]')
box.send_keys(contrasena)
box = driver.find_element_by_xpath('//*[@id="userPassword_passwordConfirm"]')
box.send_keys(contrasenanew)
box = driver.find_element_by_xpath('//*[@id="userPassword_passwordConfirm2"]')
box.send_keys(contrasenanew)
box = driver.find_element_by_xpath('//*[@id="user_password_create"]').click()
time.sleep(5)
