#!/usr/bin/env python3

import os
import sys
import time
import json
import time
import random
import threading
import subprocess
from urllib import parse
try:
	import requests
	import speedtest
	import colorama
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	dev):
		self.help = help
		self.dev = dev

	def home(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"F-Tool"+Color.LR+" | "+Color.LG+"Made By"+Color.LB+" F34RL3SS"+Color.LG+"    "+Color.LR+"<]")
		print(Color.LC+"        Type 'HELP' to see all commands ;)\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Proxy")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" WebTool")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" SpeedTest")
		print("\n")
		while True:
			try:
				option = input(Color.LR+"["+Color.LG+"Home"+Color.LR+"] >>> "+Color.RESET)
				if option == '01' or option == '1':
					os.system('clear')
					Tool.proxy(option)
				elif option == '02' or option == '2':
					os.system('clear')
					Tool.webtools()
				elif option == '03' or option == '3':
					os.system('clear')
					Tool.spdtest()
				elif option == 'ref' or option == 'REF':
					self.home()
				elif option == 'home' or option == 'HOME':
					self.home()
				elif option == 'clear' or option == 'CLEAR':
					os.system('clear')
				elif option == 'help' or option == 'HELP':
					print(self.help)
				elif option == 'dev' or option == 'DEV':
					print(self.dev)
				elif option == 'exit' or option == 'EXIT':
					subprocess.run(['pkill python'], shell=True)
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
			except KeyboardInterrupt:
				sys.exit(0)


class response_url:
	def __init__(self,
	headers):
		self.headers = headers

	def lookup(self, url):
		resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()

		info = Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']

		if resp['reverse'] == '':
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		else:
			return info

	def ip_lookup(self, ip):
		resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()

		info = Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])

		if resp['reverse'] == '':
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		else:
			return info

	def http_status(self, url):
		try:
			parser = parse.urlparse(url)
			if parser.scheme == "":
				url = "http://"+url
			resp = requests.get(url, headers=self.headers)
			status = resp.status_code
			if status == 200:
				return Color.LG+f"    [+] URL: {url}"+f"\n    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (OK)"
			elif status == 400:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Bad Requests)"
			elif status == 403:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Forbidden)"
			elif status == 404:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Not Found)"
			elif status == 429:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (To Many Requests)"
			elif status == 500:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Internal Server Error)"
			elif status == 502:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Bad Gateway)"
			elif status == 503:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Service Unavailable)"
			elif status == 504:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Gateway Timeout)"
			elif status == 507:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Insufficient Storage)"
			elif status == 508:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+f"\n    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Loop Detected)"
			else:
				return Color.LG+f"    [+] URL: {url}"+Color.LR+"\n    [+] Result: (Connection timeout)"

		except requests.exceptions.Timeout:
			return Color.LR+f"    [+] URL: {url}"+Color.LR+"\n    [+] Result: (Connection timeout)"
		except requests.exceptions.ConnectionError:
			return Color.LR+f"    [+] URL: {url}"+Color.LR+"\n    [+] Result: Error occurred"

	def findhost(self, host):
		resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}", headers=self.headers)

		info = resp.text
		if info == 'error invalid host':
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		else:
			return Color.LG+info

	def extractlink(self, url):
		resp = requests.get(f"https://api.hackertarget.com/pagelinks/?q={url}", headers=self.headers)

		info = resp.text
		if info == "input url is invalid":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		elif info == "error getting links":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" No Links Found!"
		else:
			return Color.LG+info

