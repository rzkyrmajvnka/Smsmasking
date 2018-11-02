#!/usr/bin/env python

# SMS MASKING
# Coded by 4WSec
# 03/11/2018
# Anon Cyber Team


import os
import sys
import requests
import random

######## COLOR #########
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
########################

os.system('cls' if os.name == 'nt' else 'clear')


def masking():
	print
	try:
		no=open(wutz,'r').readlines()
	except:
		
		sys.exit()
	print "\n"+ color.YELLOW +"[*]"+ color.END +" Total Target>"+ color.WARNING +"",len(no)
	no_count=len(no)
	print ""+ color.YELLOW +"[*]"+ color.END +" Please Wait "+ color.WARNING +"...\n"
	count=0
	sendzz=open(wutz)
	while (no_count > count):
		sendto=sendzz.readline().replace('\n', '')
		zdata = {"Authorization":"kutu_gSoTC9puT34Llibk4iDG63GYJV5E4KU7knk3XYSm","text":text,"to":sendto}
		r = requests.post('https://api.kata-kutuku.net/sms/masking/', data=zdata)
		if "success" in r.text:
			print "   "+ color.WARNING +"[%s]"%(count) + color.GREEN +" OK [%s]"%(sendto)
		else:
			print "   "+ color.WARNING +"[%s]"%(count) + color.RED +" FAIL [%s]"%(sendto)
		count=count+1


if __name__ == "__main__":
	banner()
	wutz = raw_input("\n"+color.WARNING +""+color.UNDERLINE+"* Input Number List : "+color.END)
	text = raw_input("\n"+color.WARNING +""+color.UNDERLINE+"* Input Text : "+color.END)
	masking()
