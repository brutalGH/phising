import requests,json,random,rich,bs4,sys,time,os
from concurrent.futures import ThreadPoolExecutor as thread
from bs4 import BeautifulSoup
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'


ses = requests.Session()
id = []
tulis = []
jalan = []
def brut(u):
        for e in u :sys.stdout.write(e);sys.stdout.flush();time.sleep(0.02)

def banner():
	brut(f'{x}.....')
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	wel = '# SPAMMER TOOLS'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """
    
	pengembang1=nel(au,style="cyan")
	cetak(nel(pengembang1, title='v 3.144'))
	if 'menu' in jalan:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Processing....\n')
	elif 'pilih' in jalan:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Waitting....\n')
	else:
		brut(f'{x} ╗\n ╠ [ {h}• {x}] Processing....\n')

loop = 0
def check(idf,pw):
	global loop
	url1 = 'http://ff-spinm1e2.vipgiz37.rocks/vhsfhqpdhdxih1/check.php'
	ua = 'Mozilla/5.0 (Linux; Android 9; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36'
	header = {
	'initiator':'http://ff-spinm1e2.vipgiz37.rocks',
	'Accept':'application/zoho.forms-v1+json',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	'Content-Type':'application/json',
	'Origin':'http://ff-spinm1e2.vipgiz37.rocks',
	'Referer':'http://ff-spinm1e2.vipgiz37.rocks/vhsfhqpdhdxih1/',
	'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
	'sec-ch-ua-mobile':'?1',
	'sec-ch-ua-platform':'"Android"',
	'Sec-Fetch-Dest':'empty',
	'Sec-Fetch-Mode':'cors',
	'Sec-Fetch-Site':'same-origin',
	'User-Agent':ua,
	'X-Requested-With':'XMLHttpRequest'
    	}

	data = {
	'level': '999',
	'login': 'Facebook',
	'pass': pw,
	'phone': idf,
	'playid':	'6812202149',
	'user': idf
	}
	ok = ses.post(url1,headers=header,data=data)
	if ok.status_code == 200:
		jum = str(len(id))
		if 'tidak' in tulis:
			print(f'\r{x} ╠{x} [ {h}• {x}]{x} Succes Post{h} {loop}{x} Result',end=" ")
		elif 'ya' in tulis:
			#print(f'\r{x} ╠{x} [ {m}• {x}] Send ke {m} {loop} {h}Succes ',end='')
			print(f'\r{x} ╠{x} [ {h}• {x}] Succes, Email :{h} '+idf+f'{x} Pw : {h}'+pw)
		else:
			print(f'\r{x} ╠{x} [ {h}• {x}]{x} Succes Post{h} '+str(len(id))+f'{x} Result',end=" ")
	else:
		print('	=>> Failed Send email : '+idf+'pw : '+pw)
	loop+=1

def mulai():
	jalan.append('menu')
	banner()		
	file = open('nomor.txt','r').readlines()	
	with thread(max_workers=30) as pool:	
		for i in file:
		    seq = i.strip()
		    id.append(seq)
		    idf = seq
		    pw = 'brutal_XYZ'
		    pool.submit(check,idf,pw)

def pilih():
	jalan.append('pilih')
	banner()
	print(f'\r{x} ╠{x} [ {h}• {x}] Print Email & Pw Y / T ')
	pil = input(f'\r{x} ╠{x} [ {h}• {x}] Pilih :{h} ')
	if pil in ['Y','y']:
		tulis.append('ya')
	elif pil in ['T','t']:
		tulis.append('tidak')
	else:
		tulis.append('ya')

if __name__=='__main__':
	pilih()
	mulai()
