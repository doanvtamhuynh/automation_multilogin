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


    driver = MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)
    if driver is not None:

        resultLogin = Google.GG_Login(driver, email)
        await asyncio.sleep(2)

        if resultLogin is True:

            Google.GG_Translate(driver, listWordTranslate)
            await asyncio.sleep(2)
            Google.GG_ALert(driver, listWordAlert)
            await asyncio.sleep(2)

            #Sign In Other Website
            OtherWebsite.Website_Youtube(driver)
            await asyncio.sleep(2)
            OtherWebsite.Website_TLDR(driver, email)
            await asyncio.sleep(2)
            OtherWebsite.Website_Envalior(driver, email)
            await asyncio.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            await asyncio.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            await asyncio.sleep(2)
            OtherWebsite.Website_Quora(driver)
            await asyncio.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            await asyncio.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            await asyncio.sleep(2)

            #Read Mail
            Gmail.ReadMail_TLDR(driver)
            await asyncio.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            await asyncio.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            await asyncio.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            Google.Change_Info(driver, newInfoAccount)
            WriteInfo(email, newInfoAccount, rf"{src}\newEmail.txt")

        await asyncio.sleep(5)
        MultiLogin.Stop(profile)


async def main():
    tasks = []
    for i in range(len(listProfile) - 1):
        tasks.append(task(listEmail[i], listProfile[i]))

    await asyncio.gather(*tasks)

asyncio.run(main())

