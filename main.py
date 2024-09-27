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
import argparse
def main(index_profile: int, index_start = None, single = None):

    ACCOUNT = ReadFile.GetUsernamePassword()
    ACCOUNT_USERNAME = ACCOUNT[0]
    ACCOUNT_PASSWORD = ACCOUNT[1]

    print(ACCOUNT_PASSWORD)
    print(ACCOUNT_USERNAME)

    root_dir = os.getcwd()
    src = rf"{root_dir}\ListFile"

    listEmail = ReadFile.GetListEmail(rf"{src}\listEmail.txt")
    if listEmail is not None:
        email = listEmail[index_profile - 1]

    listProfile = ReadFile.GetListProfile(rf"{src}\listProfile.txt")
    if listProfile is not None:
        profile = listProfile[index_profile - 1]

    listWordTranslate = ["hello", "thanks", "good"]
    listWordAlert = ["usa", "car", "football"]

    print(email)
    print(profile)

    driver = MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)
    if driver is not None:
        driver.maximize_window()
        if index_start is None and single is None:
            resultLogin = Google.GG_Login(driver, email)
            time.sleep(1)

            if resultLogin is True:

                Google.GG_Translate(driver, listWordTranslate)
                time.sleep(2)
                Google.GG_ALert(driver, listWordAlert)
                time.sleep(2)

                #Sign In Other Website
                OtherWebsite.Website_Youtube(driver)
                time.sleep(2)
                OtherWebsite.Website_TLDR(driver, email)
                time.sleep(2)
                OtherWebsite.Website_Envalior(driver, email)
                time.sleep(2)
                OtherWebsite.Website_InfoQ(driver, email)
                time.sleep(2)
                OtherWebsite.Website_Dictionary(driver, email)
                time.sleep(2)
                OtherWebsite.Website_Quora(driver)
                time.sleep(2)
                OtherWebsite.Website_ITViec(driver)
                time.sleep(2)
                OtherWebsite.Website_Foxnews(driver, email)
                time.sleep(2)

                #Read Mail
                Gmail.ReadMail_TLDR(driver)
                time.sleep(2)
                Gmail.ReadMail_Envalior(driver)
                time.sleep(2)
                Gmail.ReadMail_InfoQ(driver)

                OtherWebsite.Website_Batdongsan(driver)
                time.sleep(2)

                # Create info
                newInfoAccount = ReadFile.GetInfoAccount()
                print(newInfoAccount)

                # Google Services
                email = Google.Change_Info(driver, newInfoAccount, email)
                WriteInfo(email, rf"{src}\newEmail.txt")

                #Log out
                Google.Logout_Devices(driver)

        elif index_start == 'gg_dich' and single is None:
            Google.GG_Translate(driver, listWordTranslate)
            time.sleep(2)
            Google.GG_ALert(driver, listWordAlert)
            time.sleep(2)

            # Sign In Other Website
            OtherWebsite.Website_Youtube(driver)
            time.sleep(2)
            OtherWebsite.Website_TLDR(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'gg_alert' and single is None:
            Google.GG_ALert(driver, listWordAlert)
            time.sleep(2)

            # Sign In Other Website
            OtherWebsite.Website_Youtube(driver)
            time.sleep(2)
            OtherWebsite.Website_TLDR(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'youtube' and single is None:
            OtherWebsite.Website_Youtube(driver)
            time.sleep(2)
            OtherWebsite.Website_TLDR(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'tldr' and single is None:
            OtherWebsite.Website_TLDR(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'envalior' and single is None:
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'infoq' and single is None:
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'dictionary' and single is None:
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'quora' and single is None:
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'itviec' and single is None:
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'foxnews' and single is None:
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'read_mail' and single is None:
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'batdongsan' and single is None:
            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'change_info' and single is None:
            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'log_out' and single is None:
            Google.Logout_Devices(driver)

        elif index_start == 'gg_dich' and single == 'single':
            Google.GG_Translate(driver, listWordTranslate)
            time.sleep(2)

        elif index_start == 'gg_alert' and single == 'single':
            Google.GG_ALert(driver, listWordAlert)
            time.sleep(2)

        elif index_start == 'youtube' and single == 'single':
            OtherWebsite.Website_Youtube(driver)
            time.sleep(2)

        elif index_start == 'tldr' and single == 'single':
            OtherWebsite.Website_TLDR(driver, email)
            time.sleep(2)

        elif index_start == 'envalior' and single == 'single':
            OtherWebsite.Website_Envalior(driver, email)
            time.sleep(2)

        elif index_start == 'infoq' and single == 'single':
            OtherWebsite.Website_InfoQ(driver, email)
            time.sleep(2)

        elif index_start == 'dictionary' and single == 'single':
            OtherWebsite.Website_Dictionary(driver, email)
            time.sleep(2)
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

            # Read Mail
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)

            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

            # Log out
            Google.Logout_Devices(driver)

        elif index_start == 'quora' and single == 'single':
            OtherWebsite.Website_Quora(driver)
            time.sleep(2)

        elif index_start == 'itviec' and single == 'single':
            OtherWebsite.Website_ITViec(driver)
            time.sleep(2)

        elif index_start == 'foxnews' and single == 'single':
            OtherWebsite.Website_Foxnews(driver, email)
            time.sleep(2)

        elif index_start == 'read_mail' and single == 'single':
            Gmail.ReadMail_TLDR(driver)
            time.sleep(2)
            Gmail.ReadMail_Envalior(driver)
            time.sleep(2)
            Gmail.ReadMail_InfoQ(driver)


        elif index_start == 'batdongsan' and single == 'single':
            OtherWebsite.Website_Batdongsan(driver)
            time.sleep(2)

        elif index_start == 'change_info' and single == 'single':
            # Create info
            newInfoAccount = ReadFile.GetInfoAccount()
            print(newInfoAccount)

            # Google Services
            email = Google.Change_Info(driver, newInfoAccount, email)
            WriteInfo(email, rf"{src}\newEmail.txt")

        elif index_start == 'log_out' and single == 'single':
            Google.Logout_Devices(driver)



    time.sleep(5)
    if driver:
        MultiLogin.Stop(profile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automation')

    parser.add_argument('index_profile', type=int, help='profile index. (ex: python main.py [index_profile])')
    parser.add_argument('index_start',  nargs='?', type=str, help='start index. (ex: python main.py [index_profile] [index_start])')
    parser.add_argument('single',  nargs='?', type=str, help='start single. (ex: python main.py [index_profile] [index_start]) single')

    args = parser.parse_args()

    main(args.index_profile, args.index_start, args.single)