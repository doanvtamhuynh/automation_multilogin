from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Models.Email import NewEmail
import time
import Logic.Google_Services as Google
import random
from selenium.webdriver.common.action_chains import ActionChains

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

        try:
            wait = WebDriverWait(driver, 10)
            btn_click_here = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='underline']")))
            time.sleep(1)
            btn_click_here.click()
        except:
            print("")

        time.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save1.click()

        time.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save2.click()

        time.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save3 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_save3.click()

        time.sleep(2)
        wait = WebDriverWait(driver, 60)
        input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='company_website']")))
        time.sleep(2)
        input_text.send_keys("skyboss.com")

        time.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)
        btn_submit.click()
        print("[INFO] Success Website TLDR")
    except:
        print("[INFO] Error Website TLDR")

def Website_Envalior(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.envalior.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        time.sleep(2)
        input_email.send_keys(email.email)

        btn_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        driver.execute_script("arguments[0].click();", btn_checkbox)

        try:
            btn_submit = driver.find_element(By.XPATH, "//button[@type='SUBMIT']")
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_submit)
        except:
            btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_submit)
        time.sleep(10)
        print("[INFO] Success Website Envalior")
    except:
        print("[INFO] Error Website Envalior")

def Website_Foxnews(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.foxnews.com/newsletters")

        wait = WebDriverWait(driver, 60)
        btn_subcribe = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='button subscribe'])[1]//a")))
        time.sleep(2)
        btn_subcribe.click()
        time.sleep(2)

        actions = ActionChains(driver)

        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)
        wait = WebDriverWait(driver, 60)
        input_question = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        input_question.send_keys(email.email)
        time.sleep(1)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(5)

        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(2)

        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(2)

        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        print("[INFO] Success Website Foxnew")
    except:
        print("[INFO] Error Website Foxnew")

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
        result_signin = False
        try:
            for window in windows:
                if window != main_window:
                    driver.switch_to.window(window)
                    time.sleep(2)
                    result_signin = Google.Login_Third_Website(driver)
                    time.sleep(2)
                    break
            driver.switch_to.window(main_window)
        except:
            print("[INFO] Error Login with Google")

        time.sleep(10)
        if result_signin is True:
            driver.get("https://batdongsan.com.vn/nha-dat-ban-ha-noi")
            wait = WebDriverWait(driver, 60)
            btn_bell = wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='re__icon-switch-off--lg js__save-alert-v3-switch-icon']/span")))
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_bell)

            time.sleep(10)
            wait = WebDriverWait(driver, 60)
            btn_Submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@tracking-id='click-save-search-alert-option1']")))
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_Submit)
            print("[INFO] Success Website Bat Dong San")
        else:
            print("[INFO] Error Website Bat Dong San")
    except:
        print("[INFO] Error Website Bat Dong San")

def Website_Dictionary(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://www.dictionary.com/")

        wait = WebDriverWait(driver, 120)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        time.sleep(2)
        input_email.send_keys(email.email)

        btn_submit = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
        time.sleep(2)
        btn_submit.click()
        print("[INFO] Success Website Dictionary")
    except:
        print("[INFO] Error Website Dictionary")

def Website_ITViec(driver: webdriver):
    try:
        driver.get("https://itviec.com/sign_in")

        wait = WebDriverWait(driver, 60)
        btn_LoginGG = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'])[1]")))
        time.sleep(2)
        btn_LoginGG.click()
        result_signin = Google.Login_Third_Website(driver)
        time.sleep(5)

        if result_signin is True:
            wait = WebDriverWait(driver, 30)
            btn_Next = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[1]")))
            time.sleep(2)
            btn_Next.click()

            wait = WebDriverWait(driver, 30)
            btn_Select_Java = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='skill_java']")))
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_Select_Java)
            btn_Select_ReactJs = driver.find_element(By.XPATH, "//label[@for='skill_reactjs']")
            driver.execute_script("arguments[0].click();", btn_Select_ReactJs)
            btn_Select_DotNet = driver.find_element(By.XPATH, "//label[@for='skill_net']")
            driver.execute_script("arguments[0].click();", btn_Select_DotNet)
            btn_Select_HCM = driver.find_element(By.XPATH, "//label[@for='city_ho-chi-minh-hcm']")
            driver.execute_script("arguments[0].click();", btn_Select_HCM)

            wait = WebDriverWait(driver, 30)
            btn_Subcribe = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-jr-onboarding-target='buttonSubmit']")))
            time.sleep(2)
            driver.execute_script("arguments[0].click();", btn_Subcribe)
            print("[INFO] Success website ITViec")
        else:
            print("[INFO] Error website ITViec")
    except:
        print("[INFO] Error website ITViec")


