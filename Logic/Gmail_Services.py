from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
import time

def ReadMail(driver: webdriver, nameMail: str, href: str):
    try:
        find_email = False
        driver.get("https://mail.google.com/")

        try:
            wait = WebDriverWait(driver, 60)
            input_text = wait.until(EC.presence_of_element_located((By.XPATH, "id('aso_search_form_anchor')/DIV[1]//input")))
            time.sleep(2)
            input_text.send_keys(f"{nameMail}")
            driver.send_keys(Keys.ENTER)
            find_email = True
        except:
            try:
                wait = WebDriverWait(driver, 60)
                input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//form[id('aso_search_form_anchor')]/div[1]//input")))
                time.sleep(2)
                input_text.send_keys(f"{nameMail}")
                driver.send_keys(Keys.ENTER)
                find_email = True
            except:
                print(f"[INFO] Error read mail {nameMail}")
        if find_email is True:
            div_element = driver.find_element(By.CSS_SELECTOR, ".ae4.UI.aZ6")
            tr_element = div_element.find_element(By.CSS_SELECTOR, "table tbody tr")
            time.sleep(2)
            tr_element.click()

            wait = WebDriverWait(driver, 60)
            element_link = wait.until(EC.presence_of_element_located((By.XPATH, f"(//a[contains(@href, '{href}')])[1]")))
            link = element_link.get_attribute("href")

            driver.get(link)
    except:
        print(f"[INFO] Error read mail {nameMail}")

def ReadMail_TLDR(driver: webdriver):
    ReadMail(driver,"TLDR","https://click.pstmrk.it/3s/tldr.tech")

def ReadMail_Envalior(driver: webdriver):
    ReadMail(driver,"Envalior","https://email.envalior.com")