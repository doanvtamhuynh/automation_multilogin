from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLoginSV

email = NewEmail("abc@gmail.com","123axc","email@gmail.com")
print(email)

profile = NewProfile("sadgfhgf","sadgfhj")
print(profile)

driver = MultiLoginSV.Start("username","password",profile)

