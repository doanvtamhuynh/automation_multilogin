from Models.ProfileMultiLogin import NewProfile as Profile
from Models.Email import NewEmail as Email


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