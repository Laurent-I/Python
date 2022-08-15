import time
from datetime import datetime as dt

hosts_path = 'C:\\Python\\driver\\etc'

redirect_path = '127.0.0.1'

website_list = ['www.youtube.com', 'www.gmail.com']

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 8 < dt.now().year, dt.now().month, dt.now().day, 8):
        print('Working HOURS')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_path + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun HOURS')
    time.sleep(5)

    