import os
import sys
import time
from time import sleep


try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    request = requests.get("https://www.google.com/search?q=Manish+Singh", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'


def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)


print('')
print(G + ' Launching Anonymouse Email ')
sleep(2)
print('')
to = input(G + " Send Mail To" + C + " : " + Y)
print('')
subject = input(G + " Input Mail Subject" + C + " : " + Y)
print("")
msg = input(G + " Input Mail Content" + C + " : " + Y)
print("")
usagnt = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
sess = requests.Session()
rth = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
    'Host': 'anonymouse.org',
    'User-Agent': usagnt,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://anonymouse.org/anonemail.html',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded'
}, data={
    'to': to,
    'subject': subject,
    'text': msg
})

if '200' in rth.text:
    print(G + " Sending Email >>>>>>>>>>")
else:
    print(G + " Sending Email >>>>>>>>>>")
    print('')
    time.sleep(2)
    print(C + " Mail Successfully Sent !!")
    print('')
    sleep(3)
    print(W + " Please wait! This process can take some time. ")
    print('')
