from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.flipkart.com/")
    time.sleep(3)
    check_element = driver.find_element(By.NAME, "q")
    check_element.send_keys("laptop")
    time.sleep(3)
    check_element.send_keys(Keys.ENTER)
    time.sleep(5)
    

finally:
    driver.quit()