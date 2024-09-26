from Models.InfoAccount import NewInfo as Info
from Models.Email import NewEmail as Email

def WriteInfo(email: Email, src: str) -> bool:
    try:
        with open(src, "a") as file:
            file.write(f"{email.email}|{email.password}|{email.recovery}\n")
        print("[INFO] Wrote new email")
        return True
    except:
        print("[INFO] Cannot write new email")
        return False
