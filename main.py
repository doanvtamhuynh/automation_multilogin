from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google

email = NewEmail("email@gmail.com","123axc","recovery@gmail.com")
print(email)

profile = NewProfile("profile_id","folder_id")
print(profile)

driver = MultiLogin.Start("username","password",profile)

Google.Login_GG(driver,email)
