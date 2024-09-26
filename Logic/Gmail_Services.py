from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
import time
from selenium.webdriver.common.action_chains import ActionChains
import asyncio

async def ReadMail(driver: webdriver, nameMail: str, href: str):
    try:
        find_email = False
        driver.get("https://mail.google.com/")

        try:
            wait = WebDriverWait(driver, 60)
            input_text = wait.until(EC.presence_of_element_located((By.XPATH, "id('aso_search_form_anchor')/DIV[1]//input")))
            await asyncio.sleep(2)
            input_text.send_keys(f"{nameMail}")
            input_text.send_keys(Keys.ENTER)
            find_email = True
        except:
            try:
                wait = WebDriverWait(driver, 60)
                input_text = wait.until(EC.presence_of_element_located((By.XPATH, "//form[id('aso_search_form_anchor')]/div[1]//input")))
                await asyncio.sleep(2)
                input_text.send_keys(f"{nameMail}")
                input_text.send_keys(Keys.ENTER)
                find_email = True
            except:
                print(f"[INFO] Error find read mail {nameMail}")
        if find_email is True:
            wait = WebDriverWait(driver, 60)
            div_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ae4 UI aZ6 id']//tr")))
            div_element.click()
            await asyncio.sleep(10)
            if div_element:
                wait = WebDriverWait(driver, 60)
                element_link = wait.until(
                    EC.presence_of_element_located((By.XPATH, f"(//a[contains(@href, '{href}')])[1]")))
                link = element_link.get_attribute("href")
                driver.get(link)
                await asyncio.sleep(3)
                print(f"[INFO] Success read mail {nameMail}")
            else:
                print(f"[INFO] Error click read mail {nameMail}")
        else:
            print(f"[INFO] Error find read mail {nameMail}")
    except:
        print(f"[INFO] Error read mail {nameMail}")

async def ReadMail_TLDR(driver: webdriver):
    await ReadMail(driver,"TLDR","confirmed")

async def ReadMail_Envalior(driver: webdriver):
    await ReadMail(driver,"Envalior","https://email.envalior.com")

async def ReadMail_InfoQ(driver: webdriver):
    await ReadMail(driver,"infoQ","https://infoq.vn/Registers/redirectIndex")