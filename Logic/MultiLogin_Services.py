import requests
import hashlib
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from Models.ProfileMultiLogin import NewProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions

MLX_BASE = "https://api.multilogin.com"
MLX_LAUNCHER = "https://launcher.mlx.yt:45001/api/v1"
MLX_LAUNCHER_V2 = (
    "https://launcher.mlx.yt:45001/api/v2"
)
LOCALHOST = "http://127.0.0.1"
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

def signin(username: str, password: str) -> str:
    payload = {
        "email": username,
        "password": hashlib.md5(password.encode()).hexdigest(),
    }
    r = requests.post(f"{MLX_BASE}/user/signin", json=payload)
    if r.status_code != 200:
        print(f"\n[INFO] Error during login: {r.text}\n")
    else:
        response = r.json()["data"]
        token = response["token"]
        return token
    return None

def Start(username: str, password: str, profile: NewProfile) -> webdriver:
    try:
        token = signin(username,password)
        if token is not None:
            HEADERS.update({"Authorization": f"Bearer {token}"})
            r = requests.get(
                f"{MLX_LAUNCHER_V2}/profile/f/{profile.folderID}/p/{profile.profileID}/start?automation_type=selenium",
                headers=HEADERS,
            )
            response = r.json()
            if r.status_code != 200:
                print(f"\n[INFO] Error while starting profile: {r.text}\n")
            else:
                print(f"\n[INFO] Profile {profile.profileID} started.\n")
            selenium_port = response["data"]["port"]
            driver = webdriver.Remote(
                command_executor=f"{LOCALHOST}:{selenium_port}", options=ChromiumOptions()
            )
            return driver
        return None
    except:
        token = signin(username, password)
        if token is not None:
            HEADERS.update({"Authorization": f"Bearer {token}"})
            r = requests.get(
                f"{MLX_LAUNCHER_V2}/profile/f/{profile.folderID}/p/{profile.profileID}/start?automation_type=selenium",
                headers=HEADERS,
            )
            response = r.json()
            if r.status_code != 200:
                print(f"\n[INFO] Error while starting profile: {r.text}\n")
            else:
                print(f"\n[INFO] Profile {profile.profileID} started.\n")
            selenium_port = response["data"]["port"]

            driver = webdriver.Remote(
                command_executor=f"{LOCALHOST}:{selenium_port}",
                options= FirefoxOptions()
            )
            return driver
        return None

def Stop(profile: NewProfile) -> None:
    r = requests.get(f"{MLX_LAUNCHER}/profile/stop/p/{profile.profileID}", headers=HEADERS)
    if r.status_code != 200:
        print(f"\n[INFO] Error while stopping profile: {r.text}\n")
    else:
        print(f"\n[INFO] Profile {profile.profileID} stopped.\n")