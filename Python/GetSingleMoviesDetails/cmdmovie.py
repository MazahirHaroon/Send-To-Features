import os
import requests
import string
import re
from Tkinter import *
import tkMessageBox
master = Tk()

def callback():
    pad=3
    master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
    text = Text(master)
    path=ent.get()
    path=ent.get()
    for root, dirs, files in os.walk(path):
        sb = Scrollbar(master,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        sb.configure(command=text.yview)
        text.configure(yscrollcommand=sb.set)
        lb = Listbox(master)
        lb.pack()
        for file in files:
            if file.endswith(".mp4"):
                 #print(os.path.join(root, file))
                 #print file
                 file = file.strip( '.mp4')
                 url = 'https://www.google.co.in/search?q='+file+'+imdb'
                 r = requests.get(url)
                 k = r.text
                 m = re.search('www.imdb.com/title/(.+?)/', k)
                 text.pack()
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
                     text.insert(INSERT, "Title1         : "+Title+"\n")
                     text.insert(INSERT, "Rating        : "+Rating+"\n")
                     text.insert(INSERT, "Released Date : "+Rls+"\n")
                     text.insert(INSERT, "Genre         : "+Genre+"\n")
                     text.insert(INSERT, "Director      : "+Director+"\n")
                     text.insert(INSERT, "Writer        : "+Writer+"\n")
                     text.insert(INSERT, "Cast          : "+Actors+"\n\n")
                     text.insert(INSERT, "Synopsis:\n")
                     text.insert(INSERT, Plot+"\n\n")
    text.tag_add("here", "1.0", "1.4")
    text.tag_add("start", "1.8", "1.13")

def callback2(film):
            film.replace(" ", "")
            pad=3
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            text = Text(master)
            master.title("MovieSort")
        #    film=ent.get()
            tkMessageBox.showinfo("MovieSort", "Please Wait, details about '"+film+"' is on the way!")
            url = 'https://www.google.co.in/search?q='+film+'+imdb'
            #print url
            #mm = url
            r = requests.get(url)
            k = r.text
            m = re.search('www.imdb.com/title/(.+?)/', k)
            text.pack()
            sb = Scrollbar(master,orient=VERTICAL)
            sb.pack(side=RIGHT,fill=Y)
            sb.configure(command=text.yview)
            text.configure(yscrollcommand=sb.set)
            if m:
                    found = m.group(1)
                    #print found
                    m = re.search('www.imdb.com/title/(.+?)/', k)
                    text.pack()
                    movie = 'http://www.omdbapi.com/?i='+found+'&plot=short&r=json'
                    #mm = movie
                    r = requests.get(movie)
                    k = r.text
                    m = re.search('Title":"(.+?)",', k)
                    Title = m.group(1)
                    #print Title
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
                    if(Title!=film):
                            text.insert(CURRENT, "Showing Result for "+Title+"\n\n")
                    text.insert(CURRENT, "Title         : "+Title+"\n")
                    text.insert(INSERT, "Rating        : "+Rating+"\n")
                    text.insert(INSERT, "Released Date : "+Rls+"\n")
                    text.insert(INSERT, "Genre         : "+Genre+"\n")
                    text.insert(INSERT, "Director      : "+Director+"\n")
                    text.insert(INSERT, "Writer        : "+Writer+"\n")
                    text.insert(INSERT, "Cast          : "+Actors+"\n\n")
                    text.insert(INSERT, "Synopsis:\n")
                    text.insert(INSERT, Plot+"\n\n")

                    text.tag_config("Movie Number :", background="yellow", foreground="blue")
                    text.tag_config("Title         : ", foreground="blue")
                    text.tag_config("Rating        ", foreground="blue")
                    text.tag_config("Released Date : ", foreground="blue")
                    text.tag_config("Genre         : ", foreground="blue")
film = sys.argv[1]
film = film.split("\\")
callback2(film[len(film)-1])
#callback2(film)
mainloop()
