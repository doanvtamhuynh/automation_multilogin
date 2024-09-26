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
import asyncio


async def Website_TLDR(driver: webdriver, email: NewEmail):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://tldr.tech/")

        wait = WebDriverWait(driver, 60)
        input_email = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_email.send_keys, email.email)
        click_submit = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//button[@type='submit']")
        await asyncio.sleep(2)
        await loop.run_in_executor(None, click_submit.click)

        try:
            wait = WebDriverWait(driver, 10)
            btn_click_here = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@class='underline']")))
            await asyncio.sleep(1)
            await loop.run_in_executor(None, btn_click_here.click)
        except:
            print("")

        await asyncio.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save1 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_save1.click)

        await asyncio.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save2 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_save2.click)

        await asyncio.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_save3 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_save3.click)


        await asyncio.sleep(2)
        wait = WebDriverWait(driver, 60)
        input_text = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='company_website']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_text.send_keys, "skyboss.com")

        await asyncio.sleep(2)
        wait = WebDriverWait(driver, 60)
        btn_submit = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_submit.click)

        print("[INFO] Success Website https://tldr.tech/")
    except:
        print("[INFO] Error Website https://tldr.tech/")

async def Website_Envalior(driver: webdriver, email: NewEmail):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://www.envalior.com/")

        wait = WebDriverWait(driver, 60)
        input_email = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_email.send_keys, email.email)

        btn_checkbox = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//input[@type='checkbox']")
        await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();", btn_checkbox)

        try:
            btn_submit = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//button[@type='SUBMIT']")
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();", btn_submit)
        except:
            btn_submit = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//button[@type='submit']")
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();", btn_submit)
        await asyncio.sleep(10)
        print("[INFO] Success Website https://www.envalior.com/")
    except:
        print("[INFO] Error Website https://www.envalior.com/")

async def Website_Foxnews(driver: webdriver, email: NewEmail):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://www.foxnews.com/newsletters")

        wait = WebDriverWait(driver, 60)
        btn_subcribe = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//div[@class='button subscribe'])[1]//a")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_subcribe.click)
        await asyncio.sleep(2)

        actions = ActionChains(driver)

        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await asyncio.sleep(1)
        wait = WebDriverWait(driver, 60)
        input_question = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        await loop.run_in_executor(None, input_question.send_keys, email.email)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await asyncio.sleep(1)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(5)

        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)

        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)

        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.TAB).perform)
        await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        await asyncio.sleep(2)
        print("[INFO] Success Website https://www.foxnews.com/newsletters")
    except:
        print("[INFO] Error Website https://www.foxnews.com/newsletters")

async def Website_Batdongsan(driver: webdriver):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://batdongsan.com.vn/sellernet/trang-dang-nhap")
        wait = WebDriverWait(driver, 60)
        main_window = await driver.current_window_handle
        btn_LoginGG = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@data-tracking-label='type=Google']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_LoginGG.click)
        await asyncio.sleep(2)
        windows = await driver.window_handles
        result_signin = False
        try:
            for window in windows:
                if window != main_window:
                    driver.switch_to.window(window)
                    await asyncio.sleep(2)
                    result_signin = await Google.Login_Third_Website(driver)
                    await asyncio.sleep(2)
                    break
            await driver.switch_to.window(main_window)
        except:
            print("[INFO] Error Login with Google")

        await asyncio.sleep(10)
        if result_signin is True:
            driver.get("https://batdongsan.com.vn/nha-dat-ban-ha-noi")
            wait = WebDriverWait(driver, 60)
            btn_bell = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//i[@class='re__icon-switch-off--lg js__save-alert-v3-switch-icon']/span")))
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_bell)

            await asyncio.sleep(10)
            wait = WebDriverWait(driver, 60)
            btn_Submit = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@tracking-id='click-save-search-alert-option1']")))
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Submit)
            print("[INFO] Success Website Bat Dong San")
        else:
            print("[INFO] Error Website Bat Dong San")
    except:
        print("[INFO] Error Website Bat Dong San")

async def Website_Dictionary(driver: webdriver, email: NewEmail):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://www.dictionary.com/")

        wait = WebDriverWait(driver, 120)
        input_email = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_email.send_keys, email.email)

        btn_submit = await loop.run_in_executor(None, driver.find_element, By.XPATH, "(//button[@type='submit'])[2]")
        await asyncio.sleep(2)
        btn_submit.click()
        print("[INFO] Success Website Dictionary")
    except:
        print("[INFO] Error Website Dictionary")

