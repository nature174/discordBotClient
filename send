#!/usr/bin/python3
from os import system as s
import fileinput
import sys
try:
    with open("webhook.txt") as wbhk:
        webhook = wbhk.read().strip()
except FileNotFoundError:
        print("Error Loading Webhook - Error")
        sys.exit(1)
profile = str(input())
profile_url = str(input("Profile Picture (url) [Optional]: "))

if profile == "" or not profile:
    profile = ""
else:
    pass

if profile_url == "" or not profile_url:
	profile_url = ""
else:
    pass

for line in fileinput.input():
	print("Message: ")
	line = line.strip()
	s("curl -X POST -H \"Content-Type: application/json\" -d '{\"text\": \""+line+"\",\"username\":\""+profile+"\",\"avatar_url\": \""+profile_url+"\"}' "+webhook+"/slack 0> /dev/null 1> /dev/null 2> /dev/null")
