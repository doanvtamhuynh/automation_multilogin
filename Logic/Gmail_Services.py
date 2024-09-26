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
    loop = asyncio.get_running_loop()
    actions = ActionChains(driver)
    try:
        driver.get("https://mail.google.com/")

        try:
            wait = WebDriverWait(driver, 30)
            input_text = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                    (By.XPATH, "id('aso_search_form_anchor')/DIV[1]//input")))
            await asyncio.sleep(2)
            await loop.run_in_executor(None, input_text.send_keys, nameMail)
            await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
        except:
            try:
                wait = WebDriverWait(driver, 30)
                input_text = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
                    (By.XPATH, "//form[id('aso_search_form_anchor')]/div[1]//input")))
                await asyncio.sleep(2)
                await loop.run_in_executor(None, input_text.send_keys, nameMail)
                await loop.run_in_executor(None, actions.send_keys(Keys.RETURN).perform)
            except:
                print(f"[INFO] Error find read mail {nameMail}")
        wait = WebDriverWait(driver, 20)
        div_element = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
            (By.XPATH, "//div[@class='ae4 UI aZ6 id']//tr")))
        await loop.run_in_executor(None, div_element.click)

        await asyncio.sleep(10)
        wait = WebDriverWait(driver, 20)
        element_link = await loop.run_in_executor(None, wait.until, EC.presence_of_element_located(
            (By.XPATH, f"(//a[contains(@href, '{href}')])[1]")))
        link = await loop.run_in_executor(None, element_link.get_attribute, "href")
        driver.get(link)
        await asyncio.sleep(3)
        print(f"[INFO] Success read mail {nameMail}")
    except:
        print(f"[INFO] Error read mail {nameMail}")

async def ReadMail_TLDR(driver: webdriver):
    await ReadMail(driver,"TLDR","confirmed")

async def ReadMail_Envalior(driver: webdriver):
    await ReadMail(driver,"Envalior","https://email.envalior.com")

async def ReadMail_InfoQ(driver: webdriver):
    await ReadMail(driver,"infoQ","https://infoq.vn/Registers/redirectIndex")