from selenium import webdriver
import time

mail = "tareauno@pebih.com"

driver = webdriver.Chrome()
driver.get('https://www.pccomponentes.com/recovery-password')
time.sleep(30)

box = driver.find_element_by_xpath('//*[@id="email"]')
box.send_keys(mail)
box = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click()
time.sleep(5)
box = driver.find_element_by_xpath('//*[@id="root"]/main/section/form/button/div').click()