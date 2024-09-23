from Models.ProfileMultiLogin import NewProfile as Profile
from Models.Email import NewEmail as Email
from Models.InfoAccount import NewInfo as Info
import random


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
        with open(r"G:\Code\ListFile\listPassword.txt") as file:
            lines = file.readlines()
        password = lines[random(len(lines))]
    except:
        print("[INFO] File Password empty")
        password = "duchanh456"

    try:
        with open(r"G:\Code\ListFile\listRecovery.txt") as file:
            lines = file.readlines()
        recovery = lines[random(len(lines))]
    except:
        print("[INFO] File Recovery empty")
        recovery = "milleroainum@gmail.com"

    try:
        with open(r"G:\Code\ListFile\listHo.txt") as file:
            lines = file.readlines()
        ho = lines[random(len(lines))]
    except:
        print("[INFO] File Ho empty")
        ho = "Nguyen"

    try:
        with open(r"G:\Code\ListFile\listTen.txt") as file:
            lines = file.readlines()
        ten = lines[random(len(lines))]
    except:
        print("[INFO] File Ten empty")
        ten = "Nhi"

    try:
        with open(r"G:\Code\ListFile\listDiaChi.txt") as file:
            lines = file.readlines()
        index = random(2, len(lines) - 2)
        homeAddress = lines[index]
        workAddress = lines[index + 1]
    except:
        print("[INFO] File Dia chi empty")
        homeAddress = "32, Đường Nguyễn Khắc Viện, Quận 9, TP. Hồ Chí Minh"
        workAddress = "50, Đường Lò Lu, Quận 9, TP. Hồ Chí Minh"

    newInfo = Info(password, recovery, ten, ho, homeAddress, workAddress)
    return newInfo