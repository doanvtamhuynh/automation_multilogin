from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
import time

def Website_TLDR(driver: webdriver, email: NewEmail):
    try:
        driver.get("https://tldr.tech/")
        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        input_email.send_keys(email.email)
        click_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        click_submit.click()

        wait = WebDriverWait(driver, 60)
        click_save1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        click_save1.click()

        wait = WebDriverWait(driver, 60)
        click_save2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        click_save2.click()

        wait = WebDriverWait(driver, 60)
        click_save3 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        click_save3.click()

        wait = WebDriverWait(driver, 60)
        input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='company_website']")))
        input_text.send_keys("skyboss.com")

        wait = WebDriverWait(driver, 60)
        click_submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        click_submit.click()

    except:
        print("[INFO] Error Website https://tldr.tech/")