class Tool:
	def __init__(self,
	help,
	dev,
	headers):
		self.help = help
		self.dev = dev
		self.headers = headers

	def proxy(self, new):
		if new == 'ref' or new == 'REF':
			os.system('clear')
			print(Color.LG+"[*] Downloading New Proxy...")
		else:
			print(Color.LG+"[*] Downloading All Proxy...")
		with open("url.json", 'r') as p:
			read_url = p.read()
			readjson = json.loads(read_url)
		try:
			http  = requests.get(readjson['Proxies'][0]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][1]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][2]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][3]['url'], headers=self.headers).text
			https = requests.get(readjson['Proxies'][4]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][5]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][6]['url'], headers=self.headers).text
			https +=  requests.get(readjson['Proxies'][7]['url'], headers=self.headers).text
			socks4  = requests.get(readjson['Proxies'][8]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][9]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][10]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][11]['url'], headers=self.headers).text
			socks5 = requests.get(readjson['Proxies'][12]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][13]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][14]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][15]['url'], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit(Color.LR+"Error: Check your Internet Connection.")

		print(Color.LR+"\n\n    [>    "+Color.LG+"Proxy"+Color.LR+"    <]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" HTTP PROXY")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTPS PROXY")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" SOCKS4 PROXY")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SOCKS5 PROXY")
		print("\n")
		while True:
				option = input(Color.LR+"["+Color.LG+"Proxy"+Color.LR+"] >>> "+Color.RESET)
				if option == '01' or option == '1':
					with open("http.txt", 'w') as p:
						p.write(http)
					print(Color.LG+"[+]"+Color.LC+" Saved to http.txt")
				elif option == '02' or option == '2':
					with open("https.txt", 'w') as p:
						p.write(https)
					print(Color.LG+"[+]"+Color.LC+" Saved to https.txt")
				elif option == '03' or option == '3':
					with open("socks4.txt", 'w') as p:
						p.write(socks4)
					print(Color.LG+"[+]"+Color.LC+" Saved to socks4.txt")
				elif option == '04' or option == '4':
					with open("socks5.txt", 'w') as p:
						p.write(socks5)
					print(Color.LG+"[+]"+Color.LC+" Saved to socks5.txt")
				elif option == 'ref' or option == 'REF':
					self.proxy(option)
				elif option == 'home' or option == 'HOME':
					F_Tool.home()
				elif option == 'clear' or option == 'CLEAR':
					os.system('clear')
				elif option == 'help' or option == 'HELP':
					print(self.help)
				elif option == 'dev' or option == 'DEV':
					print(self.dev)
				elif option == 'exit' or option == 'EXIT':
					subprocess.run(['pkill python'], shell=True)
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def webtools(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Web Tool"+Color.LR+"    <]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" LOOKUP")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" IP INFO")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP STATUS")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" FIND HOST")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" EXTRACT LINK")
		print("\n")
		while True:
			option = input(Color.LR+"["+Color.LG+"WebTool"+Color.LR+"] >>> "+Color.LG)
			if option == '01' or option == '1':
				while True:
					lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					try:
						parser = parse.urlparse(lookup)
						host = parser.netloc
						path = parser.path.replace("/", "")
						if parser.scheme == 'https':
							print(response_url(self.headers).lookup(host))
						elif parser.scheme == 'http':
							print(response_url(self.headers).lookup(host))
						elif host == '':
							print(response_url(self.headers).lookup(path))
						else:
							print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					except:
						print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					break
			elif option == '02' or option == '2':
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
					try:
						print(response_url(self.headers).ip_lookup(ip_lookup))
					except:
						print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address")
					break
			elif option == '03' or option == '3':
				while True:
					http = input(Color.LR+"["+Color.LG+"HTTP CHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					try:
						print(response_url(self.headers).http_status(http))
					except:
						print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					break
			elif option == '04' or option == '4':
				while True:
					findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					try:
						parser = parse.urlparse(findhost)
						host = parser.netloc
						path = parser.path.replace("/", "")
						if parser.scheme == 'https':
							print(response_url(self.headers).findhost(host))
						elif parser.scheme == 'http':
							print(response_url(self.headers).findhost(host))
						elif host == '':
							print(response_url(self.headers).findhost(path))
						else:
							print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					except:
						print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					break
			elif option == '05' or option == '5':
				while True:
					excractlink = input(Color.LR+"["+Color.LG+"EXCRACTLINK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					try:
						print(response_url(self.headers).extractlink(excractlink))
					except:
						print(Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL")
					break
			elif option == 'ref' or option == 'REF':
				self.webtools()
			elif option == 'home' or option == 'HOME':
				F_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
			elif option == 'help' or option == 'HELP':
				print(self.help)
			elif option == 'dev' or option == 'DEV':
				print(self.dev)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill python'], shell=True)
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def spdtest(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Internet SpeedTest"+Color.LR+"    <]\n\n")
		try:
			spdt = speedtest.Speedtest()

			print(Color.LC+"[*] Loading Server List...")
			spdt.get_servers()
			time.sleep(0.1)

			print(Color.LC+"[*] Choosing Best Server...")
			get = spdt.get_best_server()
			time.sleep(0.1)

			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Location:"+Color.LY+f" {get['name']}")

			print(Color.LC+"\n[*] Performing Download Test...")
			download_result = spdt.download()

			print(Color.LC+"[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			time.sleep(0.1)
			print(Color.LC+"\nResults:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Download Speed:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Upload Speed:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Error: Check your Internet Connection.\n\n")


def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0', 
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
	'Chrome/34.0.1847.116 Safari/537.36',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01']

	headers = {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

	return headers


def main():
	F_Tool.home()


if __name__ == '__main__':
	commands = Color.LC+"""HOME"""+Color.LR+""" ~> """+Color.LY+"""Back to home"""+Color.LC+"""
REF"""+Color.LR+""" ~> """+Color.LY+"""Refresh the program"""+Color.LC+"""
CLEAR"""+Color.LR+""" ~> """+Color.LY+"""Clear your face XD"""+Color.LC+"""
EXIT"""+Color.LR+""" ~> """+Color.LY+"""Exit the program"""+Color.LC+"""
DEV"""+Color.LR+""" ~> """+Color.LY+"""Contact me :)"""
	dev = Color.LC+"""Telegram"""+Color.LR+"""  :"""+Color.LY+""" https://t.me/FDc0d3"""+Color.LC+"""
Github"""+Color.LR+"""    :"""+Color.LY+""" https://github.com/FDc0d3"""+Color.LC+"""
Facebook"""+Color.LR+"""  :"""+Color.LY+""" https//facebook.com/F34RL3SS.DEV"""+Color.LC+"""
Email"""+Color.LR+"""     :"""+Color.LY+""" fearless-devs@proton.me"""
	F_Tool = Home(commands, dev)
	Tool = Tool(commands, dev, spoof_useragents())
	main()