def Website_Quora(driver: webdriver):
    try:
        driver.get("https://humanity.quora.com")
        wait = WebDriverWait(driver, 60)
        btn_SignIn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'qu-ml--medium')]")))
        time.sleep(2)
        driver.execute_script("arguments[0].click();", btn_SignIn)

        wait = WebDriverWait(driver, 60)
        btn_Continue = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'puppeteer_test_login_button_google')]")))
        time.sleep(2)
        driver.execute_script("arguments[0].click();", btn_Continue)
        result_signin = Google.Login_Third_Website(driver)
        time.sleep(5)
        if result_signin is True:
            try:
                wait = WebDriverWait(driver, 60)
                btn_Follow = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'qu-bg--tribe_theme_blue')]")))
                time.sleep(2)
                try:
                    btn_Follow.click()
                except:
                    driver.execute_script("arguments[0].click();", btn_Follow)

                try:
                    wait = WebDriverWait(driver, 15)
                    btn_Bell = wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//div[@class="q-box qu-display--inline-block"]//button')))
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", btn_Bell)

                    try:
                        wait = WebDriverWait(driver, 30)
                        checkbox_AllPost = wait.until(
                            EC.presence_of_element_located((By.XPATH, "//input[@value='all_notifs']")))
                        driver.execute_script("arguments[0].click();", checkbox_AllPost)
                    except:
                        None

                    try:
                        wait = WebDriverWait(driver, 10)
                        btn_Email = wait.until(EC.presence_of_element_located(
                            (By.XPATH, "//input[@aria-checked='false' and @type='checkbox']")))
                        driver.execute_script("arguments[0].click();", btn_Email)
                    except:
                        None
                except:
                    wait = WebDriverWait(driver, 10)
                    btn_Bell = wait.until(EC.presence_of_element_located((By.XPATH, "id('notitifications')")))
                    time.sleep(2)
                    try:
                        btn_Bell.click()
                    except:
                        driver.execute_script("arguments[0].click();", btn_Bell)

                    try:
                        wait = WebDriverWait(driver, 30)
                        checkbox_AllPost = wait.until(
                            EC.presence_of_element_located((By.XPATH, "//input[@value='all_notifs']")))
                        driver.execute_script("arguments[0].click();", checkbox_AllPost)
                    except:
                        None

                    try:
                        wait = WebDriverWait(driver, 10)
                        btn_Email = wait.until(EC.presence_of_element_located(
                            (By.XPATH, "//input[@aria-checked='false' and @type='checkbox']")))
                        driver.execute_script("arguments[0].click();", btn_Email)
                    except:
                        None

            except:
                None

            driver.get("https://www.quora.com/settings/notifications")
            wait = WebDriverWait(driver, 60)
            btn_Daily = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='NotifSettingsRadioButtonsItem' and @value='2']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", btn_Daily)
            driver.execute_script("arguments[0].click();", btn_Daily)

            print("[INFO] Success website Quora")
        else:
            print("[INFO] Error website Quora")
    except:
        print("[INFO] Error website Quora")

