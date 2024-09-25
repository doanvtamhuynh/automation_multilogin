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

ACCOUNT = ReadFile.GetUsernamePassword()
ACCOUNT_USERNAME = ACCOUNT[0]
ACCOUNT_PASSWORD = ACCOUNT[1]

print(ACCOUNT_PASSWORD)
print(ACCOUNT_USERNAME)

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

listEmail = ReadFile.GetListEmail(rf"{src}\listEmail.txt")
if listEmail is not None:
    email = listEmail[0]

listProfile = ReadFile.GetListProfile(rf"{src}\listProfile.txt")
if listProfile is not None:
    profile = listProfile[0]

listWordTranslate = ["hello", "thanks", "good"]
listWordAlert = ["usa", "car", "football"]

print(email)
print(profile)

driver = MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)
if driver is not None:

    # resultLogin = Google.GG_Login(driver, email)
    # time.sleep(1)
    resultLogin = True

    if resultLogin is True:

        # Google.GG_Translate(driver, listWordTranslate)
        # time.sleep(2)
        # Google.GG_ALert(driver, listWordAlert)
        # time.sleep(2)
        #
        # #Sign In Other Website
        # OtherWebsite.Website_Youtube(driver)
        # time.sleep(2)
        # OtherWebsite.Website_TLDR(driver, email)
        # time.sleep(2)
        # OtherWebsite.Website_Envalior(driver, email)
        # time.sleep(2)
        # OtherWebsite.Website_InfoQ(driver, email)
        # time.sleep(2)
        # OtherWebsite.Website_Dictionary(driver, email)
        # time.sleep(2)
        # OtherWebsite.Website_Quora(driver)
        # time.sleep(2)
        # OtherWebsite.Website_ITViec(driver)
        # time.sleep(2)
        # OtherWebsite.Website_Foxnews(driver, email)
        # time.sleep(2)
        #
        # #Read Mail
        # Gmail.ReadMail_TLDR(driver)
        # time.sleep(2)
        # Gmail.ReadMail_Envalior(driver)
        # time.sleep(2)
        # Gmail.ReadMail_InfoQ(driver)
        #
        # OtherWebsite.Website_Batdongsan(driver)
        # time.sleep(2)
        #
        # # Create info
        # newInfoAccount = ReadFile.GetInfoAccount()
        # print(newInfoAccount)
        #
        # # Google Services
        # Google.Change_Info(driver, newInfoAccount)
        # WriteInfo(email, newInfoAccount, rf"{src}\newEmail.txt")

        #Log out
        Google.Logout_Devices(driver)
    time.sleep(5)
    if driver:
        MultiLogin.Stop(profile)