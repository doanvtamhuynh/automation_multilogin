from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail

def Login_GG(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://accounts.google.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        input_email.send_keys(email.email)
        input_email.send_keys(Keys.ENTER)

        wait = WebDriverWait(driver, 60)
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password'][@name='Passwd']")))
        input_password.send_keys(email.password)
        input_password.send_keys(Keys.ENTER)

        try:
            wait = WebDriverWait(driver, 20)
            click_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='Dl08I']//li[3]")))
            click_recovery.click()

            wait = WebDriverWait(driver, 20)
            input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            input_recovery.send_keys(email.recovery)
            input_recovery.send_keys(Keys.ENTER)
        except:
            print("[INFO] No need to enter Recovery")

        try:
            wait = WebDriverWait(driver, 5)
            simple_login = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
            simple_login.click()
        except:
            print("[INFO] No need to enter simple_login")

    except:
        print("[INFO] Error Login Google")