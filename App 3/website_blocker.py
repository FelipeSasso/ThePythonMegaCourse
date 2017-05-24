import time
from datetime import datetime as dt

host_temp="hosts"
host_path="/etc/hosts"
redirects="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        # print("Vai trabalhar")
        with open(host_path, 'r+') as file:
            content=file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirects + " " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
