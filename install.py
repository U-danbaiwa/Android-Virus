import os
import sys
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
os.system("clear")
os.system("figlet U-danbaiwa")
print("please wait...")
os.system("cd /data/data/com.termux/files/home")
os.system("pkg update -y")
os.system("pkg install -y git")
os.system("pkg install python2")
os.system("pkg install figlet -y")
os.system("pkg install toilet -y")
print("\n")
print(yellow+bold+"\t\t=====COMPLETE=====")
print(green+bold+"\t\t\ttype\n\t\tpython gmail-hack.py")
