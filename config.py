from selenium import webdriver
import platform
from os import getenv, path, getcwd
from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

LOGIN_USER_EMAIL = getenv("LOGIN_USER_EMAIL")
LOGIN_USER_PASSWORD = getenv("LOGIN_USER_PASSWORD")
FIFA_FUT_URL = "https://www.ea.com/pl-pl/fifa/ultimate-team/web-app/"
EA_EMAIL = "EA@e.ea.com"

INCREASE_COUNT = 20
LOGIN_MANUALLY = False


def create_driver():
    system = platform.system()

    if system == "Darwin":
        path = f"{basedir}/chrome_mac/chromedriver"
    elif system == "Linux":
        path = f"{basedir}/chrome_linux/chromedriver"
    elif system == "Windows":
        path = f"{basedir}/chrome_windows/chromedriver.exe"
    else:
        raise OSError(f"Operating system {system} is not supported")

    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()

    return driver


PLAYER = {
    "name": "messi",
    "cost": 1500,
}


# Credentials - fill in if LOGIN_MANUALLY is False
USER = {
    "email": LOGIN_USER_EMAIL,
    "password": LOGIN_USER_PASSWORD,
}

EMAIL_CREDENTIALS = {
    "email": LOGIN_USER_EMAIL,
    "password": LOGIN_USER_PASSWORD,
}
