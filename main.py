from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time

email = NewEmail("email@gmail.com","123axc","recovery@gmail.com")
profile = NewProfile("profile_id","folder_id")
list = ["hello","thanks","good"]

driver = MultiLogin.Start("username","password",profile)

Google.GG_Login(driver,email)
Google.GG_Translate(driver, list)

time.sleep(1000)
MultiLogin.Stop(profile)