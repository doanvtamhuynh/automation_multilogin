from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
import time

def ReadMail_TLDR(driver: webdriver):
    driver.get("https://mail.google.com/")

    try:
        wait = WebDriverWait(driver, 60)
        input_text = wait.until(EC.presence_of_element_located((By.XPATH, "id('aso_search_form_anchor')/DIV[1]//input")))
        input_text.send_keys("TLDR")
        driver.send_keys(Keys.ENTER)
    except:
        try:
            wait = WebDriverWait(driver, 60)
            input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//form[id('aso_search_form_anchor')]/div[1]//input")))
            input_text.send_keys("TLDR")
            driver.send_keys(Keys.ENTER)
        except:
            print("[INFO] Error read mail TLDR")
