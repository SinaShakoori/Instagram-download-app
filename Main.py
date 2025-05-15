from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

Service = chromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)


driver.get("https://www.instagram.com/")


username = "username"
password = "123456789"

user = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[1]/div/label/input""")
user.send_keys(f"{username}")

passw= driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[2]/div/label/input""")
passw.send_keys(f"{password}")


log = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[3]/button""")
log.click()

time.sleep(10)