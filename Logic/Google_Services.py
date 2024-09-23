from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
from Models.InfoAccount import NewInfo
import time


def GG_Login(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://accounts.google.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        input_email.send_keys(email.email)
        input_email.send_keys(Keys.ENTER)

        wait = WebDriverWait(driver, 60)
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password'][@name='Passwd']")))
        time.sleep(2)
        input_password.send_keys(email.password)
        input_password.send_keys(Keys.ENTER)

        try:
            wait = WebDriverWait(driver, 10)
            click_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='Dl08I']//li[3]")))
            time.sleep(2)
            click_recovery.click()

            wait = WebDriverWait(driver, 10)
            input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            time.sleep(2)
            input_recovery.send_keys(email.recovery)
            input_recovery.send_keys(Keys.ENTER)
        except:
            print("[INFO] No need to enter Recovery")

        try:
            wait = WebDriverWait(driver, 5)
            simple_login = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
            time.sleep(2)
            simple_login.click()
        except:
            print("[INFO] No need to enter simple_login")

    except:
        print("[INFO] Error Login Google")
    finally:
        print("[INFO] Success Login Google")

def Login_Third_Website(driver: webdriver):
    try:
        wait = WebDriverWait(driver, 60)
        select_account = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-authuser='0']")))
        time.sleep(2)
        select_account.click()
        time.sleep(1)
        wait = WebDriverWait(driver, 60)
        btn_Continue = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
        time.sleep(2)
        btn_Continue.click()

    except:
        print("[INFO] Error Login third website with Google")

def GG_Translate(driver: webdriver, wordList: list):
    try:
        for word in wordList:
            try:
                driver.get('https://translate.google.com/')
                wait = WebDriverWait(driver, 60)
                input_word = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea")))
                time.sleep(2)
                input_word.send_keys(word)
                time.sleep(3)
            except:
                continue
    except:
        print("[INFO] Error GG Translate")
    finally:
        print("[INFO] Success GG Translate")

def GG_ALert(driver: webdriver, wordList: list):
    try:
        for word in wordList:
            try:
                driver.get("https://www.google.com/alerts")
                wait = WebDriverWait(driver, 60)
                input_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
                time.sleep(2)
                input_word.send_keys(word)

                wait = WebDriverWait(driver, 60)
                click_alert = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='create_alert']")))
                time.sleep(2)
                click_alert.click()
                time.sleep(3)
            except:
                continue
    except:
        print("[INFO] Error GG Alert")
    finally:
        print("[INFO] Success GG GG Alert")

def Change_Info(driver: webdriver, infoAccount: NewInfo):
    try:
        driver.get("https://myaccount.google.com/profile/name/edit")
        wait = WebDriverWait(driver, 60)
        input_ten = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_ten.send_keys(infoAccount.ten)
        time.sleep(2)
        input_ho = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
        input_ho.send_keys(infoAccount.ho)

        wait = WebDriverWait(driver, 10)
        btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@jsname='Pr7Yme'])[3]")))
        time.sleep(2)
        btn_Save.click()
    except:
        print("[INFO] Error change name")
    finally:
        print("[INFO] Success change name")

    try:
        driver.get("https://myaccount.google.com/recovery/email")
        wait = WebDriverWait(driver, 60)
        input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        time.sleep(2)
        input_recovery.send_keys(infoAccount.recovery)
        wait = WebDriverWait(driver, 10)
        btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@jsname='Pr7Yme'])[3]")))
        time.sleep(1)
        btn_Save.click()
    except:
        print("[INFO] Error change recovery")
    finally:
        print("[INFO] Success change recovery")

    try:
        driver.get("https://myaccount.google.com/address/home")
        wait = WebDriverWait(driver, 60)
        input_address = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_address.send_keys(infoAccount.homeAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@jsname='y863Ob'])")))
            time.sleep(2)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.ENTER)
        except:
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.ENTER)
    except:
        print("[INFO] Error change home address")
    finally:
        print("[INFO] Success change home address")

    try:
        driver.get("https://myaccount.google.com/address/work")
        wait = WebDriverWait(driver, 60)
        input_address = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_address.send_keys(infoAccount.workAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@jsname='y863Ob'])")))
            time.sleep(2)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.ENTER)
        except:
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.TAB)
            time.sleep(0.5)
            driver.send_keys(Keys.ENTER)
    except:
        print("[INFO] Error change work address")
    finally:
        print("[INFO] Success change work address")

    try:
        driver.get("https://myaccount.google.com/signinoptions/password")
        wait = WebDriverWait(driver, 60)
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
        time.sleep(2)
        input_password.send_keys(infoAccount.password)

        re_enter_password = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        time.sleep(1)
        re_enter_password.send_keys(infoAccount.password)
        driver.send_keys(Keys.ENTER)
    except:
        print("[INFO] Error change password")
    finally:
        print("[INFO] Success change password")