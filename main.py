from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 



username= "your_username"
password= "your_password"




try:
    Service = chromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service)

    driver.get("https://www.instagram.com/")
    rob = driver.find_element(By.XPATH,"""/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]""")
    rob.click()
    time.sleep(3)
    user = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[1]/div/label/input""")
    user.send_keys(username)
    time.sleep(2)
    passw= driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[2]/div/label/input""")
    passw.send_keys(password)
    time.sleep(2)
    log = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div[1]/div[3]/button/div""")
    log.click()
    time.sleep(10)
    try:
        
        save = driver.find_element(By.XPATH,"""//*[@id="mount_0_0_lM"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div""")
        save.click()
        time.sleep(5)
    except:
        print(f"Error occurred:Error!")

except Exception as e:
    print(f"Error occurred: مشکل حساب!")
finally:
    input("Press Enter to close the browser...") 
    driver.quit()