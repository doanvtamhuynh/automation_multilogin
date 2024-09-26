from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
from Models.InfoAccount import NewInfo
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
import time


async def GG_Login(driver: webdriver, email: NewEmail) -> bool:
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://accounts.google.com/")

        wait = WebDriverWait(driver, 60)
        input_email = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_email.send_keys, email.email)
        await loop.run_in_executor(None, input_email.send_keys, Keys.ENTER)

        wait = WebDriverWait(driver, 60)
        input_password = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@type='password'][@name='Passwd']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_password.send_keys, email.password)
        await loop.run_in_executor(None, input_password.send_keys, Keys.ENTER)

        try:
            wait = WebDriverWait(driver, 10)
            click_recovery = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//div[@data-challengeid='5']")))
            await asyncio.sleep(2)
            await loop.run_in_executor(None, click_recovery.click)

            wait = WebDriverWait(driver, 10)
            input_recovery = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            await asyncio.sleep(2)
            await loop.run_in_executor(None, input_recovery.send_keys, email.password)
            await loop.run_in_executor(None, input_recovery.send_keys, Keys.ENTER)

        except:
            print("[INFO] No need to enter Recovery")

        try:
            wait = WebDriverWait(driver, 5)
            simple_login = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
            await asyncio.sleep(2)
            await loop.run_in_executor(None, simple_login.click)
        except:
            print("[INFO] No need to enter simple_login")
        print("[INFO] Success Login Google")
        return True
    except:
        print("[INFO] Error Login Google")
        return False

async def Login_Third_Website(driver: webdriver) -> bool:
    loop = asyncio.get_running_loop()
    try:
        wait = WebDriverWait(driver, 60)
        select_account = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//div[@data-authuser='0']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, select_account.click)
        await asyncio.sleep(1)
        wait = WebDriverWait(driver, 60)
        btn_Continue = await loop.run_in_executor(None, wait.until,
                                              EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_Continue.click)
        return True
    except:
        print("[INFO] Error Login third website with Google")
        return False

