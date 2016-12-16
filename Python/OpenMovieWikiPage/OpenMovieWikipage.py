import sys
import os
import requests
import string
import re
import webbrowser

def openpage(wiki):
            wiki.replace(" ", "")
            replace = [".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
            "x264","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip",
            "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian",
            "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
            "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
            "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
            "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
            "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
            "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
            "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
            "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
            "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
            "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
            "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
            "Exclusive","171","DiDee","v2"]
            for value in replace:
               wiki = wiki.replace(value," ")
            wiki = wiki.strip();
            url = 'https://www.google.co.in/search?q='+wiki+'+wikipedia'
            r = requests.get(url)
            k = r.text
            m = re.search('https://en.wikipedia.org/wiki/(.+?)/', k)
            if m:
                link = m.group(0)
                link = link.split('&amp')
                webbrowser.open_new(link[0])


wiki = sys.argv[1]
wiki = wiki.split("\\")
openpage(wiki[len(wiki)-1])
#callback2(wiki)
