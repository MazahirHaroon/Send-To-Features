import sys
import os
import requests
import string
import re
import webbrowser

def openpage(wiki):
            wiki.replace(" ", "")
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