async def Website_ITViec(driver: webdriver):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://itviec.com/sign_in")

        wait = WebDriverWait(driver, 60)
        btn_LoginGG = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'])[1]")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, btn_LoginGG.click)
        result_signin = await Google.Login_Third_Website(driver)
        await asyncio.sleep(5)

        if result_signin is True:
            wait = WebDriverWait(driver, 30)
            btn_Next = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[1]")))
            await asyncio.sleep(2)
            await loop.run_in_executor(None, btn_Next.click)

            wait = WebDriverWait(driver, 30)
            btn_Select_Java = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//label[@for='skill_java']")))
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Select_Java)
            btn_Select_ReactJs = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//label[@for='skill_reactjs']")
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Select_ReactJs)
            btn_Select_DotNet = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//label[@for='skill_net']")
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Select_DotNet)
            btn_Select_HCM = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//label[@for='city_ho-chi-minh-hcm']")
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Select_HCM)
            wait = WebDriverWait(driver, 30)
            btn_Subcribe = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@data-jr-onboarding-target='buttonSubmit']")))
            await asyncio.sleep(2)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Subcribe)
        print("[INFO] Success website ITViec")
    except:
        print("[INFO] Error website ITViec")


async def Website_Quora(driver: webdriver):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://humanity.quora.com")

        wait = WebDriverWait(driver, 60)
        btn_SignIn = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'qu-ml--medium')]")))
        await asyncio.sleep(2)
        await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();", btn_SignIn)

        wait = WebDriverWait(driver, 60)
        btn_Continue = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'puppeteer_test_login_button_google')]")))
        await asyncio.sleep(2)
        await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();", btn_Continue)

        result_signin = await Google.Login_Third_Website(driver)
        await asyncio.sleep(2)

        if result_signin is True:
            try:
                wait = WebDriverWait(driver, 60)
                btn_Follow = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'qu-bg--tribe_theme_blue')]")))
                await asyncio.sleep(2)
                try:
                    await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                                   btn_Follow)
                except:
                    await loop.run_in_executor(None, btn_Follow.click)

                wait = WebDriverWait(driver, 60)
                btn_Bell = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "id('notitifications')")))
                await asyncio.sleep(2)
                try:
                    await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                                   btn_Bell)
                except:
                    await loop.run_in_executor(None, btn_Bell.click)

                try:
                    wait = WebDriverWait(driver, 60)
                    checkbox_AllPost = await loop.run_in_executor(None, wait.until,
                                                            EC.presence_of_element_located((By.XPATH, "//input[@value='all_notifs']")))
                    await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                                   checkbox_AllPost)
                except:
                    None

                try:
                    wait = WebDriverWait(driver, 60)
                    btn_Email = await loop.run_in_executor(None, wait.until,
                                                                  EC.presence_of_element_located(
                                                                      (By.XPATH, "//input[@aria-checked='false' and @type='checkbox']")))
                    await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                                   btn_Email)
                except:
                    None
            except:
                None

            driver.get("https://www.quora.com/settings/notifications")
            wait = WebDriverWait(driver, 60)
            btn_Daily = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='NotifSettingsRadioButtonsItem' and @value='2']")))
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].scrollIntoView(true);",
                                                           btn_Daily)
            await asyncio.get_event_loop().run_in_executor(None, driver.execute_script, "arguments[0].click();",
                                                           btn_Daily)

        print("[INFO] Success website Quora")
    except:
        print("[INFO] Error website Quora")

