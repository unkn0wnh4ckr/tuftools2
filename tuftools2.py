#!/usr/local/bin/python
# coding: latin-1
import sys
import os
import socks
import socket
import time
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("""
bold=`echo -en "\e[1m"`
underline=`echo -en "\e[4m"`
dim=`echo -en "\e[2m"`
strickthrough=`echo -en "\e[9m"`
blink=`echo -en "\e[5m"`
reverse=`echo -en "\e[7m"`
hidden=`echo -en "\e[8m"`
 normal=`echo -en "\e[0m"`
 black=`echo -en "\e[30m"`
 red=`echo -en "\e[31m"`
 green=`echo -en "\e[32m"`
 orange=`echo -en "\e[33m"`
 blue=`echo -en "\e[34m"`
 purple=`echo -en "\e[35m"`
 aqua=`echo -en "\e[36m"`
 gray=`echo -en "\e[37m"`
 darkgray=`echo -en "\e[90m"`
 lightred=`echo -en "\e[91m"`
 lightgreen=`echo -en "\e[92m"`
 lightyellow=`echo -en "\e[93m"`
 lightblue=`echo -en "\e[94m"`
 lightpurple=`echo -en "\e[95m"`
 lightaqua=`echo -en "\e[96m"`
 white=`echo -en "\e[97m"`
 default=`echo -en "\e[39m"`
 BLACK=`echo -en "\e[40m"`
 RED=`echo -en "\e[41m"`
 GREEN=`echo -en "\e[42m"`
 ORANGE=`echo -en "\e[43m"`
 BLUE=`echo -en "\e[44m"`
 PURPLE=`echo -en "\e[45m"`
 AQUA=`echo -en "\e[46m"`
 GRAY=`echo -en "\e[47m"`
 DARKGRAY=`echo -en "\e[100m"`
 LIGHTRED=`echo -en "\e[101m"`
 LIGHTGREEN=`echo -en "\e[102m"`
 LIGHTYELLOW=`echo -en "\e[103m"`
 LIGHTBLUE=`echo -en "\e[104m"`
 LIGHTPURPLE=`echo -en "\e[105m"`
 LIGHTAQUA=`echo -en "\e[106m"`
 WHITE=`echo -en "\e[107m"`
 DEFAULT=`echo -en "\e[49m"`
""")


W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'
LB = '\033[1;36m'
P = '\033[35m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packets = random._urandom(5000)
none_ascii = '''
                              ████████████████████████████████████████████████░ 
██████████░            ████████░ ██░ █░ █░   █░    █░   █░  ██░       ██░     █░
█░  ██░  █░            ██░       ██░   ███░  ██░  ███░  ██░ ██░       ██░
    ██░      █░   █░   █████░    ██░   ██░█░ ██░  ██░█░ ██░ ██░        ████████░
    ██░      █░   █░   ██░       ██░   ██░ █░██░  ██░ █░██░ ██░               ██░
    ██░      █░   █░   ██░       ██░    █░  ██░    █░  ██░  ██░     █░ █░     ██░
    ██░       ████░    ██░       ██░     ████░      ████░    ████████░ ████████░   \033[0m2.0
                        \033[32mcoded by\033[0m @unkn0wn_bali    
      
'''
print R+(none_ascii.decode('utf-8'))

print N+"""
1: fade          \033[93mtype\033[0m : dos          \033[93mfile\033[0m : python

2: hydra         \033[93mtype\033[0m : password     \033[93mfile\033[0m : shell?

3: metasploit    \033[93mtype\033[0m : exploit      \033[93mfile\033[0m : ruby

4: red hawk      \033[93mtype\033[0m : info         \033[93mfile\033[0m : php

5: katoolin      \033[93mtype\033[0m : install      \033[93mfile\033[0m : python

6: instainsane   \033[93mtype\033[0m : password     \033[93mfile\033[0m : shell

7: nmap          \033[93mtype\033[0m : info         \033[93mfile\033[0m : shell?

8: th3inspector  \033[93mtype\033[0m : info         \033[93mfile\033[0m : perl

9: cupp          \033[93mtype\033[0m : password     \033[93mfile\033[0m : python

10: no 10th remove this and reclone it for new scripts when i add more
"""

tool = raw_input('[\033[91mtuf\033[0m]:  \033[91mchoose a tool \033[92m$:\033[1;36m ')

if tool == "1" : os.system("git clone https://github.com/unkn0wnh4ckr/fade")
if tool == "2" : os.system("apt-get install hydra")
if tool == "3" :
	print Y+"would you like to apt install or git clone? [git/apt]"
	metasploit = raw_input(Y+"$:\033[1;36m ")
	if metasploit == "git" : os.system("git clone https://github.com/rapid7/metasploit-framework")
	if metasploit == "apt" : os.system("apt-get install metasploit-framework")
	else : print "\033[0m[\033[91m+\033[0m]  \033[91mno option called\033[0m", metasploit
if tool == "4" : os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
if tool == "5" : os.system("git clone https://github.com/LionSec/katoolin")
if tool == "6" : os.system("git clone https://github.com/thelinuxchoice/instainsane")
if tool == "7" : os.system("apt-get install nmap")
if tool == "8" : os.system("git clone https://github.com/Moham3dRiahi/Th3inspector")
if tool == "9" :
	print Y+"would you like to apt install or git clone? [git/apt]"
	cupp = raw_input(Y+"$:\033[1;36m ")
	if cupp == "git" : os.system("git clone https://github.com/Mebus/cupp")
	if cupp == "apt" : os.system("apt-get install cupp")
	else : print "\033[0m[\033[91m+\033[0m]  \033[91mno option called\033[0m", cupp
if tool == "10" : print """
so i cant think of another script to add so its stopping
at 9 but i will add more in the future so make sure to
reclone it often il post when i add a new script on my instagram
@unkn0wn_bali - thanks for getting the script =]
"""
else : print "\033[0m[\033[91m+\033[0m]  \033[91mno option called\033[0m", tool