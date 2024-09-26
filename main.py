from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time
import Logic.OtherWebsite_Services as OtherWebsite
import Logic.ReadFile as ReadFile
import Logic.Gmail_Services as Gmail
from Logic.WriteFile import WriteInfo
import os
import threading
import asyncio

ACCOUNT = ReadFile.GetUsernamePassword()
ACCOUNT_USERNAME = ACCOUNT[0]
ACCOUNT_PASSWORD = ACCOUNT[1]

print(ACCOUNT_PASSWORD)
print(ACCOUNT_USERNAME)

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

listEmail = ReadFile.GetListEmail(rf"{src}\listEmail.txt")

listProfile = ReadFile.GetListProfile(rf"{src}\listProfile.txt")

listWordTranslate = ["hello", "thanks", "good"]
listWordAlert = ["usa", "car", "football"]

async def task(email: NewEmail, profile: NewProfile):
    print(email)
    print(profile)

    driver = await MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)

    if driver is not None:

        resultLogin = await Google.GG_Login(driver, email)
        await asyncio.sleep(2)

        if resultLogin is True:

            await Google.GG_Translate(driver, listWordTranslate)
            await asyncio.sleep(2)
            await Google.GG_ALert(driver, listWordAlert)
            await asyncio.sleep(2)

            #Sign In Other Website
            await OtherWebsite.Website_Youtube(driver)
            await asyncio.sleep(2)
            await OtherWebsite.Website_TLDR(driver, email)
            await asyncio.sleep(2)
            await OtherWebsite.Website_Envalior(driver, email)
            await asyncio.sleep(2)
            await OtherWebsite.Website_InfoQ(driver, email)
            await asyncio.sleep(2)
            await OtherWebsite.Website_Dictionary(driver, email)
            await asyncio.sleep(2)
            await OtherWebsite.Website_Quora(driver)
            await asyncio.sleep(2)
            await OtherWebsite.Website_ITViec(driver)
            await asyncio.sleep(2)
            await OtherWebsite.Website_Foxnews(driver, email)
            await asyncio.sleep(2)

            #Read Mail
            await Gmail.ReadMail_TLDR(driver)
            await asyncio.sleep(2)
            await Gmail.ReadMail_Envalior(driver)
            await asyncio.sleep(2)
            await Gmail.ReadMail_InfoQ(driver)

            await OtherWebsite.Website_Batdongsan(driver)
            await asyncio.sleep(2)

            # Create info
            newInfoAccount = await ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            await Google.Change_Info(driver, newInfoAccount)
            WriteInfo(email, newInfoAccount, rf"{src}\newEmail.txt")

            #Log out
            await Google.Logout_Devices(driver)

        if driver:
            await asyncio.sleep(5)
            await MultiLogin.Stop(profile)


async def main():
    tasks = []
    for i in range(len(listProfile)):
        tasks.append(task(listEmail[i], listProfile[i]))

    await asyncio.gather(*tasks)

asyncio.run(main())