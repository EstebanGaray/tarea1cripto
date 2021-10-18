from selenium import webdriver
import time

mail = "tareauno@pebih.com"

driver = webdriver.Chrome()
driver.get('https://gameshark.cl/recuperar-contrase%C3%B1a')
time.sleep(5)

box = driver.find_element_by_xpath('//*[@id="email"]')
box.send_keys(mail)
box = driver.find_element_by_xpath('//*[@id="content"]/section/form/button').click()