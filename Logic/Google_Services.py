from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
from Models.InfoAccount import NewInfo
import time
from selenium.webdriver.common.action_chains import ActionChains


def GG_Login(driver: webdriver, email: NewEmail) -> bool:
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
            click_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengeid='5']")))
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
        print("[INFO] Success Login Google")
        try:
            driver.get("https://accounts.google.com/")
            wait = WebDriverWait(driver, 10)
            input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            return True
        except:
            print("[INFO] Error Login Google")
            return False
    except:
        print("[INFO] Error Login Google")
        return False

def Login_Third_Website(driver: webdriver) -> bool:
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
        return True
    except:
        print("[INFO] Error Login third website with Google")
        return False

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
        print("[INFO] Success GG Translate")
    except:
        print("[INFO] Error GG Translate")

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
        print("[INFO] Success GG GG Alert")
    except:
        print("[INFO] Error GG Alert")

def Change_Info(driver: webdriver, infoAccount: NewInfo, email: NewEmail) -> NewEmail:
    try:
        driver.get("https://myaccount.google.com/profile/name/edit")
        wait = WebDriverWait(driver, 60)
        input_ten = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_ten.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        input_ten.send_keys(infoAccount.ten)
        time.sleep(2)
        input_ho = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
        input_ho.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        input_ho.send_keys(infoAccount.ho)

        wait = WebDriverWait(driver, 10)
        btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@jsname='Pr7Yme'])[3]")))
        time.sleep(2)
        btn_Save.click()
        print("[INFO] Success change name")
    except:
        print("[INFO] Error change name")

    try:
        driver.get("https://myaccount.google.com/recovery/email")
        wait = WebDriverWait(driver, 60)
        input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        time.sleep(2)
        input_recovery.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        input_recovery.send_keys(infoAccount.recovery)
        input_recovery.send_keys(Keys.ENTER)
        email.recovery = infoAccount.recovery
        print("[INFO] Success change recovery")
    except Exception as ex:
        print(f"[INFO] Error change recovery: {ex}")

    try:
        driver.get("https://myaccount.google.com/gender")
        wait = WebDriverWait(driver, 60)
        btn_gender = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[1]")))
        time.sleep(2)
        btn_gender.click()
        print("[INFO] Success change gender")
    except:
        print("[INFO] Error change gender")

    try:
        driver.get("https://myaccount.google.com/address/home")
        wait = WebDriverWait(driver, 60)
        input_address = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_address.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        input_address.send_keys(infoAccount.homeAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@jsname='y863Ob'])")))
            time.sleep(2)

            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            time.sleep(2)
            actions.send_keys(Keys.RETURN).perform()
        except:
            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            time.sleep(2)
            actions.send_keys(Keys.RETURN).perform()
        print("[INFO] Success change home address")
    except:
        print("[INFO] Error change home address")

    try:
        driver.get("https://myaccount.google.com/address/work")
        wait = WebDriverWait(driver, 60)
        input_address = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        input_address.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        input_address.send_keys(infoAccount.workAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@jsname='y863Ob'])")))
            time.sleep(2)

            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            time.sleep(2)
            actions.send_keys(Keys.RETURN).perform()
        except:
            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            time.sleep(2)
            actions.send_keys(Keys.RETURN).perform()
        print("[INFO] Success change work address")
    except:
        print("[INFO] Error change work address")

    try:
        driver.get("https://myaccount.google.com/signinoptions/password")
        wait = WebDriverWait(driver, 60)
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
        time.sleep(2)
        input_password.send_keys(infoAccount.password)

        re_enter_password = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        time.sleep(1)
        re_enter_password.send_keys(infoAccount.password)
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.RETURN).perform()
        try:
            time.sleep(2)
            actions.send_keys(Keys.RETURN).perform()
        except:
            None
        email.password = infoAccount.password
        print("[INFO] Success change password")
    except:
        print("[INFO] Error change password")
    return email

def Logout_Devices(driver: webdriver):
    try:
        while True:
            driver.get("https://myaccount.google.com/device-activity")

            wait = WebDriverWait(driver, 60)
            check_loadpage = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]')))
            if check_loadpage:
                try:
                    wait = WebDriverWait(driver, 10)
                    check_logout = wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]//p')))
                    if check_logout:
                        break
                except:
                    try:
                        wait = WebDriverWait(driver, 10)
                        click_logout = wait.until(
                            EC.presence_of_element_located((By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]')))
                        time.sleep(2)
                        try:
                            click_logout.click()
                        except:
                            driver.execute_script("arguments[0].click();", click_logout)

                        try:
                            time.sleep(5)
                            wait = WebDriverWait(driver, 60)
                            check_btn_logout = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='etzm7d']")))

                            actions = ActionChains(driver)
                            actions.send_keys(Keys.TAB).perform()
                            actions.send_keys(Keys.RETURN).perform()
                            time.sleep(5)
                            actions.send_keys(Keys.TAB).perform()
                            actions.send_keys(Keys.RETURN).perform()
                            time.sleep(3)
                        except:
                            None
                    except:
                        break
            else:
                break
    except:
        None
    finally:
        time.sleep(5)
        print("[INFO] Success logout")