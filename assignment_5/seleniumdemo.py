# import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("mern stack developer")
search_box.send_keys(Keys.RETURN)

# photo_link = driver.find_element(By.XPATH, "//img[contains(@class,'mw-file-element')]").click()




driver.implicitly_wait(5)

time.sleep(10)
driver.quit()