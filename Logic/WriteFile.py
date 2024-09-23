from Models.InfoAccount import NewInfo as Info
from Models.Email import NewEmail as Email

def WriteInfo(email: Email, newInfo: Info, src: str) -> bool:
    try:
        with open(src, "a") as file:
            file.write(f"{email.email}|{newInfo.password}|{newInfo.recovery}")
    except:
        print("[INFO] Cannot write new email")
        return False
    finally:
        print("[INFO] Wrote new email")
        return True