async def GG_Translate(driver: webdriver, wordList: list):
    loop = asyncio.get_running_loop()
    try:
        for word in wordList:
            try:
                driver.get('https://translate.google.com/')
                wait = WebDriverWait(driver, 60)
                input_word = await loop.run_in_executor(None, wait.until,
                                                    EC.presence_of_element_located(
                                                        (By.XPATH, "//textarea")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, input_word.send_keys, word)
                await asyncio.sleep(3)
            except:
                continue
        print("[INFO] Success GG Translate")
    except:
        print("[INFO] Error GG Translate")

async def GG_ALert(driver: webdriver, wordList: list):
    loop = asyncio.get_running_loop()
    try:
        for word in wordList:
            try:
                driver.get("https://www.google.com/alerts")
                wait = WebDriverWait(driver, 60)
                input_word = await loop.run_in_executor(None, wait.until,
                                                  EC.presence_of_element_located(
                                                      (By.XPATH, "//input[@type='text']")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, input_word.send_keys, word)

                wait = WebDriverWait(driver, 60)
                click_alert = await loop.run_in_executor(None, wait.until,
                                                  EC.presence_of_element_located(
                                                      (By.XPATH, "//span[@id='create_alert']")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, click_alert.click)
                await asyncio.sleep(3)
            except:
                continue
        print("[INFO] Success GG GG Alert")
    except:
        print("[INFO] Error GG Alert")

async def Change_Info(driver: webdriver, infoAccount: NewInfo):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://myaccount.google.com/profile/name/edit")

        wait = WebDriverWait(driver, 60)
        input_ten = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_ten.click)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, input_ten.send_keys, infoAccount.ten)
        await asyncio.sleep(2)

        input_ho = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[3]")))
        await loop.run_in_executor(None, input_ho.click)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, input_ho.send_keys, infoAccount.ho)

        wait = WebDriverWait(driver, 10)
        btn_Save = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//button[@jsname='Pr7Yme'])[3]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_Save.click)
        print("[INFO] Success change name")
    except:
        print("[INFO] Error change name")

    try:
        driver.get("https://myaccount.google.com/recovery/email")

        wait = WebDriverWait(driver, 60)
        input_recovery = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_recovery.click)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, input_recovery.send_keys, infoAccount.recovery)
        await loop.run_in_executor(None, input_recovery.send_keys, Keys.ENTER)

        print("[INFO] Success change recovery")
    except Exception as ex:
        print(f"[INFO] Error change recovery: {ex}")

    try:
        driver.get("https://myaccount.google.com/gender")
        wait = WebDriverWait(driver, 60)
        btn_gender = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[1]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_gender.click)
        print("[INFO] Success change gender")
    except:
        print("[INFO] Error change gender")

    try:
        driver.get("https://myaccount.google.com/address/home")
        wait = WebDriverWait(driver, 60)
        input_address = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_address.click)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, input_address.send_keys, infoAccount.homeAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                (By.XPATH, "(//div[@jsname='y863Ob'])")))

            await asyncio.sleep(2)

            actions = ActionChains(driver)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await asyncio.sleep(2)
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        except:
            actions = ActionChains(driver)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await asyncio.sleep(2)
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        print("[INFO] Success change home address")
    except:
        print("[INFO] Error change home address")

    try:
        driver.get("https://myaccount.google.com/address/work")
        wait = WebDriverWait(driver, 60)
        input_address = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='text'])[2]")))
        await loop.run_in_executor(None, input_address.click)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform)
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_address.send_keys, infoAccount.workAddress)

        try:
            wait = WebDriverWait(driver, 5)
            btn_Save = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                (By.XPATH, "(//div[@jsname='y863Ob'])")))

            await asyncio.sleep(2)

            actions = ActionChains(driver)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await asyncio.sleep(2)
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        except:
            actions = ActionChains(driver)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
            await asyncio.sleep(2)
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        print("[INFO] Success change work address")
    except:
        print("[INFO] Error change work address")

    try:
        driver.get("https://myaccount.google.com/signinoptions/password")
        wait = WebDriverWait(driver, 60)
        input_password = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                                            (By.XPATH, "(//input[@type='password'])[1]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_password.send_keys, infoAccount.password)

        re_enter_password = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='password'])[2]")))
        await asyncio.sleep(1)
        await loop.run_in_executor(None, re_enter_password.send_keys, infoAccount.password)
        await asyncio.sleep(1)
        actions = ActionChains(driver)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)
        try:
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        except:
            None
        print("[INFO] Success change password")
    except:
        print("[INFO] Error change password")

async def Logout_Devices(driver: webdriver):
    loop = asyncio.get_running_loop()
    try:
        while True:
            driver.get("https://myaccount.google.com/device-activity")

            wait = WebDriverWait(driver, 60)
            check_loadpage = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]')))

            if check_loadpage:
                try:
                    wait = WebDriverWait(driver, 10)
                    check_logout = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                        (By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]//p')))

                    if check_logout:
                        break
                except:
                    try:
                        wait = WebDriverWait(driver, 10)
                        click_logout = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                            (By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]')))

                        await asyncio.sleep(2)
                        try:
                            await loop.run_in_executor(None, click_logout.click)
                        except:
                            await loop.run_in_executor(None, driver.execute_script, "arguments[0].click();", click_logout)

                        try:
                            await asyncio.sleep(5)
                            wait = WebDriverWait(driver, 60)
                            check_btn_logout = await loop.run_in_executor(None, wait.until,
                                                                    EC.presence_of_element_located((By.XPATH, "//div[@class='etzm7d']")))

                            actions = ActionChains(driver)
                            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
                            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
                            await asyncio.sleep(5)
                            await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
                            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
                            await asyncio.sleep(3)
                        except:
                            None
                    except:
                        break
            else:
                break
    except:
        None
    finally:
        await asyncio.sleep(5)
        print("[INFO] Success logout")
