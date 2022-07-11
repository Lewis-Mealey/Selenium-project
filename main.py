import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://chrome.google.com/webstore/detail/windows-accounts/ppnbnpeolgkicgegkbkbjmhlideopiji")

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "g-c-Hf"))
    )
finally:
    search = driver.find_element(By.CLASS_NAME, "g-c-Hf")
    search.click()

time.sleep(5)

driver.get("https://nitec.eu.itglue.com/organizations")

#username
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
finally:
    search = driver.find_element("id", "i0116")
    search.send_keys("username")
    search.send_keys(Keys.RETURN)

#password
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )
finally:
    search = driver.find_element("name", "passwd")
    search.send_keys("password")

#submit
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
finally:
    time.sleep(3)
    search = driver.find_element("id", "idSIButton9")
    search.click()

time.sleep(3)

search = driver.find_element("class", "table-cell text-left content")
search.click()
