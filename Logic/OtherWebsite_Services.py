from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
import time
import pyautogui
import Logic.Google_Services as Google

def Website_TLDR(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://tldr.tech/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        time.sleep(2)
        input_email.send_keys(email.email)
        click_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        time.sleep(2)
        click_submit.click()

        wait = WebDriverWait(driver, 60)
        btn_save1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save1.click()

        wait = WebDriverWait(driver, 60)
        btn_save2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save2.click()

        wait = WebDriverWait(driver, 60)
        btn_save3 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save3.click()

        wait = WebDriverWait(driver, 60)
        input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='company_website']")))
        time.sleep(2)
        input_text.send_keys("skyboss.com")

        wait = WebDriverWait(driver, 60)
        btn_submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_submit.click()

    except:
        print("[INFO] Error Website https://tldr.tech/")

def Website_Envalior(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.envalior.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        time.sleep(2)
        input_email.send_keys(email.email)
        btn_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        time.sleep(2)
        btn_checkbox.click()
        try:
            btn_submit = driver.find_element(By.XPATH, "//button[@type='SUBMIT']")
            time.sleep(2)
            btn_submit.click()
        except:
            btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
            time.sleep(2)
            btn_submit.click()
    except:
        print("[INFO] Error Website https://www.envalior.com/")

def Website_Foxnews(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.foxnews.com/newsletters")

        wait = WebDriverWait(driver, 60)
        btn_subcribe = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='button subscribe'])[1]//a")))
        time.sleep(2)
        btn_subcribe.click()
        time.sleep(2)
        driver.send_keys(Keys.TAB)
        time.sleep(1)
        pyautogui.typewrite(email.email)
        time.sleep(1)
        driver.send_keys(Keys.TAB)
        time.sleep(1)
        driver.send_keys(Keys.ENTER)
        time.sleep(5)

        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.TAB)
        driver.send_keys(Keys.ENTER)
    except:
        print("[INFO] Error Website https://www.foxnews.com/newsletters")

def Website_Batdongsan(driver: webdriver):
    try:
        driver.get("https://batdongsan.com.vn/sellernet/trang-dang-nhap")
        wait = WebDriverWait(driver, 60)
        main_window = driver.current_window_handle
        btn_LoginGG = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-tracking-label='type=Google']")))
        time.sleep(2)
        btn_LoginGG.click()
        time.sleep(2)
        windows = driver.window_handles
        try:
            for window in windows:
                if window != main_window:
                    driver.switch_to.window(window)
                    time.sleep(2)
                    Google.Login_Third_Website(driver)
                    time.sleep(2)
                    driver.close()
                    break
            driver.switch_to.window(main_window)

        except:
            print("[INFO] Error Login with Google")

        driver.get("https://batdongsan.com.vn/nha-dat-ban-ha-noi")
        wait = WebDriverWait(driver, 60)
        btn_bell = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='re__btn re__btn-icon--lg re__icon-switch-save-alert js__switch-save-alert-v3']")))
        time.sleep(2)
        btn_bell.click()

        wait = WebDriverWait(driver, 60)
        btn_Submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@tracking-id='click-save-search-alert-option1']")))
        time.sleep(2)
        btn_Submit.click()
    except:
        print("[INFO] Error Website Bat Dong San")

def Website_Dictionary(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.dictionary.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_email.send_keys(email.email)

        btn_submit = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
        time.sleep(2)
        btn_submit.click()
    except:
        print("[INFO] Error Website Dictionary")

def Website_ITViec(driver: webdriver):
    try:
        driver.get("https://itviec.com/sign_in")

        wait = WebDriverWait(driver, 60)
        btn_LoginGG = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'])[1]")))
        time.sleep(2)
        btn_LoginGG.click()
        Google.Login_Third_Website(driver)
        time.sleep(5)
        btn_Next = driver.find_element(By.XPATH, "(//button[@type='button'])[1]")
        time.sleep(2)
        btn_Next.click()

        wait = WebDriverWait(driver, 60)
        btn_Select_Java = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[1]")))
        time.sleep(2)
        btn_Select_Java.click()
        btn_Select_ReactJs = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
        btn_Select_ReactJs.click()
        btn_Select_DotNet = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]")
        btn_Select_DotNet.click()
        btn_Select_HCM = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
        btn_Select_HCM.click()

        wait = WebDriverWait(driver, 60)
        btn_Subcribe = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@data-jr-onboarding-target='buttonSubmit'])")))
        time.sleep(2)
        btn_Subcribe.click()
    except:
        print("[INFO] Error website ITViec")

def Website_Quora(driver: webdriver):
    try:
        driver.get("https://humanity.quora.com")

        wait = WebDriverWait(driver, 60)
        btn_SignIn = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[3]")))
        time.sleep(2)
        btn_SignIn.click()

        wait = WebDriverWait(driver, 60)
        btn_Continue = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='c13dhsxm'])[1]")))
        time.sleep(2)
        btn_Continue.click()
        Google.Login_Third_Website(driver)
        time.sleep(2)

        driver.get("https://humanity.quora.com")
        wait = WebDriverWait(driver, 60)
        btn_Follow = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[6]")))
        time.sleep(2)
        btn_Follow.click()

        wait = WebDriverWait(driver, 60)
        btn_Bell = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@role='button'])[8]")))
        time.sleep(2)
        btn_Bell.click()

        wait = WebDriverWait(driver, 60)
        checkbox_AllPost = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[1]")))
        time.sleep(2)
        checkbox_AllPost.click()

        btn_Email = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
        attribute_value_btn_Email = btn_Email.get_attribute("aria-checked")
        time.sleep(2)
        if attribute_value_btn_Email == "false":
            btn_Email.click()

        driver.get("https://www.quora.com/settings/notifications")
        wait = WebDriverWait(driver, 60)
        btn_Daily = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[2]")))
        time.sleep(2)
        btn_Daily.click()

    except:
        print("[INFO] Error website Quora")