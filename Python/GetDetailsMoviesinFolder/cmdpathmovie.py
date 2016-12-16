import os
import requests
import string
import re
from Tkinter import *
import tkMessageBox
import Tkinter as tki # Tkinter -> tkinter in Python3

class App(object):

    def __init__(self,path):
        self.root = tki.Tk()
        text = Text(self.root)

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        tkMessageBox.showinfo("MovieSort", "Please Wait, details about all the movies in '"+path+"' is on the way!")
        count=0
        #path=ent.get()
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".m4v") or file.endswith(".mkv"):
                    count = count + 1
        self.txt.insert(INSERT, "          Total movies count: "+str(count)+" movies\n\n")
        for root, dirs, files in os.walk(path):
            num=0
            for file in files:
                num=num+1
                if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".m4v") or file.endswith(".mkv"):
                     #print(os.path.join(root, file))
                     #print file
                     file = file.strip( '.mp4')
                     url = 'https://www.google.co.in/search?q='+file+'+imdb'
                     r = requests.get(url)
                     k = r.text
                     m = re.search('www.imdb.com/title/(.+?)/', k)
                     if m:
                         found = m.group(1)
                         #print found
                         movie = 'http://www.omdbapi.com/?i='+found+'&plot=short&r=json'
                         r = requests.get(movie)
                         k = r.text
                         m = re.search('Title":"(.+?)",', k)
                         Title = m.group(1)
                         m = re.search('imdbRating":"(.+?)",', k)
                         Rating = m.group(1)
                         m = re.search('Genre":"(.+?)",', k)
                         Genre = m.group(1)
                         m = re.search('Director":"(.+?)",', k)
                         Director = m.group(1)
                         m = re.search('Writer":"(.+?)",', k)
                         Writer = m.group(1)
                         m = re.search('Plot":"(.+?)",', k)
                         Plot = m.group(1)
                         m = re.search('Actors":"(.+?)",', k)
                         Actors = m.group(1)
                         m = re.search('Released":"(.+?)",', k)
                         Rls = m.group(1)
                             #tkMessageBox.showinfo( "Input", m,)
                         self.txt.insert(INSERT, "Movie: "+str(num)+"\n")
                         self.txt.insert(INSERT, "Title        : "+Title+"\n")
                         self.txt.insert(INSERT, "Rating        : "+Rating+"\n")
                         self.txt.insert(INSERT, "Released Date : "+Rls+"\n")
                         self.txt.insert(INSERT, "Genre         : "+Genre+"\n")
                         self.txt.insert(INSERT, "Director      : "+Director+"\n")
                         self.txt.insert(INSERT, "Writer        : "+Writer+"\n")
                         self.txt.insert(INSERT, "Cast          : "+Actors+"\n\n")
                         self.txt.insert(INSERT, "Synopsis:\n")
                         self.txt.insert(INSERT, Plot+"\n\n")


path = sys.argv[1]
app = App(path)
#_init_(self,path)
app.root.mainloop()