async def Website_InfoQ(driver: webdriver, email: NewEmail):
    loop = asyncio.get_running_loop()
    try:
        driver.get("https://infoq.vn/Registers/index")
        wait = WebDriverWait(driver, 60)
        input_surname = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='first_name']")))
        await asyncio.sleep(2)
        await loop.run_in_executor(None, input_surname.send_keys, "Harry")

        wait = WebDriverWait(driver, 60)
        input_lastname = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='last_name']")))
        await loop.run_in_executor(None, input_lastname.send_keys, "Potter")

        wait = WebDriverWait(driver, 60)
        input_email1 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='email01']")))
        await loop.run_in_executor(None, input_email1.send_keys, email.email)

        wait = WebDriverWait(driver, 60)
        input_email2 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='email02']")))
        await loop.run_in_executor(None, input_email2.send_keys, email.email)

        wait = WebDriverWait(driver, 60)
        input_password1 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='pass01']")))
        await loop.run_in_executor(None, input_password1.send_keys, "Duchanh456@")

        wait = WebDriverWait(driver, 60)
        input_password2 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='pass02']")))
        await loop.run_in_executor(None, input_password2.send_keys, "Duchanh456@")

        random_number = random.randint(10000000, 99999999)
        phone_number = f"09{random_number}"
        wait = WebDriverWait(driver, 60)
        input_phonenumber = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='phone_num1']")))
        await loop.run_in_executor(None, input_phonenumber.send_keys, phone_number)

        wait = WebDriverWait(driver, 60)
        input_birth = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='birthday']")))
        await loop.run_in_executor(None, input_birth.send_keys, "14/03/1999")

        wait = WebDriverWait(driver, 60)
        click_gender = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@id='gt_1']")))
        await loop.run_in_executor(None, click_gender.click)

        wait = WebDriverWait(driver, 60)
        dropdown_province = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//select[@name='city_cd']")))
        select_province = await loop.run_in_executor(None, Select, dropdown_province)
        await loop.run_in_executor(None, select_province.select_by_value, "02")

        wait = WebDriverWait(driver, 60)
        input_district = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='district']")))
        await loop.run_in_executor(None, input_district.send_keys, "abc")

        wait = WebDriverWait(driver, 60)
        input_village = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='village']")))
        await loop.run_in_executor(None, input_village.send_keys, "abc")

        wait = WebDriverWait(driver, 60)
        input_address = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='address']")))
        await loop.run_in_executor(None, input_address.send_keys, "abc")

        wait = WebDriverWait(driver, 60)
        dropdown_question = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//select[@name='secret_question_cd']")))
        select_question = await loop.run_in_executor(None, Select, dropdown_question)
        await loop.run_in_executor(None, select_question.select_by_value, "02")

        wait = WebDriverWait(driver, 60)
        input_question = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH,  "//input[@name='secret_question_value']")))
        await loop.run_in_executor(None, input_question.send_keys, "abc")

        wait = WebDriverWait(driver, 60)
        click_check = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//input[@name='ag_chk']")))
        await loop.run_in_executor(None, click_check.click)

        wait = WebDriverWait(driver, 60)
        click_submit = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        await loop.run_in_executor(None, click_submit.click)

        wait = WebDriverWait(driver, 60)
        click_submitForm = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@onclick,'submitForm')]")))
        await loop.run_in_executor(None, click_submitForm.click)

        print("[INFO] Success Website https://infoq.vn/Registers/index")
    except:
        print("[INFO] Error Website https://infoq.vn/Registers/index")

async def Website_Youtube(driver: webdriver):
    loop = asyncio.get_running_loop()
    try:
        array = [
            "https://www.youtube.com/@bisko.adventure",
            "https://www.youtube.com/@MrBeast",
            "https://www.youtube.com/c/V%C4%83nT%C3%B9ng"
            ]
        for link in array:
            try:
                driver.get(link)
                wait = WebDriverWait(driver, 60)
                click_subscribe = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//yt-subscribe-button-view-model")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, click_subscribe.click)
                await asyncio.sleep(3)

                wait = WebDriverWait(driver, 60)
                click_subscribe2 = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//yt-subscribe-button-view-model")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, click_subscribe2.click)
                wait = WebDriverWait(driver, 60)
                click_allNotifi = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((
                                            By.XPATH, "//div[@class='radio-shape-wiz__label']")))

                await asyncio.sleep(2)
                await loop.run_in_executor(None, click_allNotifi.click)
                await asyncio.sleep(5)
            except:
                None
        driver.get("https://www.youtube.com/account_notifications")
        try:
            wait = WebDriverWait(driver, 60)
            click_family = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located((By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[1]//ytd-settings-switch-renderer//tp-yt-paper-toggle-button")))
            await loop.run_in_executor(None, click_family.click)
        except:
            None
        try:
            click_preferences1 = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[1]//tp-yt-paper-toggle-button")
            await loop.run_in_executor(None, click_preferences1.click)
        except:
            None
        try:
            click_preferences2 = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[2]//tp-yt-paper-toggle-button")
            await loop.run_in_executor(None, click_preferences2.click)

        except:
            None
        try:
            click_preferences3 = await loop.run_in_executor(None, driver.find_element, By.XPATH, "//ytd-item-section-renderer[3]//ytd-settings-options-renderer[3]//ytd-settings-switch-renderer[3]//tp-yt-paper-toggle-button")
            await loop.run_in_executor(None, click_preferences3.click)
        except:
            None
        print("[INFO] Success subscribe youtube")
    except:
        print("[INFO] Error Website youtube")