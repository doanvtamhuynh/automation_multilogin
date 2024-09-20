from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time
import Logic.OtherWebsite_Services as OtherWebsite

ACCOUNT_USERNAME = "username"
ACCOUNT_PASSWORD = "password"
email = NewEmail("email@gmail.com","password","recovery@gmail.com")
profile = NewProfile("profile_id","folder_id")
listWord = ["hello","thanks","good"]
print(email)
print(profile)

driver = MultiLogin.Start(ACCOUNT_USERNAME,ACCOUNT_PASSWORD,profile)
if driver is not None:

    Google.GG_Login(driver,email)
    time.sleep(1)
    Google.GG_Translate(driver, listWord)
    time.sleep(1)
    Google.GG_ALert(driver, listWord)
    time.sleep(1)
    OtherWebsite.Website_TLDR(driver, email)
    time.sleep(1)
    OtherWebsite.Website_Dictionary(driver, email)
    time.sleep(1)
    OtherWebsite.Website_Quora(driver)
    time.sleep(1)
    OtherWebsite.Website_ITViec(driver)
    time.sleep(1)
    OtherWebsite.Website_Batdongsan(driver)
    time.sleep(1)
    OtherWebsite.Website_Envalior(driver, email)
    time.sleep(1)
    OtherWebsite.Website_Foxnews(driver, email)

    time.sleep(1000)
    MultiLogin.Stop(profile)