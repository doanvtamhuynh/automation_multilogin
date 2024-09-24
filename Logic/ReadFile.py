from Models.ProfileMultiLogin import NewProfile as Profile
from Models.Email import NewEmail as Email
from Models.InfoAccount import NewInfo as Info
import random
import os

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

def GetListEmail(src: str) -> list:
    result = False
    listEmail = []
    try:
        with open(f"{src}", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Email empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        for line in lines:
            line.strip()
            detail_Line = line.split("|")
            new_Email = Email(detail_Line[0],detail_Line[1],detail_Line[2])
            listEmail.append(new_Email)
    return listEmail

def GetListProfile(src: str) -> list:
    result = False
    listProfile = []
    try:
        with open(f"{src}", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Email empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        for line in lines:
            line.strip()
            detail_Line = line.split("|")
            new_Profile = Profile(detail_Line[0],detail_Line[1])
            listProfile.append(new_Profile)
    return listProfile

def GetInfoAccount() -> Info:
    try:
        with open(rf"{src}\listPassword.txt", 'r') as file:
            listPass = file.readlines()
        index = random.randint(0, len(listPass) - 1)
        password = listPass[index]
        password = password.replace("\n","")
    except:
        print("[INFO] File Password empty")
        password = "duchanh456"

    try:
        with open(rf"{src}\listRecovery.txt", "r") as file:
            listRecovery = file.readlines()
        index = random.randint(0, len(listRecovery) - 1)
        recovery = listRecovery[index]
        recovery = recovery.replace("\n", "")
    except:
        print("[INFO] File Recovery empty")
        recovery = "milleroainum@gmail.com"

    try:
        with open(rf"{src}\listHo.txt", "r", encoding='utf-8') as file:
            listHo = file.readlines()
        index = random.randint(0, len(listHo) - 1)
        ho = listHo[index]
        ho = ho.replace("\n", "")
    except:
        print("[INFO] File Ho empty")
        ho = "Nguyen"

    try:
        with open(rf"{src}\listTen.txt", "r", encoding='utf-8') as file:
            listTen = file.readlines()
        index = random.randint(0, len(listTen) - 1)
        ten = listTen[index]
        ten = ten.replace("\n", "")
    except:
        print("[INFO] File Ten empty")
        ten = "Nhi"

    try:
        with open(rf"{src}\listDiaChi.txt", "r", encoding='utf-8') as file:
            listDiachi = file.readlines()
        index = random.randint(2, len(listDiachi) - 2)
        homeAddress = listDiachi[index]
        homeAddress = homeAddress.replace("\n", "")
        workAddress = listDiachi[index + 1]
        workAddress = workAddress.replace("\n", "")
    except:
        print("[INFO] File Dia chi empty")
        homeAddress = "32, Đường Nguyễn Khắc Viện, Quận 9, TP. Hồ Chí Minh"
        workAddress = "50, Đường Lò Lu, Quận 9, TP. Hồ Chí Minh"

    newInfo = Info(password, recovery, ten, ho, homeAddress, workAddress)
    return newInfo

def GetUsernamePassword() -> list:
    result = False
    try:
        with open(rf"{src}\username_password.txt", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Username and Password empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        lines[0].strip()
        detail_Line = lines[0].split("|")
        listUsernamePassword = [detail_Line[0], detail_Line[1]]
        return listUsernamePassword
    else:
        return None


