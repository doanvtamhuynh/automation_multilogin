from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time

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
    Google.GG_Translate(driver, listWord)

    time.sleep(1000)
    MultiLogin.Stop(profile)