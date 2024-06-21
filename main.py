# Himari by fx-09. Please do include the MIT license if you fork this repo.
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title Himari By fx-09")
os.system('cls' if os.name == 'nt' else 'clear')
print ("[+] Information:")
print ("[-] With Himari, you can get more GBs on WARP+.")
print ("[-] Version: alpha1")
print ("--------")
print ("[+] Himari was written by fx-09, please do not abuse this script because Cloudflare can ban your hardware ID (like Vanguard) if they detect an abnormal amount of GBs used.") 
print ("[-] Himari is licensed in MIT (as stated in the repository).")
print ("[-] Visit: https://github.com/fx-09 for more stuffs.") 
print ("--------")
referrer = input("[#] Enter your WARP+ ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  Himari" + " by fx-09")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] Currently working on ID: {referrer}")    
		print(f"[:)] {g} GB(s) has been added to your account.")
		print(f"[#] Status: We have {g} good requests and {b} bad requests.")
		print("[*] After 18 seconds, a new request will be sent, this countdown is necessary to avoid getting flagged as bots.")
		print(" ")
		print("[!] Want to stop the script? Press Ctrl + Z to suspend, or click X to quit the window.")
		time.sleep(18)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  Himari" + " by fx-09")
		print("")
		print("[:(] Error when connecting to server, try again...")
		print(f"[#] Total: {g} Good {b} Bad")
		print("Feeling chaotic and want to get out this madness? Press Ctrl + Z to suspend, or click X to quit the window.")