def Website_InfoQ(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://infoq.vn/Registers/index")
        wait = WebDriverWait(driver, 60)
        input_surname = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='first_name']")))
        time.sleep(2)
        input_surname.send_keys("Harry")
        wait = WebDriverWait(driver, 60)
        input_lastname = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='last_name']")))
        input_lastname.send_keys("Potter")
        wait = WebDriverWait(driver, 60)
        input_email1 = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='email01']")))
        input_email1.send_keys(email.email)
        wait = WebDriverWait(driver, 60)
        input_email2 = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='email02']")))
        input_email2.send_keys(email.email)
        wait = WebDriverWait(driver, 60)
        input_password1 = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='pass01']")))
        input_password1.send_keys("Duchanh456@")
        wait = WebDriverWait(driver, 60)
        input_password2 = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='pass02']")))
        input_password2.send_keys("Duchanh456@")
        random_number = random.randint(10000000, 99999999)
        phone_number = f"09{random_number}"
        wait = WebDriverWait(driver, 60)
        input_phonenumber = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='phone_num1']")))
        input_phonenumber.send_keys(phone_number)
        wait = WebDriverWait(driver, 60)
        input_birth = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='birthday']")))
        input_birth.send_keys("14/03/1999")
        wait = WebDriverWait(driver, 60)
        click_gender = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='gt_1']")))
        click_gender.click()
        wait = WebDriverWait(driver, 60)
        dropdown_province = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='city_cd']")))
        select_province = Select(dropdown_province)
        select_province.select_by_value("56")
        wait = WebDriverWait(driver, 60)
        input_district = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='district']")))
        input_district.send_keys("abc")
        wait = WebDriverWait(driver, 60)
        input_village = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='village']")))
        input_village.send_keys("abc")
        wait = WebDriverWait(driver, 60)
        input_address = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='address']")))
        input_address.send_keys("abc")
        wait = WebDriverWait(driver, 60)
        dropdown_question = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='secret_question_cd']")))
        select_question = Select(dropdown_question)
        select_question.select_by_value("02")
        wait = WebDriverWait(driver, 60)
        input_question = wait.until(EC.presence_of_element_located((By.XPATH,  "//input[@name='secret_question_value']")))
        input_question.send_keys("abc")
        wait = WebDriverWait(driver, 60)
        click_check = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='ag_chk']")))
        click_check.click()
        wait = WebDriverWait(driver, 60)
        click_submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        click_submit.click()
        wait = WebDriverWait(driver, 60)
        click_submitForm = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@onclick,'submitForm')]")))
        click_submitForm.click()
        print("[INFO] Success Website InfoQ")
    except:
        print("[INFO] Error Website InfoQ")

def Website_Youtube(driver: webdriver):
    try:
        driver.get("https://www.youtube.com/")
        wait = WebDriverWait(driver, 60)
        input_search = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="search"]')))
        time.sleep(1)
        input_search.click()
        time.sleep(1)
        actions = ActionChains(driver)
        time.sleep(0.5)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(10)
        array = [
            "https://www.youtube.com/@bisko.adventure",
            "https://www.youtube.com/@MrBeast",
            "https://www.youtube.com/c/V%C4%83nT%C3%B9ng"
            ]
        for link in array:
            try:

                driver.get(link)
                wait = WebDriverWait(driver, 60)
                click_subscribe = wait.until(EC.presence_of_element_located((By.XPATH, "//yt-subscribe-button-view-model")))
                time.sleep(2)
                click_subscribe.click()
                time.sleep(3)
                wait = WebDriverWait(driver, 60)
                click_subscribe2 = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//yt-subscribe-button-view-model")))
                time.sleep(2)
                click_subscribe2.click()
                wait = WebDriverWait(driver, 60)
                click_allNotifi = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='radio-shape-wiz__label']")))
                time.sleep(2)
                click_allNotifi.click()
                time.sleep(5)
            except:
                None
        driver.get("https://www.youtube.com/account_notifications")
        try:
            wait = WebDriverWait(driver, 60)
            click_family = wait.until(EC.presence_of_element_located((By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[1]//ytd-settings-switch-renderer//tp-yt-paper-toggle-button")))
            time.sleep(0.5)
            click_family.click()
        except:
            None
        try:
            click_preferences1 = driver.find_element(By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[1]//tp-yt-paper-toggle-button")
            time.sleep(0.5)
            click_preferences1.click()
        except:
            None
        try:
            click_preferences2 = driver.find_element(By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[2]//tp-yt-paper-toggle-button")
            time.sleep(0.5)
            click_preferences2.click()
        except:
            None
        try:
            click_preferences3 = driver.find_element(By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[3]//tp-yt-paper-toggle-button")
            time.sleep(0.5)
            click_preferences3.click()
        except:
            None
        print("[INFO] Success Website Youtube")
    except:
        print("[INFO] Error Website Youtube")