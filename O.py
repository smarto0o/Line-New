# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from bs4 import BeautifulSoup
from datetime import datetime
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, tempfile,glob,shutil,unicodedata,urllib3
from gtts import gTTS

satpam = LINETCR.LINE() #koplaxs
satpam.login(token="En0b15GheJNgki3bCgDe.pY8cs+TbJ3nrv9Xt6OZMtG.hQbHjmpE0KOJdATv484wHDIrw7fq4xX35ZD/AjIKdhQ=")
satpam.loginResult()

cl = LINETCR.LINE() 
cl.login(token="EnuEIDmpNyZas2igUytb.UdwLjeqPikMAOWh25mdzsW.02+b1k1Mub/+1/SwZFFWqu1jOPY3sQiPSq11RlPPQsU=")
cl.loginResult()

ki = LINETCR.LINE() 
ki.login(token="Enh9XfnRcJJHuDCzvtpd.eYrnvLmoYVtzng7g00cIxq.15iWukYA9hcyJl5gx+7lZfJBUUxyiCt3G7oCZeLb2gk=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EnZhaY2Iu9cIHVNTSMx9.MWZ54yoga4o06/+AkAGCQq.eJnDJgpbfWsLn6iogq2OnAgT3pRxe/LMnvnQKyPt5O4=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="Enp79AkoDfpbLk9T7HM7.LYqePLf2nacZLRp5YVB8bW.R9Nzfdedk7DARI9cK6cAmBki2dDQqqap8WDf1ISHbyU=")
kc.loginResult()

ks = LINETCR.LINE()
ks.login(token="EndMXuTQr3OaFg5dsZo0.Oy6eUeSoOMBbaZvyx1FRaa.oQhaib+EcHFBFNz+ZmTQnOdeyc5WHI0AlJp6ljrquXQ=")
ks.loginResult()

k1 = LINETCR.LINE() #Backup
k1.login(token="En1doewY4gdxDXaha8W6.4qLtipwiaMivyrW3+bWZfG.EOyUnEQogQ3rvcINFfnf8Uc7/beqbk7qAyMcGF5qCKM=")
k1.loginResult()

print "login success Boss"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║   ^[OP Protect Bot]^
║   Owner : ✰Doni✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║𖤓Menu For Public𖤓
║╔════════════
║╠[★]Adminlist
║╠[★]Ownerlist
║╠[★]Whitelist
║╠[★]Info Group
║╠[★]Welcome
║╠[★]Creator
║╠[★]Bot
║╠[★]Wkwkwk
║╠[★]Hehehe
║╠[★]Galau
║╠[★]You
║╠[★]Please
║╠[★]Lol
║╠[★]Welcome
║╠[★]Ping
║╠[★]Ini Apa
║╚════════════
║𖤓Menu For Admin𖤓
║╔════════════
║╠[★]Status/Set
║╠[★]Cancel
║╠[★]Buka/Tutup qr
║╠[★]Mid Bot
║╠[★]Speed/Sp
║╠[★]Cctv(Ciduk)
║╠[★]Status/Set
║╠[★]Gurl
║╠[★]Jam「On/Off
║╠[★]Tag all/Tagall
║╠[★]Absen/Respon
║╠[★]Banlist
║╠[★]Group Rename
║╠[★]Yusuf: Text Cari
║╠[★]Pp @Tag
║╠[★]Dp @Tag
║╠[★]Gn Nama Group
║╠[★]Bot? (Mid Bot)
║╠[★]Mid Bot
║╠[★]Me (Cek Mid)
║╠[★]Info Group
║╠[★]Mid @
║╠[★]Ig: Instagram
║╠[★]Yusuf: Youtube
║╠[★]/music Judul
║╠[★]Pp Group (Nama)
║╠[★]One Piece
║╠[★]SVF
║╚════════════
║𖤓Menu For Owner𖤓
║╔════════════
║╠[★]Qr On/Off
║╠[★]Cancel On/Off
║╠[★]Join On/Off
║╠[★]Share On/Off
║╠[★]Add On/Off
║╠[★]Admin add @
║╠[★]Owner add @
║╠[★]Whitelist @
║╠[★]Bot add @
║╠[★]Mimic
║╠[★]Invite Via Share
║╠[★]Allbio:Bio Bot
║╠[★]Spam Group
║╠[★]Friends BC
║╠[★]Bot 1/10 Rename
║╠[★]/imvotemeto:
║╠[★]Update Jam
║╠[★]Masuk
║╠[★]Keluar
║╠[★]Like Status
║╠[★]Like Me
║╠[★]Fvck(Kickers)
║╠[★]Nk @ Kick
║╠[★]Ban (Share)
║╠[★]Ban All
║╠[★]Unban (Share)
║╠[★]Copy @/Backup
║╠[★]Contact BC
║╠[★]List Group
║╠[★]Spam Kontak
║╠[★]Undang (Share)
║╠[★]Spam Invite
║╠[★]Spam 1000 Chat
║╚════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║        Support By
║       ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═════════════"""

Setgroup =""" 
    [Admin Menu]
================
1) Protect QR
2) Qr on/off
3) Protect Join
4) Join on/off
5) Mid Via Contact
6) Contact on/off
7) Cancel Invited
8) Cancel all
=====================
       MARS AUTO BOT
૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
====================="""

About = """╔═════════════
║One Piece Bot Version 1.5║
╚═════════════"""

KAC=[cl,ki,kk,kc,ks]
#DEF1=[ki,kk,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF2=[cl,kk,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF3=[cl,ki,kc,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF4=[cl,ki,kk,ks,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF5=[cl,ki,kk,kc,ka,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF6=[cl,ki,kk,kc,ks,kb,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF7=[cl,ki,kk,kc,ks,ka,ko,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF8=[cl,ki,kk,kc,ks,ka,kb,ke,ku] Udah Ga Kepake(Boleh di apus)
#DEF9=[cl,ki,kk,kc,ks,ka,kb,ko,ku] Udah Ga Kepake(Boleh di apus)
#DEF10=[cl,ki,kk,kc,ks,ka,kb,ko,ke] Udah Ga Kepake(Boleh di apus)
mid = cl.getProfile().mid #Tobirama
Amid = ki.getProfile().mid #Minato
Bmid = kk.getProfile().mid #Madara
Cmid = kc.getProfile().mid #Hasirama
Dmid = ks.getProfile().mid #Itama
mid1 = k1.getProfile().mid
Smid = satpam.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Smid,"ub835a524442920a99aa301f6e4c0d94b","u13244d56530ecaf4d9346ec6d340a25d","u9b0cf9e183860383b4ebefda29a81ca9","u972404a651763400b396b3f9caf6fc07","ua18e84b84b0ea266c10335585f57eb00"]
admin=["u3f2f024bfb418f735157dc53ea8ce64e"] 
owner=["u3f2f024bfb418f735157dc53ea8ce64e"]
whitelist=["ued156c86ffa56024c0acba16f7889e6d","uda679d194cf1ccdc62fcdd04b75810c5","u801eaa377df5afa1b6c19d1c4a84a7d3","uc3836737903b17b9d8fe3746a96d077e","u64da1f196cf76cf585ee7628a37ae501","u245ff14d390ed66a1ace50976d98a1fc","ub478b38260ee820e672d877810fbef36","uec1eb9eace6cc63a7f8aadf1afbc9af7","u6bc4b1a7b745ffea150f8508d6e92280","ucb4d1c40701e9c24c48d97309f6ec1f0","u728ceea7eb0700e3f2a1184235e9243f"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ OP AUTO BOT PROTECT ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ☆
☆ MARS FAMILY ☆""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":True,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "winvite" :False,
    "winvite2" :False,
    "winvite3" :False,
    "winvite4" :False,
    "winvite5" :False,
    "wblacklist":True,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
        
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
          
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in whitelist:
                pass
              else:
              	try:
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Jangan Buka Kode QR Kk")
                	cl.kickoutFromGroup(op.param1,[op.param2])
                	X = cl.getGroup(op.param1)
                	X.preventJoinByTicket = True
                	cl.updateGroup(X)
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Kk")
                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                	X = random.choice(KAC).getGroup(op.param1)
                	X.preventJoinByTicket = True
                	random.choice(KAC).updateGroup(X)
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in whitelist:
                pass
              else:
                try:
                  cl.cancelGroupInvitation(op.param1, gMembMids)
                  cl.sendText(op.param1, "Mau Invite Siapa Plak???\nKarna Ente Bukan Staff Jadi Ane Batalin Yah")
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1, "Mau Invite Siapa Plak???\nKarna Ente Bukan Staff Jadi Ane Batalin Yah")
        #------Cancel Invite User Finish------#
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"

            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"

            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"

            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Smid in op.param3:
              if wait["autoJoin"] == True:
                satpam.acceptGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
        if op.type == 17: #awal 17 ubah 13
          if wait["Protectjoin"] == True:
            if op.param2 not in admin or Bots:
            	if op.param2 in admin:
            	  pass
            	elif op.param2 in Bots:
            	  pass
            	elif op.param2 in whitelist:
            	  pass
            	else:
            	  try:
            	    cl.kickoutFromGroup(op.param1,[op.param2])
            	    cl.sendText(op.param1, "Protect Join Is On\nMatiin Terlebih dahulu Lalu Invite lagi\nCara matiin => Joinn off\nJangan Lupa Hidupkan lagi yah Ka Setelah Yang Di undang Join\nDemi Keamanan Group")
            	  except:
            	    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).sendText(op.param1,"Protect Join Is On\nMatiin Terlebih dahulu Lalu Invite lagi\nCara matiin => Joinn off\nJangan Lupa Hidupkan lagi yah Ka Setelah Yang Di undang Join\nDemi Keamanan Group")
        if op.type == 17: #awal 17 ubah 13
          if wait["Protectjoin"] == True:
            if op.param3 not in admin or Bots:
              if op.param3 in owner:
                pass
            	if op.param3 in admin:
            	  pass
            	elif op.param3 in Bots:
            	  pass
            	elif op.param3 in whitelist:
            	  pass
            	else:
            	  try:
            	    cl.kickoutFromGroup(op.param1,[op.param3])
            	    #cl.sendText(op.param1, "Protect Join Is On\nMatiin Terlebih dahulu Lalu Invite lagi\nCara matiin => Joinn off\nJangan Lupa Hidupkan lagi yah Ka Setelah Yang Di undang Join\nDemi Keamanan Group")
            	  except:
            	    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              cl.kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
        
        if op.type == 19: #Admin Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                    
              elif op.param3 in whitelist:
                if op.param2 not in Bots or owner:
                  try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
            except:
              try:
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or owner:
                try:
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  #cl.sendText(op.param1, "Makasih Brader")
                  #k1.sendText(op.param1, "Sama² Brader")
                  #k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  #cl.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  #cl.sendText(op.param1, "Makasih Brader")
                  #k1.sendText(op.param1, "Sama² Brader")
                  #k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  #cl.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Amid:
              if op.param2 not in Bots or owner:
                try:
                  G = kk.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Bmid:
              if op.param2 not in Bots or owner:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Cmid:
              if op.param2 not in Bots or owner:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Dmid:
              if op.param2 not in Bots or owner:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #f=codecs.open('st2__b.json','w','utf-8')
                  #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            elif op.param3 in Smid:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  H = cl.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  cl.updateGroup(H)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  #H = cl.getGroup(op.param1)
                  H.preventJoinByTicket = True
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  wait["blacklist"][op.param2] = True
#--------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
              if wait["winvite"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = cl.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      cl.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        cl.inviteIntoGroup(msg.to,[target])
                        cl.sendText(msg.to,"Sudah di invite bossquee💋: \n➡" + _name)
                        wait["winvite"] = False
                        break
                      except:
                        try:
                          cl.findAndAddContactsByMid(invite)
                          cl.inviteIntoGroup(op.param1,[invite])
                          wait["winvite"] = False
                        except:
                          try:
                            cl.findAndAddContactsByMid(invite)
                            cl.inviteIntoGroup(op.param1,[invite])
                            wait["winvite"] = False
                            cl.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              cl.findAndAddContactsByMid(invite)
                              cl.inviteIntoGroup(op.param1,[invite])
                              wait["winvite"] = False
                              cl.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                              break
                            except:
                              cl.sendText(msg.to,"Negative, Error detected")
                              wait["winvite"] = False
                              break
              elif wait["winvite2"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ki.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ki.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ki.findAndAddContactsByMid(target)
                        ki.inviteIntoGroup(msg.to,[target])
                        ki.sendText(msg.to,"Sudah di invite bossquee💋: \n➡" + _name)
                        wait["winvite2"] = False
                        break
                      except:
                        try:
                          ki.findAndAddContactsByMid(invite)
                          ki.inviteIntoGroup(op.param1,[invite])
                          wait["winvite2"] = False
                        except:
                          try:
                            ki.findAndAddContactsByMid(invite)
                            ki.inviteIntoGroup(op.param1,[invite])
                            wait["winvite2"] = False
                            ki.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ki.findAndAddContactsByMid(invite)
                              ki.inviteIntoGroup(op.param1,[invite])
                              wait["winvite2"] = False
                              ki.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                              break
                            except:
                              ki.sendText(msg.to,"Negative, Error detected")
                              wait["winvite2"] = False
                              break
              elif wait["winvite3"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kk.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kk.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kk.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kk.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kk.findAndAddContactsByMid(target)
                        kk.inviteIntoGroup(msg.to,[target])
                        kk.sendText(msg.to,"Sudah di invite bossquee💋: \n➡" + _name)
                        wait["winvite3"] = False
                        break
                      except:
                        try:
                          kk.findAndAddContactsByMid(invite)
                          kk.inviteIntoGroup(op.param1,[invite])
                          wait["winvite3"] = False
                        except:
                          try:
                            kk.findAndAddContactsByMid(invite)
                            kk.inviteIntoGroup(op.param1,[invite])
                            wait["winvite3"] = False
                            kk.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kk.findAndAddContactsByMid(invite)
                              kk.inviteIntoGroup(op.param1,[invite])
                              wait["winvite3"] = False
                              kk.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                              break
                            except:
                              kk.sendText(msg.to,"Negative, Error detected")
                              wait["winvite3"] = False
                              break
              elif wait["winvite4"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kc.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kc.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kc.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kc.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kc.findAndAddContactsByMid(target)
                        kc.inviteIntoGroup(msg.to,[target])
                        kc.sendText(msg.to,"Sudah di invite bossquee💋: \n➡" + _name)
                        wait["winvite4"] = False
                        break
                      except:
                        try:
                          kc.findAndAddContactsByMid(invite)
                          kc.inviteIntoGroup(op.param1,[invite])
                          wait["winvite4"] = False
                        except:
                          try:
                            kc.findAndAddContactsByMid(invite)
                            kc.inviteIntoGroup(op.param1,[invite])
                            wait["winvite4"] = False
                            kc.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kc.findAndAddContactsByMid(invite)
                              kc.inviteIntoGroup(op.param1,[invite])
                              wait["winvite4"] = False
                              kc.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                              break
                            except:
                              kc.sendText(msg.to,"Negative, Error detected")
                              wait["winvite4"] = False
                              break
              elif wait["winvite5"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ks.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ks.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ks.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ks.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ks.findAndAddContactsByMid(target)
                        ks.inviteIntoGroup(msg.to,[target])
                        ks.sendText(msg.to,"Sudah di invite bossquee💋: \n➡" + _name)
                        wait["winvite5"] = False
                        break
                      except:
                        try:
                          ks.findAndAddContactsByMid(invite)
                          ks.inviteIntoGroup(op.param1,[invite])
                          wait["winvite5"] = False
                        except:
                          try:
                            ks.findAndAddContactsByMid(invite)
                            ks.inviteIntoGroup(op.param1,[invite])
                            wait["winvite5"] = False
                            ks.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ks.findAndAddContactsByMid(invite)
                              ks.inviteIntoGroup(op.param1,[invite])
                              wait["winvite5"] = False
                              ks.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                              break
                            except:
                              ks.sendText(msg.to,"Negative, Error detected")
                              wait["winvite5"] = False
                              break
              elif wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  cl.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  cl.sendText(msg.to,"decided not to comment")
                  
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  ki.sendText(msg.to,"deleted")
                  kk.sendText(msg.to,"deleted")
                  kc.sendText(msg.to,"deleted")
                  wait["dblack"] = False

                else:
                  wait["dblack"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  ki.sendText(msg.to,"It is not in the black list")
                  kk.sendText(msg.to,"It is not in the black list")
                  kc.sendText(msg.to,"It is not in the black list")
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  cl.sendText(msg.to,"already")
                  ki.sendText(msg.to,"already")
                  kk.sendText(msg.to,"already")
                  kc.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  cl.sendText(msg.to,"aded")
                  ki.sendText(msg.to,"aded")
                  kk.sendText(msg.to,"aded")
                  kc.sendText(msg.to,"aded")

              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  ki.sendText(msg.to,"deleted")
                  kk.sendText(msg.to,"deleted")
                  kc.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False

                else:
                  wait["dblacklist"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  ki.sendText(msg.to,"It is not in the black list")
                  kk.sendText(msg.to,"It is not in the black list")
                  kc.sendText(msg.to,"It is not in the black list")
              elif wait["contact"] == True:
                msg.contentType = 0
                cl.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
                    
  #--------- Mimic------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
              text = msg.text
              if text is not None:
                cl.sendText(msg.to,text)
              else:
                if msg.contentType == 7:
            	    msg.contentType = 7
            	    msg.text = None
            	    msg.contentMetadata = {
            	               "STKID": "6",
            	               "STKPKGID": "1",
            	               "STKVER": "100" }
            	    cl.sendMessage(msg)
                elif msg.contentType == 13:
            	    msg.contentType = 13
            	    msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            	    cl.sendMessage(msg)
            
            elif "Mimic:" in msg.text:
              if msg.from_ in owner:
                cmd = msg.text.replace("Mimic:","")
                if cmd == "on":
                  if mimic["status"] == False:
                    mimic["status"] = True
                    cl.sendText(msg.to,"Mimic On Bossque")
                  else:
                    cl.sendText(msg.to,"Mimic Sudah On Bossque")
                elif cmd == "off":
                  if mimic["status"] == True:
                    mimic["status"] = False
                    cl.sendText(msg.to,"Mimic Off Bossque")
                  else:
                    cl.sendText(msg.to,"Mimic Sudah off")
                elif "add:" in cmd:
                  target0 = msg.text.replace("Mimic:add:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Success added target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Siap Ngikutin Chat Target Boss")
                        break
                elif "del:" in cmd:
                  target0 = msg.text.replace("Mimic:del:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Success deleted target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Ane Ga ngikutin lagi ah\nCape Gak Dapet Duit")
                        break
                elif cmd == "list":
                  if mimic["target"] == {}:
                    cl.sendText(msg.to,"No target")
                  else:
                    mc = "Target Mimic\n"
                    mids = []
                    for s in range(len(mimic["target"])):
                        mids.append(mimic["target"][s])
                    cmids = cl.getContacts(mids)
                    for x in range(len(cmids)):
                        mc += "\n["+str(x)+"]"+cmids[x].displayName
                    cl.sendText(msg.to,mc)
  #---------------------------
            elif msg.text in ["Menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif msg.text in ["Promo","Promosi","Promosi bot"]:
              if msg.from_ in owner or admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Promo)
                else:
                    cl.sendText(msg.to,Promo)
            elif msg.text in ["Bot Version","Bot version","OP Version","OP version"]:
              #if msg.from_ in owner or admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,About)
                else:
                    cl.sendText(msg.to,About)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Minato gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Madara gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Hasirama gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Minato kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Madara kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Hasirama kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Minato invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Madara invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Hasirama invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            ks.findAndAddContactsByMid(target)
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Sudah Ditambahkan Boss")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                          owner.append(target)
                          cl.sendText(msg.to,"Owner Sudah Ditambahkan Boss")
                        except:
                          owner.append(target)
                          cl.sendText(msg.to,"Owner Sudah Ditambahkan Boss")
                #print "[Command]Owner add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            cl.sendText(msg.to,"Owner Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "👑 Admin One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                      mc += "[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
                  
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  cl.sendText(msg.to,"The Owner is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "👑 Owner One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                      mc += "[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
    #--------------- Lawan atau Whitelist -------
            elif "Whitelist @" in msg.text:
              if msg.from_ in owner:
                #print "[Command]Staff add executing"
                _name = msg.text.replace("Whitelist @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Orang nya Ga Keliatan Kaya Setan")
                else:
                   for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            ks.findAndAddContactsByMid(target)
                            whitelist.append(target)
                            cl.sendText(msg.to,"Whitelist Ditambahkan")
                        except:
                            pass
                #print "[Command]Kawan add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                
            elif "Whitelist remove @" in msg.text:
              if msg.from_ in owner:
                #print "[Command]Kawan remove executing"
                _name = msg.text.replace("Whitelist remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Orangnya ga ada Lagi Colli")
                else:
                   for target in targets:
                        try:
                            whitelist.remove(target)
                            cl.sendText(msg.to,"Whitelist Dihapus")
                        except:
                            pass
                #print "[Command]Kawan remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak !!!")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                
            elif msg.text in ["Whitelist","whitelist"]:
              if whitelist == []:
                  cl.sendText(msg.to,"Whitelist nya Kosong Boss")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "👥Whitelist One Piece Team👥\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in whitelist:
                      mc += "👉 [★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  #print "[Command]Stafflist executed"
    #--------------------------------------
    #--------------------------------------
    #-------------- Add Friends -----------
            elif "Bot add @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        satpam.findAndAddContactsByMid(target)
                        cl.sendText(msg.to,"Kami Sudah Menambahkannya Sebagai Teman")
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam " in msg.text:
              if msg.from_ in owner:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                #Keke cantik <3
                if txt[1] == "on":
                  if jmlh <= 1000:
                    for x in range(jmlh):
                      cl.sendText(msg.to, teks)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                elif txt[1] == "off":
                  if jmlh <= 2000:
                    cl.sendText(msg.to, tulisan)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                    
            elif "Fbc " in msg.text:
              if msg.from_ in owner:
	              print "[Friend Broadcast Excuted]"
	              bctxt = msg.text.replace("Fbc ","")
	              n = cl.getAllContactIds()
	              for people in n:
	                cl.sendText(people, (bctxt))
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
            elif msg.text in ["Me"]:
              #if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Boss")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cuy buka qr","Cuy open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Boss")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bro buka qr","Bro open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Boss")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Hasirama open qr","Hasirama buka qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Bro")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Minato close qr","Minato tutup qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Bro")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Madara tutup qr","Madara close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Bro")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Hasirama tutup qr","Hasirama close qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Bro")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
            elif "Tobirama" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Minato" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Madara" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "SHasirama" == msg.text:
              if msg.from_ in admin:
                kc.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Bot1 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                  profile = cl.getProfile()
                  profile.displayName = string
                  cl.updateProfile(profile)
                  cl.sendText(msg.to,"name " + string + " done")
            elif "Bot2 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"name " + string + " done")
            elif "Bot3 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot3 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"name " + string + " done")
            elif "Bot4 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot4 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"name " + string + " done")
            elif "Bot5 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot5 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã���ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "╔═════════════\n║⭐Status Proteksi⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                if wait["Protectgr"] == True: md+="║[•]Protect QR 🔒\n"
                else: md+="║[•]Protect QR 🔓\n"
                if wait["Protectcancl"] == True: md+="║[•]Protect Invite 🔒\n"
                else: md+="║[•]Protect Invite 🔓\n"
                if wait["contact"] == True: md+="║[•]Contact ✔\n"
                else: md+="║[•]Contact ✖\n"
                if wait["autoJoin"] == True: md+="║[•]Auto Join ✔\n"
                else: md +="║[•]Auto Join ✖\n"
                #if wait["autoCancel"]["on"] == True:md+="║[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                #else: md+="║[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="║[•]Auto Leave ✔\n"
                else: md+="║[•]Auto Leave ✖\n"
                if wait["timeline"] == True: md+="║[•]Share ✔\n"
                else: md+="║[•]Share ✖\n"
                if wait["autoAdd"] == True: md+="║[•]Auto Add ✔\n"
                else: md+="║[•]Auto Add ✖\n"
                if wait["commentOn"] == True: md+="║[•]Comment ✔\n"
                else: md+="║[•]Comment ✖\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║⭐૦Ո૯ ƿɿ૯८૯ ੮૯คɱ⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═════════════"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Minato gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Madara gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Hasirama gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Cctv":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Merekam...")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "• Yang Baca%s\n\n••••••••••••••••••\n• Yang Ngintip\n%s\n••••••••••••••••••\n• Semoga• \n•Tambah jodoh\n•Tambah rejeki\n•Tambah Anak\n•Tambah Gila\n\nAmiin Ya Allah\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Mbah\nBaru Ketik Ciduk\nDASAR PIKUN ♪")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy","Kuy sini","Gok"]: #Panggil Semua Bot
              if msg.from_ in owner:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00001)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00001)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00001)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.00001)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye op","Left","Pulang"]: #Bot Ninggalin Group termasuk Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Mundur","Guys"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["Bye Minato"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Hasirama"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Itama"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Selamat bertugas"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Tunaikan Tugas Negara"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Menjaga GC wkwkwkk"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Panggil","Tagall"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Ready op" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ready op","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"maaf kalo gak sopan")
                    random.choice(KAC).sendText(msg.to,"makasih semuanya..")
                    random.choice(KAC).sendText(msg.to,"hehehhehe")
                    cl.sendText(msg.to,"★Inget Baik² Nih Logo Team Kami★\n\n★★★૦Ո૯ ƿɿ૯८૯ ੮૯คɱ★★★")
                    cl.sendImageWithUrl(msg.to,"http://oi64.tinypic.com/106xa1j.jpg")
                    cl.sendImageWithUrl(msg.to,"http://oi63.tinypic.com/125rms0.jpg")
                    cl.sendImageWithUrl(msg.to,"http://oi68.tinypic.com/kb8tae.jpg")
                    cl.sendImageWithUrl(msg.to,"http://oi63.tinypic.com/69oy2v.jpg")
                    cl.sendImageWithUrl(msg.to,"http://oi66.tinypic.com/10dxtp1.jpg")
                    cl.sendImageWithUrl(msg.to,"http://oi65.tinypic.com/2ds4y78.jpg")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'uc9363b5a4bfacd981c3e3c082bc4d5ef'}
                    cl.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            elif target in whitelist:
                              pass
                            else:
                              try:
                                klist=[cl,ki,kk,kc,ks]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              #random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              #random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        k1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        k1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
          #---------------- Copy & Back up ------------
            elif "Copy @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Copy @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  sendMessage(msg.to, "Not Found...")
                else:
                  for target in targets:
                    try:
                      cl.CloneContactProfile(target)
                      cl.sendText(msg.to, "Success Copy profile ~")
                    except Exception as e:
                      print e
                            
            elif msg.text in ["Backup","backup"]:
              if msg.from_ in owner:
                try:
                  cl.updateDisplayPicture(backup.pictureStatus)
                  cl.updateProfile(backup)
                  cl.sendText(msg.to, "Backup done")
                except Exception as e:
                  cl.sendText(msg.to, str(e))
                  
            elif "Contact bc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Contact bc ", "")
                t = cl.getAllContactIds()
                t = 100
                while(t):
                  cl.sendText(msg.to, (bctxt))
                  t-=1
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Reboot","reboot"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Oke\nKami Reboot System")
                cl.sendText(msg.to,"I'm Reboot...")
                ki.sendText(msg.to,"I'm Reboot...")
                kk.sendText(msg.to,"I'm Reboot...")
                kc.sendText(msg.to,"I'm Reboot...")
                ks.sendText(msg.to,"I'm Reboot...")
                cl.sendText(msg.to,"Reboot Done Boss") 
        #-------------Fungsi Spam Finish---------------------#
            elif "One Piece" in msg.text:
              if msg.from_ in admin:
                cl.sendImageWithUrl(msg.to,"http://oi64.tinypic.com/106xa1j.jpg")
                cl.sendImageWithUrl(msg.to,"http://oi63.tinypic.com/125rms0.jpg")
                cl.sendImageWithUrl(msg.to,"http://oi68.tinypic.com/kb8tae.jpg")
                cl.sendImageWithUrl(msg.to,"http://oi63.tinypic.com/69oy2v.jpg")
                cl.sendImageWithUrl(msg.to,"http://oi68.tinypic.com/15xl5s4.jpg")
                cl.sendImageWithUrl(msg.to,"http://oi65.tinypic.com/2z9l5ba.jpg")
                cl.sendText(msg.to,"Itu Logo Team Kami\n☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ ☆")
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = kk.getGroupIdsJoined()
                 a = kc.getGroupIdsJoined()
                 a = ks.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     kk.sendText(taf, (bctxt))
                     kc.sendText(taf, (bctxt))
                     ks.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Groups"]: #Melihat List Group
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["Groupsid"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                 gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = kk.getGroupIdsJoined()
                 gid = kc.getGroupIdsJoined()
                 gid = ks.getGroupIdsJoined()
                 for i in gid:
                   ks.leaveGroup(i)
                   kc.leaveGroup(i)
                   ki.leaveGroup(i)
                   kk.leaveGroup(i)
                   cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Sayonara")
                 else:
                   cl.sendText(msg.to,"He declined all invitations")
  #------------------------End---------------------

  #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG ??􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Absen dulu","Responsename"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"- On-")
                ki.sendText(msg.to,"- On -")
                kk.sendText(msg.to,"- On -")
                kc.sendText(msg.to,"- On-")
                ks.sendText(msg.to,"- On -")
                cl.sendText(msg.to,"Personil Lengkap Ndan\nSiap Protect Group\nDan siap Tempur")
      #-------------Fungsi Respon Finish---------------------#
            elif msg.text in ["Undang"]:
              if msg.from_ in admin:
                wait["winvite"] = True
                cl.sendText(msg.to,"Send Kontaktnya Boss 😎")
            elif msg.text in ["2undang"]:
              if msg.from_ in admin:
                wait["winvite2"] = True
                ki.sendText(msg.to,"Send Kontaktnya Boss 😎")
            elif msg.text in ["3undang"]:
              if msg.from_ in admin:
                wait["winvite3"] = True
                kk.sendText(msg.to,"Send Kontaktnya Boss 😎")
            elif msg.text in ["4undang"]:
              if msg.from_ in admin:
                wait["winvite4"] = True
                kc.sendText(msg.to,"Send Kontaktnya Boss 😎")
            elif msg.text in ["5undang"]:
              if msg.from_ in admin:
                wait["winvite5"] = True
                ks.sendText(msg.to,"Send Kontaktnya Boss 😎")
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["List"]:
                ki.sendText(msg.to,"❎▪OP▪AUTO▪BOT▪❎\n❎•Rental●Bot●Protect•\n❎•Siri•V10\n❎•GIFT STICKER & COIN•\n❎▪HANDPHONE & HEADSET▪\n❎▪VIP SMULE●i-Phone ¤ Android▪\n❎▪PULSA▪\n❎•Hubungi http://line.me/ti/p/~dwiyah89")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Sabar Mas...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Detik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ued156c86ffa56024c0acba16f7889e6d'}
              cl.sendText(msg.to,"Kenalkan")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"Kontak di atas ")
              cl.sendText(msg.to,"Itu Creator Kami Yang Pea 😜")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Maafkan saya kalau terkadang usil. namanya juga Bot kadang tak terkendali','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Poligami O.o ','Siap','Bot Dipanggilin','Ada Orang kah disini?','ngantuk','Siapa yg manggil ya?','Berisik ah...','Bat bot bat bot. gw punya nama','Apa sayang']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
            elif "Steal " in msg.text:
              if msg.from_ in admin:
                  nk0 = msg.text.replace("Steal ","")
                  nk1 = nk0.lstrip()
                  nk2 = nk1.replace("@","")
                  nk3 = nk2.rstrip()
                  _name = nk3
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for s in gs.members:
                       if _name in s.displayName:
                           targets.append(s.mid)
                  if targets == []:
                      sendMessage(msg.to,"user does not exist")
                      pass
                  else:
                      for target in targets:
                          try:
                              contact = cl.getContact(target)
                              x = contact.displayName
                              profile = cl.getProfile()
                              profile.displayName = x
                              cl.updateProfile(profile)
                              cl.sendText(msg.to,"Nyolong PP Berhasil Boss 😂")
                          except Exception as e:
                              cl.sendText(msg.to,"Fail")
                              print e
            
            elif "Ig: " in msg.text:
              if msg.from_ in admin:
                cari = msg.text.replace("Ig: ","")
                try:
                    response = requests.get("https://www.instagram.com/"+cari+"?__a=1")
                    data = response.json()
                    namaIG = str(data['user']['full_name'])
                    bioIG = str(data['user']['biography'])
                    mediaIG = str(data['user']['media']['count'])
                    verifIG = str(data['user']['is_verified'])
                    usernameIG = str(data['user']['username'])
                    followerIG = str(data['user']['followed_by']['count'])
                    profileIG = data['user']['profile_pic_url_hd']
                    privateIG = str(data['user']['is_private'])
                    followIG = str(data['user']['follows']['count'])
                    text = "==============================\n[Name] : "+namaIG+"\n[Biography] :\n"+bioIG+"\n[Follower] : "+followerIG+"\n[Following] : "+followIG+"\n[Media] : "+mediaIG+"\n[Verified] :"+verifIG+"\n[Private] : "+privateIG+"\n[Username] : "+usernameIG+"\n=============================="
                    cl.sendImageWithUrl(msg.to, profileIG)
                    cl.sendText(msg.to, str(text))
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    
            elif '/say ' in msg.text.lower():
              if msg.from_ in admin:      
                    query = msg.text.lower().replace('/say ','')
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                    
            elif '/lirik ' in msg.text.lower():
              if msg.from_ in admin:  
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                    
            #elif "Baster Band" in msg.text:
              #if msg.from_ in admin:
               # songname = msg.text.replace("Lagu: ","")
                #params = {'songname':songname}
                #r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib3.parse.urlencode(params))
                #data = r.text
                #data = json.loads(data)
                #cl.sendAudioWithUrl(msg.to, "https://m.soundcloud.com/hanavy-emang-koplaxs/baster-band-kenangan-itu-mp3")
                #cl.sendAudioWithUrl(msg.to, "https://www.reverbnation.com/basterband/song/26314484-baster-band-kenangan-itu")
                #if data == []:
                    #cl.sendText(msg.to, "Song ["+songname+"] not found")
                #else:
                    #for song in data:
                        #cl.sendAudioWithUrl(msg.to, song[4])
                        #cl.sendText(msg.to, "==============================\nSong: "+str(song[0])+"\nDuration: "+str(song[1])+"\nLink Download: "+str(song[4])+"\n==============================")
                    #pass
                  
            elif "Yusuf: " in msg.text:
              if msg.from_ in admin:
                query = msg.text.replace("Yusuf: ","")
                cl.sendText(msg.to, "Searching...")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://www.youtube.com/results'
                    params = {'search_query':query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    loop = 1
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            if loop == 0:
                                cl.sendText(msg.to, a['title']+'\nhttps://www.youtube.com'+a['href'])
                                break
                            else:
                                loop = loop - 1
            
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin:
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
            
            elif "/joox " in msg.text.lower():
              if msg.from_ in admin:
                songname = msg.text.lower().replace("/joox ","")
                params = {'songname': songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib3.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    hasil = 'This is your music\n\n'
                    hasil += 'Judul : ' + song[0]
                    hasil += '\nDurasi : ' + song[1]
                    hasil += '\nDownload Link : ' + song[4]
                    cl.sendAudioWithUrl(msg.to,song[3])
                    cl.sendText(msg.to, hasil)
                    
            elif '/music ' in msg.text.lower():
              if msg.from_ in admin:  
                try:
                    songname = msg.text.lower().replace('/music ','')
                    params = {'songname': songname}
                    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithUrl(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
                    
            elif "Pp group " in msg.text:
              if msg.from_ in admin:
                saya = msg.text.replace('Pp group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                        
            elif "Dp @" in msg.text:
              if msg.from_ in admin:
                print "[Command]dp executing"
                _name = msg.text.replace("Dp @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  cl.sendText(msg.to,"Contact not found")
                else:
                  for target in targets:
                    try:
                      contact = cl.getContact(target)
                      cu = cl.channel.getCover(target)
                      path = str(cu)
                      cl.sendImageWithUrl(msg.to,path)
                    except Exception as e:
                      raise e
                print "[Command]dp executed"
                 
            elif "Stealgroup" in msg.text:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + group.pictureStatus)
                    
            elif "Pp @" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                if targets == []:
                    cl.sendText(msg.to,"Kontak tidak ditemukan,mungkin kontak yg dituju tidak mempunyai muka")
                else:
                    for target in targets:
                      try:
                        contact = cl.getContact(target)
                        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithUrl(msg.to, path)
                      except Exception as e:
                        raise e
                        
            elif msg.text in ["Bot restart"]:
              if msg.from_ in owner:
    	          cl.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                #cl.sendText(msg.to, "Waktu Restart Sekitar 10 Detik")
                  restart_program()
                  
            elif "Anu @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Anu @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                  if _nametarget == g.displayName:
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"??ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"??ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"🔪ONE PIECE TEAM 🔪\n\nQQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
        #---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          cl.sendText(op.param1, "👥Selamat Datang Di Grup👥\n" + "👉" + str(ginfo.name) + "👈" + "\n" + "👑Founder Grup👑" + "\n" + "👉" + ginfo.creator.displayName + "👈" + "\n\n" + "     Group Ini Di Protect Oleh :" + "\n⭐||One Piece Team Protect||⭐")
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,500):
      hasil = satpam.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Pras⭐⭐👈\n\nMARS_FAMILY\nSupport By:\nOne Piece Team protect")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Sekalian Promo 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Ready 10 Bot Protect 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Ready 5 Bot Protect 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Hubungi http://line.me/ti/p/~prasetyo.86 😊")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.00001)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^Pras^\nStatus Boss udah Kami Like\nOwner Kami :\nPras\n ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Boss"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
