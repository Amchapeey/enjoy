import os
import sys
import fileinput

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

logo = """
 \033[1;33m _____                             _            
 \033[1;33m|  __ \    \033[1;36mBash File\033[1;33m              | |           
 \033[1;33m| |  | | ___  ___ _ __ _   _ _ __ | |_ ___ _ __ 
 \033[1;33m| |  | |/ _ \/ __| '__| | | | '_ \| __/ _ \ '__|
 \033[1;33m| |__| |  __/ (__| |  | |_| | |_) | ||  __/ |   
 \033[1;33m|_____/ \___|\___|_|   \__, | .__/ \__\___|_|   
 \033[1;33m                        __/ | |                 
 \033[1;33m                       |___/|_|                 
 \033[1;33m
 \033[1;36m    [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY [𝐂𝐇𝐀𝐏𝐄𝐄𝐘-𝐓𝐄𝐂𝐇] @chapeey
 
"""
banner = """
 {}[{}01{}]{} Decrypt Bash File
 
 {}[{}02{}]{} More Tools from us
 
""".format(C,W,C,Y,C,W,C,Y)

os.system("clear")
print logo
print banner

def decr():
   try:
      print ("")
      scname = raw_input(G + " Name of the Script to Decrypt" + C + " > " + Y)
      o = open(scname,'r')
      filedata = o.read()
      o.close()
      
      new_dat = filedata.replace("eval","echo")
      print ("")
      output = raw_input(G + " Name of the Decrypted Script" + C + " > " + Y)
      f = open(output,'w')
      S = (output)
      f.write(new_dat)
      f.close()
      os.system("touch dummy.sh")
      os.system("bash " + output + " > dummy.sh")
      os.remove(output)
      os.system("mv -f dummy.sh " + output)
      print ("")
      print (G + " Decryption Succeed...")
      print ("")
      print (Y + " Decrypted Script Name" + C + " > " + G + S + W)
      print ("")
      
   except KeyboardInterrupt():
       print (R + " !" + Y + " Tool Stopped " + R + "!" + W)
       print ("")
   except IOError:
       print (R + " !" + Y + " File not Found " + R + "!" + W)
       print ("")

maintool = raw_input(G + " Select an option" + C + " > " + Y)

if maintool == "1" or maintool == "01":
   decr()
elif maintool == "2" or maintool == "02":
   os.system("xdg-open https://t.me/chapeey/")
else
   print (W + "")
   print (C + "[" + R + " !" + C + "]" + Y + " Invalid input " + C + "[" + R + "!" + C + "]")
