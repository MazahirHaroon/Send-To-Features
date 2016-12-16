import sys
import os
import requests
import string
import re
import webbrowser

def openpage(search):
            search.replace(" ", "")
            url = 'https://www.google.co.in/search?q='+search
            webbrowser.open_new(url)

search = sys.argv[1]
search = search.split("\\")
openpage(search[len(search)-1])
#callback2(search)
