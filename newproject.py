import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=4752230de43d4333bfcb1f063dd69ecf').json()
        
        self.load_gui()
        
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('450x600')
    
        self.root.title('Mera News App')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

    
        self.clear()

      
        Topheading=Label(self.root,text="Top News",bg='Red',fg='white')
        Topheading.config(font=('veedana',20))
        Topheading.pack(pady=(3))

        headlines = Label(self.root,text=self.data['articles'][index]['title'],width=30,bg="black",fg="white",wraplength=350)
        headlines.pack(pady=(10,30))
        headlines.config(font=('verdana',18))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,justify='center')
        details.pack(pady=(50))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)
            prev.pack(padx=(20,10))

        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(padx=(10))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=RIGHT,padx=(0,10))


        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()