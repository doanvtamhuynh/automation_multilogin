from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time
import Logic.OtherWebsite_Services as OtherWebsite
import Logic.ReadFile as ReadFile
import Logic.Gmail_Services as Gmail
from Logic.WriteFile import WriteInfo

ACCOUNT_USERNAME = "username"
ACCOUNT_PASSWORD = "password"

listEmail = ReadFile.GetListEmail(r"G:\Code\listEmail.txt")
if listEmail is not None:
    email = listEmail[0]
#email = NewEmail("email@gmail.com","password","recovery@gmail.com")

listProfile = ReadFile.GetListProfile(r"G:\Code\listProfile.txt")
if listProfile is not None:
    profile = listProfile[0]
#profile = NewProfile("profile_id", "folder_id")

newInfoAccount = ReadFile.GetInfoAccount()

listWordTranslate = ["hello", "thanks", "good"]
listWordAlert = ["usa", "car", "football"]

WriteInfo(email, newInfoAccount, r"G:\Code\ListFile\newEmail.txt")
print(email)
print(profile)
print(newInfoAccount)

driver = MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)
if driver is not None:

    resultLogin = Google.GG_Login(driver, email)
    time.sleep(1)

    if resultLogin is True:
        # Google Services
        Google.Change_Info(driver, newInfoAccount)
        Google.GG_Translate(driver, listWordTranslate)
        time.sleep(1)
        Google.GG_ALert(driver, listWordAlert)
        time.sleep(1)

        #Sign In Other Website
        OtherWebsite.Website_TLDR(driver, email)
        time.sleep(1)
        OtherWebsite.Website_Envalior(driver, email)
        time.sleep(1)
        OtherWebsite.Website_InfoQ(driver, email)
        time.sleep(1)
        OtherWebsite.Website_Dictionary(driver, email)
        time.sleep(1)
        OtherWebsite.Website_Quora(driver)
        time.sleep(1)
        OtherWebsite.Website_ITViec(driver)
        time.sleep(1)
        OtherWebsite.Website_Batdongsan(driver)
        time.sleep(1)
        OtherWebsite.Website_Foxnews(driver, email)
        time.sleep(1)

        #Read Mail
        Gmail.ReadMail_TLDR(driver)
        time.sleep(1)
        Gmail.ReadMail_Envalior(driver)
        time.sleep(1)
        Gmail.ReadMail_InfoQ(driver)

    time.sleep(5)
    MultiLogin.Stop(profile)